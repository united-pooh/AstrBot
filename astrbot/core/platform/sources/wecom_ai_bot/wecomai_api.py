"""企业微信智能机器人 API 客户端
处理消息加密解密、API 调用等
"""

import base64
import hashlib
import json
from typing import Any

import aiohttp
from Crypto.Cipher import AES

from astrbot import logger
from astrbot.core.lang import t

from .wecomai_utils import WecomAIBotConstants
from .WXBizJsonMsgCrypt import WXBizJsonMsgCrypt


class WecomAIBotAPIClient:
    """企业微信智能机器人 API 客户端"""

    def __init__(self, token: str, encoding_aes_key: str) -> None:
        """初始化 API 客户端

        Args:
            token: 企业微信机器人 Token
            encoding_aes_key: 消息加密密钥

        """
        self.token = token
        self.encoding_aes_key = encoding_aes_key
        self.wxcpt = WXBizJsonMsgCrypt(token, encoding_aes_key, "")  # receiveid 为空串

    async def decrypt_message(
        self,
        encrypted_data: bytes,
        msg_signature: str,
        timestamp: str,
        nonce: str,
    ) -> tuple[int, dict[str, Any] | None]:
        """解密企业微信消息

        Args:
            encrypted_data: 加密的消息数据
            msg_signature: 消息签名
            timestamp: 时间戳
            nonce: 随机数

        Returns:
            (错误码, 解密后的消息数据字典)

        """
        try:
            ret, decrypted_msg = self.wxcpt.DecryptMsg(
                encrypted_data,
                msg_signature,
                timestamp,
                nonce,
            )

            if ret != WecomAIBotConstants.SUCCESS:
                logger.error(
                    t(
                        "core-platform-sources-wecom_ai_bot-wecomai_api-message_decryption_failed",
                        ret=ret,
                    )
                )
                return ret, None

            # 解析 JSON
            if decrypted_msg:
                try:
                    message_data = json.loads(decrypted_msg)
                    logger.debug(
                        t(
                            "core-platform-sources-wecom_ai_bot-wecomai_api-decryption_successful",
                            message_data=message_data,
                        )
                    )
                    return WecomAIBotConstants.SUCCESS, message_data
                except json.JSONDecodeError as e:
                    logger.error(
                        t(
                            "core-platform-sources-wecom_ai_bot-wecomai_api-json_parsing_failed",
                            e=e,
                            decrypted_msg=decrypted_msg,
                        )
                    )
                    return WecomAIBotConstants.PARSE_XML_ERROR, None
            else:
                logger.error(
                    t(
                        "core-platform-sources-wecom_ai_bot-wecomai_api-decrypted_message_empty"
                    )
                )
                return WecomAIBotConstants.DECRYPT_ERROR, None

        except Exception as e:
            logger.error(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-decryption_process_exception",
                    e=e,
                )
            )
            return WecomAIBotConstants.DECRYPT_ERROR, None

    async def encrypt_message(
        self,
        plain_message: str,
        nonce: str,
        timestamp: str,
    ) -> str | None:
        """加密消息

        Args:
            plain_message: 明文消息
            nonce: 随机数
            timestamp: 时间戳

        Returns:
            加密后的消息，失败时返回 None

        """
        try:
            ret, encrypted_msg = self.wxcpt.EncryptMsg(plain_message, nonce, timestamp)

            if ret != WecomAIBotConstants.SUCCESS:
                logger.error(
                    t(
                        "core-platform-sources-wecom_ai_bot-wecomai_api-message_encryption_failed",
                        ret=ret,
                    )
                )
                return None

            logger.debug(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-encryption_successful"
                )
            )
            return encrypted_msg

        except Exception as e:
            logger.error(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-encryption_process_exception",
                    e=e,
                )
            )
            return None

    def verify_url(
        self,
        msg_signature: str,
        timestamp: str,
        nonce: str,
        echostr: str,
    ) -> str:
        """验证回调 URL

        Args:
            msg_signature: 消息签名
            timestamp: 时间戳
            nonce: 随机数
            echostr: 验证字符串

        Returns:
            验证结果字符串

        """
        try:
            ret, echo_result = self.wxcpt.VerifyURL(
                msg_signature,
                timestamp,
                nonce,
                echostr,
            )

            if ret != WecomAIBotConstants.SUCCESS:
                logger.error(
                    t(
                        "core-platform-sources-wecom_ai_bot-wecomai_api-url_validation_failed",
                        ret=ret,
                    )
                )
                return "verify fail"

            logger.info(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-url_validation_successful"
                )
            )
            return echo_result if echo_result else "verify fail"

        except Exception as e:
            logger.error(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-url_validation_exception",
                    e=e,
                )
            )
            return "verify fail"

    async def process_encrypted_image(
        self,
        image_url: str,
        aes_key_base64: str | None = None,
    ) -> tuple[bool, bytes | str]:
        """下载并解密加密图片

        Args:
            image_url: 加密图片的 URL
            aes_key_base64: Base64 编码的 AES 密钥，如果为 None 则使用实例的密钥

        Returns:
            (是否成功, 图片数据或错误信息)

        """
        try:
            # 下载图片
            logger.info(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-downloading_encrypted_image",
                    image_url=image_url,
                )
            )

            async with aiohttp.ClientSession() as session:
                async with session.get(image_url, timeout=15) as response:
                    if response.status != 200:
                        error_msg = t(
                            "core-platform-sources-wecom_ai_bot-wecomai_api-image_download_failed_status",
                            response=response,
                        )
                        logger.error(error_msg)
                        return False, error_msg

                    encrypted_data = await response.read()
                    logger.info(
                        t(
                            "core-platform-sources-wecom_ai_bot-wecomai_api-image_download_success",
                            encrypted_data=encrypted_data,
                        )
                    )

            # 准备解密密钥
            if aes_key_base64 is None:
                aes_key_base64 = self.encoding_aes_key

            if not aes_key_base64:
                raise ValueError(
                    t(
                        "core-platform-sources-wecom_ai_bot-wecomai_api-aes_key_cannot_be_empty"
                    )
                )

            # Base64 解码密钥
            aes_key = base64.b64decode(
                aes_key_base64 + "=" * (-len(aes_key_base64) % 4),
            )
            if len(aes_key) != 32:
                raise ValueError(
                    t(
                        "core-platform-sources-wecom_ai_bot-wecomai_api-invalid_aes_key_length"
                    )
                )

            iv = aes_key[:16]  # 初始向量为密钥前 16 字节

            # 解密图片数据
            cipher = AES.new(aes_key, AES.MODE_CBC, iv)
            decrypted_data = cipher.decrypt(encrypted_data)

            # 去除 PKCS#7 填充
            pad_len = decrypted_data[-1]
            if pad_len > 32:  # AES-256 块大小为 32 字节
                raise ValueError(
                    t(
                        "core-platform-sources-wecom_ai_bot-wecomai_api-invalid_padding_length"
                    )
                )

            decrypted_data = decrypted_data[:-pad_len]
            logger.info(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-image_decrypt_success",
                    decrypted_data=decrypted_data,
                )
            )

            return True, decrypted_data

        except aiohttp.ClientError as e:
            error_msg = t(
                "core-platform-sources-wecom_ai_bot-wecomai_api-image_download_failed_exception",
                e=e,
            )
            logger.error(error_msg)
            return False, error_msg

        except ValueError as e:
            error_msg = t(
                "core-platform-sources-wecom_ai_bot-wecomai_api-parameter_error", e=e
            )
            logger.error(error_msg)
            return False, error_msg

        except Exception as e:
            error_msg = t(
                "core-platform-sources-wecom_ai_bot-wecomai_api-image_processing_exception",
                e=e,
            )
            logger.error(error_msg)
            return False, error_msg


class WecomAIBotStreamMessageBuilder:
    """企业微信智能机器人流消息构建器"""

    @staticmethod
    def make_text_stream(stream_id: str, content: str, finish: bool = False) -> str:
        """构建文本流消息

        Args:
            stream_id: 流 ID
            content: 文本内容
            finish: 是否结束

        Returns:
            JSON 格式的流消息字符串

        """
        plain = {
            "msgtype": WecomAIBotConstants.MSG_TYPE_STREAM,
            "stream": {"id": stream_id, "finish": finish, "content": content},
        }
        return json.dumps(plain, ensure_ascii=False)

    @staticmethod
    def make_image_stream(
        stream_id: str,
        image_data: bytes,
        finish: bool = False,
    ) -> str:
        """构建图片流消息

        Args:
            stream_id: 流 ID
            image_data: 图片二进制数据
            finish: 是否结束

        Returns:
            JSON 格式的流消息字符串

        """
        image_md5 = hashlib.md5(image_data).hexdigest()
        image_base64 = base64.b64encode(image_data).decode("utf-8")

        plain = {
            "msgtype": WecomAIBotConstants.MSG_TYPE_STREAM,
            "stream": {
                "id": stream_id,
                "finish": finish,
                "msg_item": [
                    {
                        "msgtype": WecomAIBotConstants.MSG_TYPE_IMAGE,
                        "image": {"base64": image_base64, "md5": image_md5},
                    },
                ],
            },
        }
        return json.dumps(plain, ensure_ascii=False)

    @staticmethod
    def make_mixed_stream(
        stream_id: str,
        content: str,
        msg_items: list,
        finish: bool = False,
    ) -> str:
        """构建混合类型流消息

        Args:
            stream_id: 流 ID
            content: 文本内容
            msg_items: 消息项列表
            finish: 是否结束

        Returns:
            JSON 格式的流消息字符串

        """
        plain = {
            "msgtype": WecomAIBotConstants.MSG_TYPE_STREAM,
            "stream": {"id": stream_id, "finish": finish, "msg_item": msg_items},
        }
        if content:
            plain["stream"]["content"] = content
        return json.dumps(plain, ensure_ascii=False)

    @staticmethod
    def make_text(content: str) -> str:
        """构建文本消息

        Args:
            content: 文本内容

        Returns:
            JSON 格式的文本消息字符串

        """
        plain = {"msgtype": "text", "text": {"content": content}}
        return json.dumps(plain, ensure_ascii=False)


class WecomAIBotMessageParser:
    """企业微信智能机器人消息解析器"""

    @staticmethod
    def parse_text_message(data: dict[str, Any]) -> str | None:
        """解析文本消息

        Args:
            data: 消息数据

        Returns:
            文本内容，解析失败返回 None

        """
        try:
            return data.get("text", {}).get("content")
        except (KeyError, TypeError):
            logger.warning(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-text_message_parse_failed"
                )
            )
            return None

    @staticmethod
    def parse_image_message(data: dict[str, Any]) -> str | None:
        """解析图片消息

        Args:
            data: 消息数据

        Returns:
            图片 URL，解析失败返回 None

        """
        try:
            return data.get("image", {}).get("url")
        except (KeyError, TypeError):
            logger.warning(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-image_message_parse_failed"
                )
            )
            return None

    @staticmethod
    def parse_stream_message(data: dict[str, Any]) -> dict[str, Any] | None:
        """解析流消息

        Args:
            data: 消息数据

        Returns:
            流消息数据，解析失败返回 None

        """
        try:
            stream_data = data.get("stream", {})
            return {
                "id": stream_data.get("id"),
                "finish": stream_data.get("finish"),
                "content": stream_data.get("content"),
                "msg_item": stream_data.get("msg_item", []),
            }
        except (KeyError, TypeError):
            logger.warning(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-stream_message_parse_failed"
                )
            )
            return None

    @staticmethod
    def parse_mixed_message(data: dict[str, Any]) -> list | None:
        """解析混合消息

        Args:
            data: 消息数据

        Returns:
            消息项列表，解析失败返回 None

        """
        try:
            return data.get("mixed", {}).get("msg_item", [])
        except (KeyError, TypeError):
            logger.warning(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-mixed_message_parse_failed"
                )
            )
            return None

    @staticmethod
    def parse_event_message(data: dict[str, Any]) -> dict[str, Any] | None:
        """解析事件消息

        Args:
            data: 消息数据

        Returns:
            事件数据，解析失败返回 None

        """
        try:
            return data.get("event", {})
        except (KeyError, TypeError):
            logger.warning(
                t(
                    "core-platform-sources-wecom_ai_bot-wecomai_api-event_message_parse_failed"
                )
            )
            return None
