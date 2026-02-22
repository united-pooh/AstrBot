from quart import request

from astrbot.api import logger
from astrbot.core.lang import t
from astrbot.dashboard.routes.route import Response, Route, RouteContext


class LangRoute(Route):
    def __init__(self, context: RouteContext) -> None:
        super().__init__(context)
        self.routes = {
            "/setLang": ("POST", self.set_Lang),
        }
        self.register_routes()

    # TODO 删除日志
    async def set_Lang(self):
        data = await request.get_json()
        lang = data.get("lang")
        logger.debug(f"[LangRoute] lang:{lang}")
        if lang is None:
            return (
                Response()
                .error(t("dashboard-routes-lang_route-lang_required"))
                .__dict__
            )
        try:
            t.load_locale(locale=lang.lower(), files=None)
        except ValueError as exc:
            return Response().error(str(exc)).__dict__
        payload = {
            "lang": lang.lower(),
            "message": t("dashboard-routes-lang_route-language_set_success", lang=lang),
        }
        return Response().ok(payload).__dict__
