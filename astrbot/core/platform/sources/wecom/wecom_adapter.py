import asyncio
import os
import sys
import uuid
from collections.abc import Awaitable, Callable
from typing import Any, cast

import quart
from requests import Response
from wechatpy.enterprise import WeChatClient, parse_message
from wechatpy.enterprise.crypto import WeChatCrypto
from wechatpy.enterprise.messages import ImageMessage, TextMessage, VoiceMessage
from wechatpy.exceptions import InvalidSignatureException
from wechatpy.messages import BaseMessage

from astrbot.api.event import MessageChain
from astrbot.api.message_components import Image, Plain, Record
from astrbot.api.platform import (
    AstrBotMessage,
    MessageMember,
    MessageType,
    Platform,
    PlatformMetadata,
    register_platform_adapter,
)
from astrbot.core import logger
from astrbot.core.lang import t
from astrbot.core.platform.astr_message_event import MessageSesion
from astrbot.core.utils.astrbot_path import get_astrbot_temp_path
from astrbot.core.utils.media_utils import convert_audio_to_wav
from astrbot.core.utils.webhook_utils import log_webhook_info

from .wecom_event import WecomPlatformEvent
from .wecom_kf import WeChatKF
from .wecom_kf_message import WeChatKFMessage

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class WecomServer:
    def __init__(self, event_queue: asyncio.Queue, config: dict) -> None:
        self.server = quart.Quart(__name__)
        self.port = int(cast(str, config.get("port")))
        self.callback_server_host = config.get("callback_server_host", "0.0.0.0")
        self.server.add_url_rule(
            "/callback/command",
            view_func=self.verify,
            methods=["GET"],
        )
        self.server.add_url_rule(
            "/callback/command",
            view_func=self.callback_command,
            methods=["POST"],
        )
        self.event_queue = event_queue

        self.crypto = WeChatCrypto(
            config["token"].strip(),
            config["encoding_aes_key"].strip(),
            config["corpid"].strip(),
        )

        self.callback: Callable[[BaseMessage], Awaitable[None]] | None = None
        self.shutdown_event = asyncio.Event()

    async def verify(self):
        """内部服务器的 GET 验证入口"""
        return await self.handle_verify(quart.request)

    async def handle_verify(self, request) -> str:
        """处理验证请求，可被统一 webhook 入口复用

        Args:
            request: Quart 请求对象

        Returns:
            验证响应
        """
        logger.info(
            t(
                "core-platform-sources-wecom-wecom_adapter-validating_request",
                request=request,
            )
        )
        args = request.args
        try:
            echo_str = self.crypto.check_signature(
                args.get("msg_signature"),
                args.get("timestamp"),
                args.get("nonce"),
                args.get("echostr"),
            )
            logger.info(
                t("core-platform-sources-wecom-wecom_adapter-validation_success")
            )
            return echo_str
        except InvalidSignatureException:
            logger.error(
                t(
                    "core-platform-sources-wecom-wecom_adapter-validation_signature_failure"
                )
            )
            raise

    async def callback_command(self):
        """内部服务器的 POST 回调入口"""
        return await self.handle_callback(quart.request)

    async def handle_callback(self, request) -> str:
        """处理回调请求，可被统一 webhook 入口复用

        Args:
            request: Quart 请求对象

        Returns:
            响应内容
        """
        data = await request.get_data()
        msg_signature = request.args.get("msg_signature")
        timestamp = request.args.get("timestamp")
        nonce = request.args.get("nonce")
        try:
            xml = self.crypto.decrypt_message(data, msg_signature, timestamp, nonce)
        except InvalidSignatureException:
            logger.error(
                t(
                    "core-platform-sources-wecom-wecom_adapter-error_decryption_signature_failed"
                )
            )
            raise
        else:
            msg = cast(BaseMessage, parse_message(xml))
            logger.info(
                t(
                    "core-platform-sources-wecom-wecom_adapter-info_parse_success",
                    msg=msg,
                )
            )

            if self.callback:
                await self.callback(msg)

        return "success"

    async def start_polling(self) -> None:
        logger.info(
            t("core-platform-sources-wecom-wecom_adapter-starting_adapter", self=self),
        )
        await self.server.run_task(
            host=self.callback_server_host,
            port=self.port,
            shutdown_trigger=self.shutdown_trigger,
        )

    async def shutdown_trigger(self) -> None:
        await self.shutdown_event.wait()


@register_platform_adapter(
    "wecom",
    t("core-platform-sources-wecom-wecom_adapter-register_adapter_decorator"),
    support_streaming_message=False,
)
class WecomPlatformAdapter(Platform):
    def __init__(
        self,
        platform_config: dict,
        platform_settings: dict,
        event_queue: asyncio.Queue,
    ) -> None:
        super().__init__(platform_config, event_queue)
        self.settingss = platform_settings
        self.client_self_id = uuid.uuid4().hex[:8]
        self.api_base_url = platform_config.get(
            "api_base_url",
            "https://qyapi.weixin.qq.com/cgi-bin/",
        )
        self.unified_webhook_mode = platform_config.get("unified_webhook_mode", False)

        if not self.api_base_url:
            self.api_base_url = "https://qyapi.weixin.qq.com/cgi-bin/"

        self.api_base_url = self.api_base_url.removesuffix("/")
        if not self.api_base_url.endswith("/cgi-bin"):
            self.api_base_url += "/cgi-bin"

        if not self.api_base_url.endswith("/"):
            self.api_base_url += "/"

        self.server = WecomServer(self._event_queue, self.config)
        self.agent_id: str | None = None

        self.client = WeChatClient(
            self.config["corpid"].strip(),
            self.config["secret"].strip(),
        )

        # 微信客服
        self.kf_name = self.config.get("kf_name", None)
        if self.kf_name:
            # inject
            self.wechat_kf_api = WeChatKF(client=self.client)
            self.wechat_kf_message_api = WeChatKFMessage(self.client)
            self.client.__setattr__("kf", self.wechat_kf_api)
            self.client.__setattr__("kf_message", self.wechat_kf_message_api)

        self.client.__setattr__("API_BASE_URL", self.api_base_url)

        async def callback(msg: BaseMessage) -> None:
            if msg.type == "unknown" and msg._data["Event"] == "kf_msg_or_event":

                def get_latest_msg_item() -> dict | None:
                    token = msg._data["Token"]
                    kfid = msg._data["OpenKfId"]
                    has_more = 1
                    ret = {}
                    while has_more:
                        ret = self.wechat_kf_api.sync_msg(token, kfid)
                        has_more = ret["has_more"]
                    msg_list = ret.get("msg_list", [])
                    if msg_list:
                        return msg_list[-1]
                    return None

                msg_new = await asyncio.get_event_loop().run_in_executor(
                    None,
                    get_latest_msg_item,
                )
                if msg_new:
                    await self.convert_wechat_kf_message(msg_new)
                return
            await self.convert_message(msg)

        self.server.callback = callback

    @override
    async def send_by_session(
        self,
        session: MessageSesion,
        message_chain: MessageChain,
    ) -> None:
        # 企业微信客服不支持主动发送
        if hasattr(self.client, "kf_message"):
            logger.warning(
                t(
                    "core-platform-sources-wecom-wecom_adapter-warning_session_send_unsupported"
                )
            )
            await super().send_by_session(session, message_chain)
            return
        if not self.agent_id:
            logger.warning(
                t(
                    "core-platform-sources-wecom-wecom_adapter-send_by_session_failed",
                    session=session,
                ),
            )
            await super().send_by_session(session, message_chain)
            return

        message_obj = AstrBotMessage()
        message_obj.self_id = self.agent_id
        message_obj.session_id = session.session_id
        message_obj.type = session.message_type
        message_obj.sender = MessageMember(session.session_id, session.session_id)
        message_obj.message = []
        message_obj.message_str = ""
        message_obj.message_id = uuid.uuid4().hex
        message_obj.raw_message = {"_proactive_send": True}

        event = WecomPlatformEvent(
            message_str=message_obj.message_str,
            message_obj=message_obj,
            platform_meta=self.meta(),
            session_id=message_obj.session_id,
            client=self.client,
        )
        await event.send(message_chain)
        await super().send_by_session(session, message_chain)

    @override
    def meta(self) -> PlatformMetadata:
        return PlatformMetadata(
            "wecom",
            t("core-platform-sources-wecom-wecom_adapter-label_wecom_adapter"),
            id=self.config.get("id", "wecom"),
            support_streaming_message=False,
            support_proactive_message=False,
        )

    @override
    async def run(self) -> None:
        loop = asyncio.get_event_loop()
        if self.kf_name:
            try:
                acc_list = (
                    await loop.run_in_executor(
                        None,
                        self.wechat_kf_api.get_account_list,
                    )
                ).get("account_list", [])
                logger.debug(
                    t(
                        "core-platform-sources-wecom-wecom_adapter-got_customer_service_list",
                        acc_list=acc_list,
                    )
                )
                for acc in acc_list:
                    name = acc.get("name", None)
                    if name != self.kf_name:
                        continue
                    open_kfid = acc.get("open_kfid", None)
                    if not open_kfid:
                        logger.error(
                            t(
                                "core-platform-sources-wecom-wecom_adapter-error_kf_open_kfid_empty"
                            )
                        )
                    logger.debug(f"Found open_kfid: {open_kfid!s}")
                    kf_url = (
                        await loop.run_in_executor(
                            None,
                            self.wechat_kf_api.add_contact_way,
                            open_kfid,
                            "astrbot_placeholder",
                        )
                    ).get("url", "")
                    logger.info(
                        t(
                            "core-platform-sources-wecom-wecom_adapter-info_scan_qrcode_for_kf",
                            kf_url=kf_url,
                        ),
                    )
            except Exception as e:
                logger.error(e)

        # 如果启用统一 webhook 模式，则不启动独立服务器
        webhook_uuid = self.config.get("webhook_uuid")
        if self.unified_webhook_mode and webhook_uuid:
            log_webhook_info(
                t(
                    "core-platform-sources-wecom-wecom_adapter-wecom_webhook_info",
                    id=self.meta().id,
                ),
                webhook_uuid,
            )
            # 保持运行状态，等待 shutdown
            await self.server.shutdown_event.wait()
        else:
            await self.server.start_polling()

    async def webhook_callback(self, request: Any) -> Any:
        """统一 Webhook 回调入口"""
        # 根据请求方法分发到不同的处理函数
        if request.method == "GET":
            return await self.server.handle_verify(request)
        else:
            return await self.server.handle_callback(request)

    async def convert_message(self, msg: BaseMessage) -> AstrBotMessage | None:
        abm = AstrBotMessage()
        if isinstance(msg, TextMessage):
            abm.message_str = msg.content
            abm.self_id = str(msg.agent)
            abm.message = [Plain(msg.content)]
            abm.type = MessageType.FRIEND_MESSAGE
            abm.sender = MessageMember(
                cast(str, msg.source),
                cast(str, msg.source),
            )
            abm.message_id = str(msg.id)
            abm.timestamp = int(cast(int | str, msg.time))
            abm.session_id = abm.sender.user_id
            abm.raw_message = msg
        elif isinstance(msg, ImageMessage):
            abm.message_str = t(
                "core-platform-sources-wecom-wecom_adapter-message_image_placeholder"
            )
            abm.self_id = str(msg.agent)
            abm.message = [Image(file=msg.image, url=msg.image)]
            abm.type = MessageType.FRIEND_MESSAGE
            abm.sender = MessageMember(
                cast(str, msg.source),
                cast(str, msg.source),
            )
            abm.message_id = str(msg.id)
            abm.timestamp = int(cast(int | str, msg.time))
            abm.session_id = abm.sender.user_id
            abm.raw_message = msg
        elif isinstance(msg, VoiceMessage):
            resp: Response = await asyncio.get_event_loop().run_in_executor(
                None,
                self.client.media.download,
                msg.media_id,
            )
            temp_dir = get_astrbot_temp_path()
            path = os.path.join(temp_dir, f"wecom_{msg.media_id}.amr")
            with open(path, "wb") as f:
                f.write(resp.content)

            try:
                path_wav = os.path.join(temp_dir, f"wecom_{msg.media_id}.wav")
                path_wav = await convert_audio_to_wav(path, path_wav)
            except Exception as e:
                logger.error(
                    t(
                        "core-platform-sources-wecom-wecom_adapter-error_audio_convert_failed",
                        e=e,
                    )
                )
                path_wav = path
                return

            abm.message_str = ""
            abm.self_id = str(msg.agent)
            abm.message = [Record(file=path_wav, url=path_wav)]
            abm.type = MessageType.FRIEND_MESSAGE
            abm.sender = MessageMember(
                cast(str, msg.source),
                cast(str, msg.source),
            )
            abm.message_id = str(msg.id)
            abm.timestamp = int(cast(int | str, msg.time))
            abm.session_id = abm.sender.user_id
            abm.raw_message = msg
        else:
            logger.warning(
                t(
                    "core-platform-sources-wecom-wecom_adapter-unimplemented_event",
                    msg=msg,
                )
            )
            return

        self.agent_id = abm.self_id
        logger.info(f"abm: {abm}")
        await self.handle_msg(abm)

    async def convert_wechat_kf_message(self, msg: dict) -> AstrBotMessage | None:
        msgtype = msg.get("msgtype")
        external_userid = cast(str, msg.get("external_userid"))
        abm = AstrBotMessage()
        abm.raw_message = msg
        abm.raw_message["_wechat_kf_flag"] = None  # 方便处理
        abm.self_id = msg["open_kfid"]
        abm.sender = MessageMember(external_userid, external_userid)
        abm.session_id = external_userid
        abm.type = MessageType.FRIEND_MESSAGE
        abm.message_id = msg.get("msgid", uuid.uuid4().hex[:8])
        abm.message_str = ""
        if msgtype == "text":
            text = msg.get("text", {}).get("content", "").strip()
            abm.message = [Plain(text=text)]
            abm.message_str = text
        elif msgtype == "image":
            media_id = msg.get("image", {}).get("media_id", "")
            resp: Response = await asyncio.get_event_loop().run_in_executor(
                None,
                self.client.media.download,
                media_id,
            )
            temp_dir = get_astrbot_temp_path()
            path = os.path.join(temp_dir, f"weixinkefu_{media_id}.jpg")
            with open(path, "wb") as f:
                f.write(resp.content)
            abm.message = [Image(file=path, url=path)]
        elif msgtype == "voice":
            media_id = msg.get("voice", {}).get("media_id", "")
            resp: Response = await asyncio.get_event_loop().run_in_executor(
                None,
                self.client.media.download,
                media_id,
            )

            temp_dir = get_astrbot_temp_path()
            path = os.path.join(temp_dir, f"weixinkefu_{media_id}.amr")
            with open(path, "wb") as f:
                f.write(resp.content)

            try:
                path_wav = os.path.join(temp_dir, f"weixinkefu_{media_id}.wav")
                path_wav = await convert_audio_to_wav(path, path_wav)
            except Exception as e:
                logger.error(
                    t(
                        "core-platform-sources-wecom-wecom_adapter-error_audio_convert_failed_2",
                        e=e,
                    )
                )
                path_wav = path
                return

            abm.message = [Record(file=path_wav, url=path_wav)]
        else:
            logger.warning(
                t(
                    "core-platform-sources-wecom-wecom_adapter-warning_kf_message_not_implemented",
                    msg=msg,
                )
            )
            return
        await self.handle_msg(abm)

    async def handle_msg(self, message: AstrBotMessage) -> None:
        message_event = WecomPlatformEvent(
            message_str=message.message_str,
            message_obj=message,
            platform_meta=self.meta(),
            session_id=message.session_id,
            client=self.client,
        )
        self.commit_event(message_event)

    def get_client(self) -> WeChatClient:
        return self.client

    async def terminate(self) -> None:
        self.server.shutdown_event.set()
        try:
            await self.server.server.shutdown()
        except Exception as _:
            pass
        logger.info(t("core-platform-sources-wecom-wecom_adapter-info_adapter_closed"))
