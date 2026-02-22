import asyncio
import json
import os
import time
import uuid
import wave
from typing import Any

import jwt
from quart import websocket

from astrbot import logger
from astrbot.core.core_lifecycle import AstrBotCoreLifecycle
from astrbot.core.lang import t
from astrbot.core.platform.sources.webchat.webchat_queue_mgr import webchat_queue_mgr
from astrbot.core.utils.astrbot_path import get_astrbot_temp_path

from .route import Route, RouteContext


class LiveChatSession:
    """Live Chat 会话管理器"""

    def __init__(self, session_id: str, username: str) -> None:
        self.session_id = session_id
        self.username = username
        self.conversation_id = str(uuid.uuid4())
        self.is_speaking = False
        self.is_processing = False
        self.should_interrupt = False
        self.audio_frames: list[bytes] = []
        self.current_stamp: str | None = None
        self.temp_audio_path: str | None = None

    def start_speaking(self, stamp: str) -> None:
        """开始说话"""
        self.is_speaking = True
        self.current_stamp = stamp
        self.audio_frames = []
        logger.debug(
            t(
                "dashboard-routes-live_chat-debug_user_starts_speaking",
                self=self,
                stamp=stamp,
            )
        )

    def add_audio_frame(self, data: bytes) -> None:
        """添加音频帧"""
        if self.is_speaking:
            self.audio_frames.append(data)

    async def end_speaking(self, stamp: str) -> tuple[str | None, float]:
        """结束说话，返回组装的 WAV 文件路径和耗时"""
        start_time = time.time()
        if not self.is_speaking or stamp != self.current_stamp:
            logger.warning(
                t(
                    "dashboard-routes-live_chat-debug_stamp_mismatch_or_not_speaking",
                    stamp=stamp,
                    self=self,
                )
            )
            return None, 0.0

        self.is_speaking = False

        if not self.audio_frames:
            logger.warning(t("dashboard-routes-live_chat-no_audio_frame_data"))
            return None, 0.0

        # 组装 WAV 文件
        try:
            temp_dir = get_astrbot_temp_path()
            os.makedirs(temp_dir, exist_ok=True)
            audio_path = os.path.join(temp_dir, f"live_audio_{uuid.uuid4()}.wav")

            # 假设前端发送的是 PCM 数据，采样率 16000Hz，单声道，16位
            with wave.open(audio_path, "wb") as wav_file:
                wav_file.setnchannels(1)  # 单声道
                wav_file.setsampwidth(2)  # 16位 = 2字节
                wav_file.setframerate(16000)  # 采样率 16000Hz
                for frame in self.audio_frames:
                    wav_file.writeframes(frame)

            self.temp_audio_path = audio_path
            logger.info(
                t(
                    "dashboard-routes-live_chat-audio_file_saved",
                    audio_path=audio_path,
                    audio_path_2=os.path.getsize(audio_path),
                )
            )
            return audio_path, time.time() - start_time

        except Exception as e:
            logger.error(
                t("dashboard-routes-live_chat-failed_to_assemble_wav", e=e),
                exc_info=True,
            )
            return None, 0.0

    def cleanup(self) -> None:
        """清理临时文件"""
        if self.temp_audio_path and os.path.exists(self.temp_audio_path):
            try:
                os.remove(self.temp_audio_path)
                logger.debug(
                    t("dashboard-routes-live_chat-debug_temp_file_deleted", self=self)
                )
            except Exception as e:
                logger.warning(
                    t("dashboard-routes-live_chat-delete_temp_file_failed", e=e)
                )
        self.temp_audio_path = None


class LiveChatRoute(Route):
    """Live Chat WebSocket 路由"""

    def __init__(
        self,
        context: RouteContext,
        db: Any,
        core_lifecycle: AstrBotCoreLifecycle,
    ) -> None:
        super().__init__(context)
        self.core_lifecycle = core_lifecycle
        self.db = db
        self.plugin_manager = core_lifecycle.plugin_manager
        self.sessions: dict[str, LiveChatSession] = {}

        # 注册 WebSocket 路由
        self.app.websocket("/api/live_chat/ws")(self.live_chat_ws)

    async def live_chat_ws(self) -> None:
        """Live Chat WebSocket 处理器"""
        # WebSocket 不能通过 header 传递 token，需要从 query 参数获取
        # 注意：WebSocket 上下文使用 websocket.args 而不是 request.args
        token = websocket.args.get("token")
        if not token:
            await websocket.close(1008, "Missing authentication token")
            return

        try:
            jwt_secret = self.config["dashboard"].get("jwt_secret")
            payload = jwt.decode(token, jwt_secret, algorithms=["HS256"])
            username = payload["username"]
        except jwt.ExpiredSignatureError:
            await websocket.close(1008, "Token expired")
            return
        except jwt.InvalidTokenError:
            await websocket.close(1008, "Invalid token")
            return

        session_id = f"webchat_live!{username}!{uuid.uuid4()}"
        live_session = LiveChatSession(session_id, username)
        self.sessions[session_id] = live_session

        logger.info(
            t("dashboard-routes-live_chat-websocket_connected", username=username)
        )

        try:
            while True:
                message = await websocket.receive_json()
                await self._handle_message(live_session, message)

        except Exception as e:
            logger.error(
                t("dashboard-routes-live_chat-websocket_error", e=e), exc_info=True
            )

        finally:
            # 清理会话
            if session_id in self.sessions:
                live_session.cleanup()
                del self.sessions[session_id]
            logger.info(
                t("dashboard-routes-live_chat-websocket_closed", username=username)
            )

    async def _handle_message(self, session: LiveChatSession, message: dict) -> None:
        """处理 WebSocket 消息"""
        msg_type = message.get("t")  # 使用 t 代替 type

        if msg_type == "start_speaking":
            # 开始说话
            stamp = message.get("stamp")
            if not stamp:
                logger.warning(
                    t("dashboard-routes-live_chat-start_speaking_missing_stamp")
                )
                return
            session.start_speaking(stamp)

        elif msg_type == "speaking_part":
            # 音频片段
            audio_data_b64 = message.get("data")
            if not audio_data_b64:
                return

            # 解码 base64
            import base64

            try:
                audio_data = base64.b64decode(audio_data_b64)
                session.add_audio_frame(audio_data)
            except Exception as e:
                logger.error(t("dashboard-routes-live_chat-decode_audio_failed", e=e))

        elif msg_type == "end_speaking":
            # 结束说话
            stamp = message.get("stamp")
            if not stamp:
                logger.warning(
                    t("dashboard-routes-live_chat-end_speaking_missing_stamp")
                )
                return

            audio_path, assemble_duration = await session.end_speaking(stamp)
            if not audio_path:
                await websocket.send_json(
                    {
                        "t": "error",
                        "data": t("dashboard-routes-live_chat-audio_assembly_failed"),
                    }
                )
                return

            # 处理音频：STT -> LLM -> TTS
            await self._process_audio(session, audio_path, assemble_duration)

        elif msg_type == "interrupt":
            # 用户打断
            session.should_interrupt = True
            logger.info(
                t("dashboard-routes-live_chat-info_user_interrupted", session=session)
            )

    async def _process_audio(
        self, session: LiveChatSession, audio_path: str, assemble_duration: float
    ) -> None:
        """处理音频：STT -> LLM -> 流式 TTS"""
        try:
            # 发送 WAV 组装耗时
            await websocket.send_json(
                {"t": "metrics", "data": {"wav_assemble_time": assemble_duration}}
            )
            wav_assembly_finish_time = time.time()

            session.is_processing = True
            session.should_interrupt = False

            # 1. STT - 语音转文字
            ctx = self.plugin_manager.context
            stt_provider = ctx.provider_manager.stt_provider_insts[0]

            if not stt_provider:
                logger.error(
                    t("dashboard-routes-live_chat-stt_provider_not_configured")
                )
                await websocket.send_json(
                    {
                        "t": "error",
                        "data": t(
                            "dashboard-routes-live_chat-stt_service_not_configured"
                        ),
                    }
                )
                return

            await websocket.send_json(
                {"t": "metrics", "data": {"stt": stt_provider.meta().type}}
            )

            user_text = await stt_provider.get_text(audio_path)
            if not user_text:
                logger.warning(t("dashboard-routes-live_chat-stt_result_empty"))
                return

            logger.info(
                t("dashboard-routes-live_chat-stt_result_received", user_text=user_text)
            )

            await websocket.send_json(
                {
                    "t": "user_msg",
                    "data": {"text": user_text, "ts": int(time.time() * 1000)},
                }
            )

            # 2. 构造消息事件并发送到 pipeline
            # 使用 webchat queue 机制
            cid = session.conversation_id
            queue = webchat_queue_mgr.get_or_create_queue(cid)

            message_id = str(uuid.uuid4())
            payload = {
                "message_id": message_id,
                "message": [{"type": "plain", "text": user_text}],  # 直接发送文本
                "action_type": "live",  # 标记为 live mode
            }

            # 将消息放入队列
            await queue.put((session.username, cid, payload))

            # 3. 等待响应并流式发送 TTS 音频
            back_queue = webchat_queue_mgr.get_or_create_back_queue(message_id, cid)

            bot_text = ""
            audio_playing = False

            try:
                while True:
                    if session.should_interrupt:
                        # 用户打断，停止处理
                        logger.info(
                            t("dashboard-routes-live_chat-user_interruption_detected")
                        )
                        await websocket.send_json({"t": "stop_play"})
                        # 保存消息并标记为被打断
                        await self._save_interrupted_message(
                            session, user_text, bot_text
                        )
                        # 清空队列中未处理的消息
                        while not back_queue.empty():
                            try:
                                back_queue.get_nowait()
                            except asyncio.QueueEmpty:
                                break
                        break

                    try:
                        result = await asyncio.wait_for(back_queue.get(), timeout=0.5)
                    except asyncio.TimeoutError:
                        continue

                    if not result:
                        continue

                    result_message_id = result.get("message_id")
                    if result_message_id != message_id:
                        logger.warning(
                            t(
                                "dashboard-routes-live_chat-message_id_mismatch",
                                result_message_id=result_message_id,
                                message_id=message_id,
                            )
                        )
                        continue

                    result_type = result.get("type")
                    result_chain_type = result.get("chain_type")
                    data = result.get("data", "")

                    if result_chain_type == "agent_stats":
                        try:
                            stats = json.loads(data)
                            await websocket.send_json(
                                {
                                    "t": "metrics",
                                    "data": {
                                        "llm_ttft": stats.get("time_to_first_token", 0),
                                        "llm_total_time": stats.get("end_time", 0)
                                        - stats.get("start_time", 0),
                                    },
                                }
                            )
                        except Exception as e:
                            logger.error(
                                t(
                                    "dashboard-routes-live_chat-parse_agentstats_failed",
                                    e=e,
                                )
                            )
                        continue

                    if result_chain_type == "tts_stats":
                        try:
                            stats = json.loads(data)
                            await websocket.send_json(
                                {
                                    "t": "metrics",
                                    "data": stats,
                                }
                            )
                        except Exception as e:
                            logger.error(
                                t(
                                    "dashboard-routes-live_chat-parse_ttsstats_failed",
                                    e=e,
                                )
                            )
                        continue

                    if result_type == "plain":
                        # 普通文本消息
                        bot_text += data

                    elif result_type == "audio_chunk":
                        # 流式音频数据
                        if not audio_playing:
                            audio_playing = True
                            logger.debug(
                                t(
                                    "dashboard-routes-live_chat-start_playing_audio_stream"
                                )
                            )

                            # Calculate latency from wav assembly finish to first audio chunk
                            speak_to_first_frame_latency = (
                                time.time() - wav_assembly_finish_time
                            )
                            await websocket.send_json(
                                {
                                    "t": "metrics",
                                    "data": {
                                        "speak_to_first_frame": speak_to_first_frame_latency
                                    },
                                }
                            )

                        text = result.get("text")
                        if text:
                            await websocket.send_json(
                                {
                                    "t": "bot_text_chunk",
                                    "data": {"text": text},
                                }
                            )

                        # 发送音频数据给前端
                        await websocket.send_json(
                            {
                                "t": "response",
                                "data": data,  # base64 编码的音频数据
                            }
                        )

                    elif result_type in ["complete", "end"]:
                        # 处理完成
                        logger.info(
                            t(
                                "dashboard-routes-live_chat-bot_reply_completed",
                                bot_text=bot_text,
                            )
                        )

                        # 如果没有音频流，发送 bot 消息文本
                        if not audio_playing:
                            await websocket.send_json(
                                {
                                    "t": "bot_msg",
                                    "data": {
                                        "text": bot_text,
                                        "ts": int(time.time() * 1000),
                                    },
                                }
                            )

                        # 发送结束标记
                        await websocket.send_json({"t": "end"})

                        # 发送总耗时
                        wav_to_tts_duration = time.time() - wav_assembly_finish_time
                        await websocket.send_json(
                            {
                                "t": "metrics",
                                "data": {"wav_to_tts_total_time": wav_to_tts_duration},
                            }
                        )
                        break
            finally:
                webchat_queue_mgr.remove_back_queue(message_id)

        except Exception as e:
            logger.error(
                t("dashboard-routes-live_chat-error_process_audio_failed", e=e),
                exc_info=True,
            )
            await websocket.send_json(
                {
                    "t": "error",
                    "data": t(
                        "dashboard-routes-live_chat-websocket_error_processing_failed",
                        e=e,
                    ),
                }
            )

        finally:
            session.is_processing = False
            session.should_interrupt = False

    async def _save_interrupted_message(
        self, session: LiveChatSession, user_text: str, bot_text: str
    ) -> None:
        """保存被打断的消息"""
        interrupted_text = bot_text + t(
            "dashboard-routes-live_chat-interrupted_by_user_suffix"
        )
        logger.info(
            t(
                "dashboard-routes-live_chat-info_saved_interrupted_message",
                interrupted_text=interrupted_text,
            )
        )

        # 简单记录到日志，实际保存逻辑可以后续完善
        try:
            timestamp = int(time.time() * 1000)
            logger.info(
                t(
                    "dashboard-routes-live_chat-debug_user_message",
                    user_text=user_text,
                    session=session,
                    timestamp=timestamp,
                )
            )
            if bot_text:
                logger.info(
                    t(
                        "dashboard-routes-live_chat-debug_bot_message_interrupted",
                        interrupted_text=interrupted_text,
                        session=session,
                        timestamp=timestamp,
                    )
                )
        except Exception as e:
            logger.error(
                t("dashboard-routes-live_chat-error_log_message_failed", e=e),
                exc_info=True,
            )
