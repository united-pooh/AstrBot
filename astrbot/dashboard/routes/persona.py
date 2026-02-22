import traceback

from quart import request

from astrbot.core import logger
from astrbot.core.core_lifecycle import AstrBotCoreLifecycle
from astrbot.core.db import BaseDatabase
from astrbot.core.lang import t

from .route import Response, Route, RouteContext


class PersonaRoute(Route):
    def __init__(
        self,
        context: RouteContext,
        db_helper: BaseDatabase,
        core_lifecycle: AstrBotCoreLifecycle,
    ) -> None:
        super().__init__(context)
        self.routes = {
            "/persona/list": ("GET", self.list_personas),
            "/persona/detail": ("POST", self.get_persona_detail),
            "/persona/create": ("POST", self.create_persona),
            "/persona/update": ("POST", self.update_persona),
            "/persona/delete": ("POST", self.delete_persona),
            "/persona/move": ("POST", self.move_persona),
            "/persona/reorder": ("POST", self.reorder_items),
            # Folder routes
            "/persona/folder/list": ("GET", self.list_folders),
            "/persona/folder/tree": ("GET", self.get_folder_tree),
            "/persona/folder/detail": ("POST", self.get_folder_detail),
            "/persona/folder/create": ("POST", self.create_folder),
            "/persona/folder/update": ("POST", self.update_folder),
            "/persona/folder/delete": ("POST", self.delete_folder),
        }
        self.db_helper = db_helper
        self.persona_mgr = core_lifecycle.persona_mgr
        self.register_routes()

    async def list_personas(self):
        """获取所有人格列表"""
        try:
            # 支持按文件夹筛选
            folder_id = request.args.get("folder_id")
            if folder_id is not None:
                personas = await self.persona_mgr.get_personas_by_folder(
                    folder_id if folder_id else None
                )
            else:
                personas = await self.persona_mgr.get_all_personas()
            return (
                Response()
                .ok(
                    [
                        {
                            "persona_id": persona.persona_id,
                            "system_prompt": persona.system_prompt,
                            "begin_dialogs": persona.begin_dialogs or [],
                            "tools": persona.tools,
                            "skills": persona.skills,
                            "folder_id": persona.folder_id,
                            "sort_order": persona.sort_order,
                            "created_at": persona.created_at.isoformat()
                            if persona.created_at
                            else None,
                            "updated_at": persona.updated_at.isoformat()
                            if persona.updated_at
                            else None,
                        }
                        for persona in personas
                    ],
                )
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-get_persona_list_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(t("dashboard-routes-persona-error_fetch_persona_list", e=e))
                .__dict__
            )

    async def get_persona_detail(self):
        """获取指定人格的详细信息"""
        try:
            data = await request.get_json()
            persona_id = data.get("persona_id")

            if not persona_id:
                return (
                    Response()
                    .error(
                        t("dashboard-routes-persona-response_error_missing_persona_id")
                    )
                    .__dict__
                )

            persona = await self.persona_mgr.get_persona(persona_id)
            if not persona:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-persona_not_exists"))
                    .__dict__
                )

            return (
                Response()
                .ok(
                    {
                        "persona_id": persona.persona_id,
                        "system_prompt": persona.system_prompt,
                        "begin_dialogs": persona.begin_dialogs or [],
                        "tools": persona.tools,
                        "skills": persona.skills,
                        "folder_id": persona.folder_id,
                        "sort_order": persona.sort_order,
                        "created_at": persona.created_at.isoformat()
                        if persona.created_at
                        else None,
                        "updated_at": persona.updated_at.isoformat()
                        if persona.updated_at
                        else None,
                    },
                )
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-get_persona_detail_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t(
                        "dashboard-routes-persona-get_persona_details_failed_response",
                        e=e,
                    )
                )
                .__dict__
            )

    async def create_persona(self):
        """创建新人格"""
        try:
            data = await request.get_json()
            persona_id = data.get("persona_id", "").strip()
            system_prompt = data.get("system_prompt", "").strip()
            begin_dialogs = data.get("begin_dialogs", [])
            tools = data.get("tools")
            skills = data.get("skills")
            folder_id = data.get("folder_id")  # None 表示根目录
            sort_order = data.get("sort_order", 0)

            if not persona_id:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-persona_id_required"))
                    .__dict__
                )

            if not system_prompt:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-system_prompt_required"))
                    .__dict__
                )

            # 验证 begin_dialogs 格式
            if begin_dialogs and len(begin_dialogs) % 2 != 0:
                return (
                    Response()
                    .error(
                        t("dashboard-routes-persona-preset_conversations_must_be_even")
                    )
                    .__dict__
                )

            persona = await self.persona_mgr.create_persona(
                persona_id=persona_id,
                system_prompt=system_prompt,
                begin_dialogs=begin_dialogs if begin_dialogs else None,
                tools=tools if tools else None,
                skills=skills if skills else None,
                folder_id=folder_id,
                sort_order=sort_order,
            )

            return (
                Response()
                .ok(
                    {
                        "message": t("dashboard-routes-persona-persona_create_success"),
                        "persona": {
                            "persona_id": persona.persona_id,
                            "system_prompt": persona.system_prompt,
                            "begin_dialogs": persona.begin_dialogs or [],
                            "tools": persona.tools or [],
                            "skills": persona.skills or [],
                            "folder_id": persona.folder_id,
                            "sort_order": persona.sort_order,
                            "created_at": persona.created_at.isoformat()
                            if persona.created_at
                            else None,
                            "updated_at": persona.updated_at.isoformat()
                            if persona.updated_at
                            else None,
                        },
                    },
                )
                .__dict__
            )
        except ValueError as e:
            return Response().error(str(e)).__dict__
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-create_persona_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-persona-create_persona_failed_response", e=e)
                )
                .__dict__
            )

    async def update_persona(self):
        """更新人格信息"""
        try:
            data = await request.get_json()
            persona_id = data.get("persona_id")
            system_prompt = data.get("system_prompt")
            begin_dialogs = data.get("begin_dialogs")
            tools = data.get("tools")
            skills = data.get("skills")

            if not persona_id:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-missing_persona_id"))
                    .__dict__
                )

            # 验证 begin_dialogs 格式
            if begin_dialogs is not None and len(begin_dialogs) % 2 != 0:
                return (
                    Response()
                    .error(
                        t("dashboard-routes-persona-preset_conversations_even_required")
                    )
                    .__dict__
                )

            await self.persona_mgr.update_persona(
                persona_id=persona_id,
                system_prompt=system_prompt,
                begin_dialogs=begin_dialogs,
                tools=tools,
                skills=skills,
            )

            return (
                Response()
                .ok({"message": t("dashboard-routes-persona-persona_update_success")})
                .__dict__
            )
        except ValueError as e:
            return Response().error(str(e)).__dict__
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-update_persona_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-persona-update_persona_failed_response", e=e)
                )
                .__dict__
            )

    async def delete_persona(self):
        """删除人格"""
        try:
            data = await request.get_json()
            persona_id = data.get("persona_id")

            if not persona_id:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-update_missing_persona_id"))
                    .__dict__
                )

            await self.persona_mgr.delete_persona(persona_id)

            return (
                Response()
                .ok({"message": t("dashboard-routes-persona-persona_delete_success")})
                .__dict__
            )
        except ValueError as e:
            return Response().error(str(e)).__dict__
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-delete_persona_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-persona-delete_persona_failed_response", e=e)
                )
                .__dict__
            )

    async def move_persona(self):
        """移动人格到指定文件夹"""
        try:
            data = await request.get_json()
            persona_id = data.get("persona_id")
            folder_id = data.get("folder_id")  # None 表示移动到根目录

            if not persona_id:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-delete_missing_persona_id"))
                    .__dict__
                )

            await self.persona_mgr.move_persona_to_folder(persona_id, folder_id)

            return (
                Response()
                .ok({"message": t("dashboard-routes-persona-persona_move_success")})
                .__dict__
            )
        except ValueError as e:
            return Response().error(str(e)).__dict__
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-move_persona_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(t("dashboard-routes-persona-move_persona_failed_response", e=e))
                .__dict__
            )

    # ====
    # Folder Routes
    # ====

    async def list_folders(self):
        """获取文件夹列表"""
        try:
            parent_id = request.args.get("parent_id")
            # 空字符串视为 None（根目录）
            if parent_id == "":
                parent_id = None
            folders = await self.persona_mgr.get_folders(parent_id)
            return (
                Response()
                .ok(
                    [
                        {
                            "folder_id": folder.folder_id,
                            "name": folder.name,
                            "parent_id": folder.parent_id,
                            "description": folder.description,
                            "sort_order": folder.sort_order,
                            "created_at": folder.created_at.isoformat()
                            if folder.created_at
                            else None,
                            "updated_at": folder.updated_at.isoformat()
                            if folder.updated_at
                            else None,
                        }
                        for folder in folders
                    ],
                )
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-get_folder_list_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-persona-get_folder_list_failed_response", e=e)
                )
                .__dict__
            )

    async def get_folder_tree(self):
        """获取文件夹树形结构"""
        try:
            tree = await self.persona_mgr.get_folder_tree()
            return Response().ok(tree).__dict__
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-get_folder_tree_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-persona-get_folder_tree_failed_response", e=e)
                )
                .__dict__
            )

    async def get_folder_detail(self):
        """获取指定文件夹的详细信息"""
        try:
            data = await request.get_json()
            folder_id = data.get("folder_id")

            if not folder_id:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-missing_folder_id"))
                    .__dict__
                )

            folder = await self.persona_mgr.get_folder(folder_id)
            if not folder:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-folder_not_found"))
                    .__dict__
                )

            return (
                Response()
                .ok(
                    {
                        "folder_id": folder.folder_id,
                        "name": folder.name,
                        "parent_id": folder.parent_id,
                        "description": folder.description,
                        "sort_order": folder.sort_order,
                        "created_at": folder.created_at.isoformat()
                        if folder.created_at
                        else None,
                        "updated_at": folder.updated_at.isoformat()
                        if folder.updated_at
                        else None,
                    },
                )
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-get_folder_detail_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t(
                        "dashboard-routes-persona-get_folder_details_failed_response",
                        e=e,
                    )
                )
                .__dict__
            )

    async def create_folder(self):
        """创建文件夹"""
        try:
            data = await request.get_json()
            name = data.get("name", "").strip()
            parent_id = data.get("parent_id")
            description = data.get("description")
            sort_order = data.get("sort_order", 0)

            if not name:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-folder_name_required"))
                    .__dict__
                )

            folder = await self.persona_mgr.create_folder(
                name=name,
                parent_id=parent_id,
                description=description,
                sort_order=sort_order,
            )

            return (
                Response()
                .ok(
                    {
                        "message": t("dashboard-routes-persona-folder_create_success"),
                        "folder": {
                            "folder_id": folder.folder_id,
                            "name": folder.name,
                            "parent_id": folder.parent_id,
                            "description": folder.description,
                            "sort_order": folder.sort_order,
                            "created_at": folder.created_at.isoformat()
                            if folder.created_at
                            else None,
                            "updated_at": folder.updated_at.isoformat()
                            if folder.updated_at
                            else None,
                        },
                    },
                )
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-create_folder_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(t("dashboard-routes-persona-create_folder_failed_response", e=e))
                .__dict__
            )

    async def update_folder(self):
        """更新文件夹信息"""
        try:
            data = await request.get_json()
            folder_id = data.get("folder_id")
            name = data.get("name")
            parent_id = data.get("parent_id")
            description = data.get("description")
            sort_order = data.get("sort_order")

            if not folder_id:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-update_missing_folder_id"))
                    .__dict__
                )

            await self.persona_mgr.update_folder(
                folder_id=folder_id,
                name=name,
                parent_id=parent_id,
                description=description,
                sort_order=sort_order,
            )

            return (
                Response()
                .ok({"message": t("dashboard-routes-persona-folder_update_success")})
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-update_folder_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(t("dashboard-routes-persona-update_folder_failed_response", e=e))
                .__dict__
            )

    async def delete_folder(self):
        """删除文件夹"""
        try:
            data = await request.get_json()
            folder_id = data.get("folder_id")

            if not folder_id:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-delete_missing_folder_id"))
                    .__dict__
                )

            await self.persona_mgr.delete_folder(folder_id)

            return (
                Response()
                .ok({"message": t("dashboard-routes-persona-folder_delete_success")})
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-delete_folder_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-persona-failed_to_delete_folder_response", e=e)
                )
                .__dict__
            )

    async def reorder_items(self):
        """批量更新排序顺序

        请求体格式:
        {
            "items": [
                {"id": "persona_id_1", "type": "persona", "sort_order": 0},
                {"id": "persona_id_2", "type": "persona", "sort_order": 1},
                {"id": "folder_id_1", "type": "folder", "sort_order": 0},
                ...
            ]
        }
        """
        try:
            data = await request.get_json()
            items = data.get("items", [])

            if not items:
                return (
                    Response()
                    .error(t("dashboard-routes-persona-items_cannot_be_empty"))
                    .__dict__
                )

            # 验证每个 item 的格式
            for item in items:
                if not all(k in item for k in ("id", "type", "sort_order")):
                    return (
                        Response()
                        .error(
                            t(
                                "dashboard-routes-persona-each_item_missing_required_fields"
                            )
                        )
                        .__dict__
                    )
                if item["type"] not in ("persona", "folder"):
                    return (
                        Response()
                        .error(t("dashboard-routes-persona-invalid_item_type"))
                        .__dict__
                    )

            await self.persona_mgr.batch_update_sort_order(items)

            return (
                Response()
                .ok({"message": t("dashboard-routes-persona-sort_update_success")})
                .__dict__
            )
        except Exception as e:
            logger.error(
                t(
                    "dashboard-routes-persona-update_sorting_failed",
                    e=e,
                    format_exc=traceback.format_exc(),
                )
            )
            return (
                Response()
                .error(
                    t("dashboard-routes-persona-failed_to_update_sorting_response", e=e)
                )
                .__dict__
            )
