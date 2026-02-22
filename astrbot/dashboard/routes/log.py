import asyncio
import json
import time
from collections.abc import AsyncGenerator
from typing import cast

from quart import Response as QuartResponse
from quart import make_response, request

from astrbot.core import LogBroker, logger
from astrbot.core.lang import t

from .route import Response, Route, RouteContext


def _format_log_sse(log: dict, ts: float) -> str:
    """辅助函数：格式化 SSE 消息"""
    payload = {
        "type": "log",
        **log,
    }
    return f"id: {ts}\ndata: {json.dumps(payload, ensure_ascii=False)}\n\n"


class LogRoute(Route):
    def __init__(self, context: RouteContext, log_broker: LogBroker) -> None:
        super().__init__(context)
        self.log_broker = log_broker
        self.app.add_url_rule("/api/live-log", view_func=self.log, methods=["GET"])
        self.app.add_url_rule(
            "/api/log-history",
            view_func=self.log_history,
            methods=["GET"],
        )
        self.app.add_url_rule(
            "/api/trace/settings",
            view_func=self.get_trace_settings,
            methods=["GET"],
        )
        self.app.add_url_rule(
            "/api/trace/settings",
            view_func=self.update_trace_settings,
            methods=["POST"],
        )

    async def _replay_cached_logs(
        self, last_event_id: str
    ) -> AsyncGenerator[str, None]:
        """辅助生成器：重放缓存的日志"""
        try:
            last_ts = float(last_event_id)
            cached_logs = list(self.log_broker.log_cache)

            for log_item in cached_logs:
                log_ts = float(log_item.get("time", 0))

                if log_ts > last_ts:
                    yield _format_log_sse(log_item, log_ts)

        except ValueError:
            pass
        except Exception as e:
            logger.error(t("dashboard-routes-log-error_sse_resend_history_failed", e=e))

    async def log(self) -> QuartResponse:
        last_event_id = request.headers.get("Last-Event-ID")

        async def stream():
            queue = None
            try:
                if last_event_id:
                    async for event in self._replay_cached_logs(last_event_id):
                        yield event

                queue = self.log_broker.register()
                while True:
                    message = await queue.get()
                    current_ts = message.get("time", time.time())
                    yield _format_log_sse(message, current_ts)

            except asyncio.CancelledError:
                pass
            except Exception as e:
                logger.error(t("dashboard-routes-log-error_sse_connection_failed", e=e))
            finally:
                if queue:
                    self.log_broker.unregister(queue)

        response = cast(
            QuartResponse,
            await make_response(
                stream(),
                {
                    "Content-Type": "text/event-stream",
                    "Cache-Control": "no-cache",
                    "Connection": "keep-alive",
                    "Transfer-Encoding": "chunked",
                },
            ),
        )
        response.timeout = None  # type: ignore
        return response

    async def log_history(self):
        """获取日志历史"""
        try:
            logs = list(self.log_broker.log_cache)
            return (
                Response()
                .ok(
                    data={
                        "logs": logs,
                    },
                )
                .__dict__
            )
        except Exception as e:
            logger.error(t("dashboard-routes-log-error_fetch_log_history_failed", e=e))
            return (
                Response()
                .error(t("dashboard-routes-log-response_error_fetch_log_history", e=e))
                .__dict__
            )

    async def get_trace_settings(self):
        """获取 Trace 设置"""
        try:
            trace_enable = self.config.get("trace_enable", True)
            return Response().ok(data={"trace_enable": trace_enable}).__dict__
        except Exception as e:
            logger.error(t("dashboard-routes-log-error_get_trace_settings_failed", e=e))
            return (
                Response()
                .error(t("dashboard-routes-log-response_error_get_trace_settings", e=e))
                .__dict__
            )

    async def update_trace_settings(self):
        """更新 Trace 设置"""
        try:
            data = await request.json
            if data is None:
                return (
                    Response()
                    .error(t("dashboard-routes-log-response_error_request_data_empty"))
                    .__dict__
                )

            trace_enable = data.get("trace_enable")
            if trace_enable is not None:
                self.config["trace_enable"] = bool(trace_enable)
                self.config.save_config()

            return (
                Response()
                .ok(
                    message=t("dashboard-routes-log-response_ok_trace_settings_updated")
                )
                .__dict__
            )
        except Exception as e:
            logger.error(
                t("dashboard-routes-log-error_update_trace_settings_failed", e=e)
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-log-response_error_update_trace_settings", e=e)
                )
                .__dict__
            )
