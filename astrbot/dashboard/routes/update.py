import traceback

from quart import request

from astrbot.core import DEMO_MODE, logger, pip_installer
from astrbot.core.config.default import VERSION
from astrbot.core.core_lifecycle import AstrBotCoreLifecycle
from astrbot.core.db.migration.helper import check_migration_needed_v4, do_migration_v4
from astrbot.core.lang import t
from astrbot.core.updator import AstrBotUpdator
from astrbot.core.utils.io import download_dashboard, get_dashboard_version

from .route import Response, Route, RouteContext

CLEAR_SITE_DATA_HEADERS = {"Clear-Site-Data": '"cache"'}


class UpdateRoute(Route):
    def __init__(
        self,
        context: RouteContext,
        astrbot_updator: AstrBotUpdator,
        core_lifecycle: AstrBotCoreLifecycle,
    ) -> None:
        super().__init__(context)
        self.routes = {
            "/update/check": ("GET", self.check_update),
            "/update/releases": ("GET", self.get_releases),
            "/update/do": ("POST", self.update_project),
            "/update/dashboard": ("POST", self.update_dashboard),
            "/update/pip-install": ("POST", self.install_pip_package),
            "/update/migration": ("POST", self.do_migration),
        }
        self.astrbot_updator = astrbot_updator
        self.core_lifecycle = core_lifecycle
        self.register_routes()

    async def do_migration(self):
        need_migration = await check_migration_needed_v4(self.core_lifecycle.db)
        if not need_migration:
            return (
                Response()
                .ok(None, t("dashboard-routes-update-no_migration_needed"))
                .__dict__
            )
        try:
            data = await request.json
            pim = data.get("platform_id_map", {})
            await do_migration_v4(
                self.core_lifecycle.db,
                pim,
                self.core_lifecycle.astrbot_config,
            )
            return (
                Response()
                .ok(None, t("dashboard-routes-update-migration_successful"))
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-update-migration_failed",
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(t("dashboard-routes-update-migration_failed_response", e=e))
                .__dict__
            )

    async def check_update(self):
        type_ = request.args.get("type", None)

        try:
            dv = await get_dashboard_version()
            if type_ == "dashboard":
                return (
                    Response()
                    .ok({"has_new_version": dv != f"v{VERSION}", "current_version": dv})
                    .__dict__
                )
            ret = await self.astrbot_updator.check_update(None, None, False)
            return Response(
                status="success",
                message=str(ret)
                if ret is not None
                else t("dashboard-routes-update-already_latest_version"),
                data={
                    "version": f"v{VERSION}",
                    "has_new_version": ret is not None,
                    "dashboard_version": dv,
                    "dashboard_has_new_version": bool(dv and dv != f"v{VERSION}"),
                },
            ).__dict__
        except Exception as e:
            logger.warning(
                t("dashboard-routes-update-check_update_failed_warning", e=e)
            )
            return Response().error(e.__str__()).__dict__

    async def get_releases(self):
        try:
            ret = await self.astrbot_updator.get_releases()
            return Response().ok(ret).__dict__
        except Exception as e:
            logger.error(f"/api/update/releases: {traceback.format_exc()}")
            return Response().error(e.__str__()).__dict__

    async def update_project(self):
        data = await request.json
        version = data.get("version", "")
        reboot = data.get("reboot", True)
        if version == "" or version == "latest":
            latest = True
            version = ""
        else:
            latest = False

        proxy: str = data.get("proxy", None)
        if proxy:
            proxy = proxy.removesuffix("/")

        try:
            await self.astrbot_updator.update(
                latest=latest,
                version=version,
                proxy=proxy,
            )

            try:
                await download_dashboard(latest=latest, version=version, proxy=proxy)
            except Exception as e:
                logger.error(
                    t("dashboard-routes-update-download_panel_files_failed", e=e)
                )

            # pip 更新依赖
            logger.info(t("dashboard-routes-update-updating_dependencies"))
            try:
                await pip_installer.install(requirements_path="requirements.txt")
            except Exception as e:
                logger.error(
                    t("dashboard-routes-update-update_dependencies_failed", e=e)
                )

            if reboot:
                await self.core_lifecycle.restart()
                ret = (
                    Response()
                    .ok(None, t("dashboard-routes-update-success_restart_in_2s"))
                    .__dict__
                )
                return ret, 200, CLEAR_SITE_DATA_HEADERS
            ret = (
                Response()
                .ok(None, t("dashboard-routes-update-success_apply_on_next_start"))
                .__dict__
            )
            return ret, 200, CLEAR_SITE_DATA_HEADERS
        except Exception as e:
            logger.error(f"/api/update_project: {traceback.format_exc()}")
            return Response().error(e.__str__()).__dict__

    async def update_dashboard(self):
        try:
            try:
                await download_dashboard(version=f"v{VERSION}", latest=False)
            except Exception as e:
                logger.error(
                    t("dashboard-routes-update-download_panel_files_failed_alt", e=e)
                )
                return (
                    Response()
                    .error(
                        t("dashboard-routes-update-response_download_panel_failed", e=e)
                    )
                    .__dict__
                )
            ret = (
                Response()
                .ok(None, t("dashboard-routes-update-success_refresh_to_apply"))
                .__dict__
            )
            return ret, 200, CLEAR_SITE_DATA_HEADERS
        except Exception as e:
            logger.error(f"/api/update_dashboard: {traceback.format_exc()}")
            return Response().error(e.__str__()).__dict__

    async def install_pip_package(self):
        if DEMO_MODE:
            return (
                Response()
                .error("You are not permitted to do this operation in demo mode")
                .__dict__
            )

        data = await request.json
        package = data.get("package", "")
        mirror = data.get("mirror", None)
        if not package:
            return (
                Response()
                .error(t("dashboard-routes-update-missing_or_invalid_package"))
                .__dict__
            )
        try:
            await pip_installer.install(package, mirror=mirror)
            return (
                Response()
                .ok(None, t("dashboard-routes-update-installation_successful"))
                .__dict__
            )
        except Exception as e:
            logger.error(f"/api/update_pip: {traceback.format_exc()}")
            return Response().error(e.__str__()).__dict__
