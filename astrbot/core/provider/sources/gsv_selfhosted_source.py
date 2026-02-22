import asyncio
import os
import uuid

import aiohttp

from astrbot import logger
from astrbot.core.lang import t
from astrbot.core.utils.astrbot_path import get_astrbot_temp_path

from ..entities import ProviderType
from ..provider import TTSProvider
from ..register import register_provider_adapter


@register_provider_adapter(
    provider_type_name="gsv_tts_selfhost",
    desc=t("core-provider-sources-gsv_selfhosted_source-display_name"),
    provider_type=ProviderType.TEXT_TO_SPEECH,
)
class ProviderGSVTTS(TTSProvider):
    def __init__(
        self,
        provider_config: dict,
        provider_settings: dict,
    ) -> None:
        super().__init__(provider_config, provider_settings)

        self.api_base = provider_config.get("api_base", "http://127.0.0.1:9880").rstrip(
            "/",
        )
        self.gpt_weights_path: str = provider_config.get("gpt_weights_path", "")
        self.sovits_weights_path: str = provider_config.get("sovits_weights_path", "")

        # TTS 请求的默认参数，移除前缀gsv_
        self.default_params: dict = {
            key.removeprefix("gsv_"): str(value).lower()
            for key, value in provider_config.get("gsv_default_parms", {}).items()
        }
        self.timeout = provider_config.get("timeout", 60)
        self._session: aiohttp.ClientSession | None = None

    async def initialize(self) -> None:
        """异步初始化：在 ProviderManager 中被调用"""
        self._session = aiohttp.ClientSession(
            timeout=aiohttp.ClientTimeout(total=self.timeout),
        )
        try:
            await self._set_model_weights()
            logger.info(
                t(
                    "core-provider-sources-gsv_selfhosted_source-initialization_completed"
                )
            )
        except Exception as e:
            logger.error(
                t(
                    "core-provider-sources-gsv_selfhosted_source-initialization_failed",
                    e=e,
                )
            )
            raise

    def get_session(self) -> aiohttp.ClientSession:
        if not self._session or self._session.closed:
            raise RuntimeError(
                "[GSV TTS] Provider HTTP session is not ready or closed.",
            )
        return self._session

    async def _make_request(
        self,
        endpoint: str,
        params=None,
        retries: int = 3,
    ) -> bytes | None:
        """发起请求"""
        for attempt in range(retries):
            logger.debug(
                t(
                    "core-provider-sources-gsv_selfhosted_source-request_details",
                    endpoint=endpoint,
                    params=params,
                )
            )
            try:
                async with self.get_session().get(endpoint, params=params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        raise Exception(
                            f"[GSV TTS] Request to {endpoint} failed with status {response.status}: {error_text}",
                        )
                    return await response.read()
            except Exception as e:
                if attempt < retries - 1:
                    logger.warning(
                        t(
                            "core-provider-sources-gsv_selfhosted_source-request_failed_retry",
                            endpoint=endpoint,
                            attempt=attempt + 1,
                            e=e,
                        ),
                    )
                    await asyncio.sleep(1)
                else:
                    logger.error(
                        t(
                            "core-provider-sources-gsv_selfhosted_source-request_final_failure",
                            endpoint=endpoint,
                            e=e,
                        )
                    )
                    raise

    async def _set_model_weights(self) -> None:
        """设置模型路径"""
        try:
            if self.gpt_weights_path:
                await self._make_request(
                    f"{self.api_base}/set_gpt_weights",
                    {"weights_path": self.gpt_weights_path},
                )
                logger.info(
                    t(
                        "core-provider-sources-gsv_selfhosted_source-gpt_model_path_set",
                        self=self,
                    )
                )
            else:
                logger.info(
                    t(
                        "core-provider-sources-gsv_selfhosted_source-using_builtin_gpt_model"
                    )
                )

            if self.sovits_weights_path:
                await self._make_request(
                    f"{self.api_base}/set_sovits_weights",
                    {"weights_path": self.sovits_weights_path},
                )
                logger.info(
                    t(
                        "core-provider-sources-gsv_selfhosted_source-sovits_model_path_set",
                        self=self,
                    ),
                )
            else:
                logger.info(
                    t(
                        "core-provider-sources-gsv_selfhosted_source-using_builtin_sovits_model"
                    )
                )
        except aiohttp.ClientError as e:
            logger.error(
                t(
                    "core-provider-sources-gsv_selfhosted_source-model_path_network_error",
                    e=e,
                )
            )
        except Exception as e:
            logger.error(
                t(
                    "core-provider-sources-gsv_selfhosted_source-model_path_unknown_error",
                    e=e,
                )
            )

    async def get_audio(self, text: str) -> str:
        """实现 TTS 核心方法，根据文本内容自动切换情绪"""
        if not text.strip():
            raise ValueError(
                t("core-provider-sources-gsv_selfhosted_source-text_cannot_be_empty")
            )

        endpoint = f"{self.api_base}/tts"

        params = self.build_synthesis_params(text)

        temp_dir = get_astrbot_temp_path()
        os.makedirs(temp_dir, exist_ok=True)
        path = os.path.join(temp_dir, f"gsv_tts_{uuid.uuid4().hex}.wav")

        logger.debug(
            t(
                "core-provider-sources-gsv_selfhosted_source-calling_synthesis_api",
                params=params,
            )
        )

        result = await self._make_request(endpoint, params)
        if isinstance(result, bytes):
            with open(path, "wb") as f:
                f.write(result)
            return path
        raise Exception(
            t(
                "core-provider-sources-gsv_selfhosted_source-synthesis_failed",
                text=text,
                result=result,
            )
        )

    def build_synthesis_params(self, text: str) -> dict:
        """构建语音合成所需的参数字典。

        当前仅包含默认参数 + 文本，未来可在此基础上动态添加如情绪、角色等语义控制字段。
        """
        params = self.default_params.copy()
        params["text"] = text
        # TODO: 在此处添加情绪分析，例如 params["emotion"] = detect_emotion(text)
        return params

    async def terminate(self) -> None:
        """终止释放资源：在 ProviderManager 中被调用"""
        if self._session and not self._session.closed:
            await self._session.close()
            logger.info(t("core-provider-sources-gsv_selfhosted_source-session_closed"))
