import asyncio
import base64
import json
import os
import traceback
import uuid

import aiohttp

from astrbot import logger
from astrbot.core.lang import t
from astrbot.core.utils.astrbot_path import get_astrbot_temp_path

from ..entities import ProviderType
from ..provider import TTSProvider
from ..register import register_provider_adapter


@register_provider_adapter(
    "volcengine_tts",
    t("core-provider-sources-volcengine_tts-service_title"),
    provider_type=ProviderType.TEXT_TO_SPEECH,
)
class ProviderVolcengineTTS(TTSProvider):
    def __init__(self, provider_config: dict, provider_settings: dict) -> None:
        super().__init__(provider_config, provider_settings)
        self.api_key = provider_config.get("api_key", "")
        self.appid = provider_config.get("appid", "")
        self.cluster = provider_config.get("volcengine_cluster", "")
        self.voice_type = provider_config.get("volcengine_voice_type", "")
        self.speed_ratio = provider_config.get("volcengine_speed_ratio", 1.0)
        self.api_base = provider_config.get(
            "api_base",
            "https://openspeech.bytedance.com/api/v1/tts",
        )
        self.timeout = provider_config.get("timeout", 20)

    def _build_request_payload(self, text: str) -> dict:
        return {
            "app": {
                "appid": self.appid,
                "token": self.api_key,
                "cluster": self.cluster,
            },
            "user": {"uid": str(uuid.uuid4())},
            "audio": {
                "voice_type": self.voice_type,
                "encoding": "mp3",
                "speed_ratio": self.speed_ratio,
                "volume_ratio": 1.0,
                "pitch_ratio": 1.0,
            },
            "request": {
                "reqid": str(uuid.uuid4()),
                "text": text,
                "text_type": "plain",
                "operation": "query",
                "with_frontend": 1,
                "frontend_type": "unitTson",
            },
        }

    async def get_audio(self, text: str) -> str:
        """异步方法获取语音文件路径"""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer; {self.api_key}",
        }

        payload = self._build_request_payload(text)

        logger.debug(
            t(
                "core-provider-sources-volcengine_tts-debug_request_headers",
                headers=headers,
            )
        )
        logger.debug(
            t("core-provider-sources-volcengine_tts-debug_request_url", self=self)
        )
        logger.debug(
            t(
                "core-provider-sources-volcengine_tts-debug_request_body",
                ensure_ascii=json.dumps(payload, ensure_ascii=False)[:100],
            )
        )

        try:
            async with (
                aiohttp.ClientSession() as session,
                session.post(
                    self.api_base,
                    data=json.dumps(payload),
                    headers=headers,
                    timeout=self.timeout,
                ) as response,
            ):
                logger.debug(
                    t(
                        "core-provider-sources-volcengine_tts-debug_response_status",
                        response=response,
                    )
                )

                response_text = await response.text()
                logger.debug(
                    t(
                        "core-provider-sources-volcengine_tts-debug_response_content",
                        response_text=response_text[:200],
                    )
                )

                if response.status == 200:
                    resp_data = json.loads(response_text)

                    if "data" in resp_data:
                        audio_data = base64.b64decode(resp_data["data"])

                        temp_dir = get_astrbot_temp_path()
                        os.makedirs(temp_dir, exist_ok=True)
                        file_path = os.path.join(
                            temp_dir,
                            f"volcengine_tts_{uuid.uuid4()}.mp3",
                        )

                        loop = asyncio.get_running_loop()
                        await loop.run_in_executor(
                            None,
                            lambda: open(file_path, "wb").write(audio_data),
                        )

                        return file_path
                    error_msg = resp_data.get(
                        "message",
                        t(
                            "core-provider-sources-volcengine_tts-unknown_error_fallback"
                        ),
                    )
                    raise Exception(
                        t(
                            "core-provider-sources-volcengine_tts-exception_api_error",
                            error_msg=error_msg,
                        )
                    )
                raise Exception(
                    t(
                        "core-provider-sources-volcengine_tts-api_request_failed",
                        response=response,
                        response_text=response_text,
                    ),
                )

        except Exception as e:
            error_details = traceback.format_exc()
            logger.debug(
                t(
                    "core-provider-sources-volcengine_tts-exception_details",
                    error_details=error_details,
                )
            )
            raise Exception(
                t("core-provider-sources-volcengine_tts-tts_exception", e=e)
            )
