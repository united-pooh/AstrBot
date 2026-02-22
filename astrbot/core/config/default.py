"""如需修改配置，请在 `data/cmd_config.json` 中修改或者在管理面板中可视化修改。"""

import os
from typing import Any, TypedDict

from astrbot.core.lang import t
from astrbot.core.utils.astrbot_path import get_astrbot_data_path

VERSION = "4.18.0"
DB_PATH = os.path.join(get_astrbot_data_path(), "data_v4.db")

WEBHOOK_SUPPORTED_PLATFORMS = [
    "qq_official_webhook",
    "weixin_official_account",
    "wecom",
    "wecom_ai_bot",
    "slack",
    "lark",
    "line",
]

# 默认配置
DEFAULT_CONFIG = {
    "config_version": 2,
    "platform_settings": {
        "unique_session": False,
        "rate_limit": {
            "time": 60,
            "count": 30,
            "strategy": "stall",  # stall, discard
        },
        "reply_prefix": "",
        "forward_threshold": 1500,
        "enable_id_white_list": True,
        "id_whitelist": [],
        "id_whitelist_log": True,
        "wl_ignore_admin_on_group": True,
        "wl_ignore_admin_on_friend": True,
        "reply_with_mention": False,
        "reply_with_quote": False,
        "path_mapping": [],
        "segmented_reply": {
            "enable": False,
            "only_llm_result": True,
            "interval_method": "random",
            "interval": "1.5,3.5",
            "log_base": 2.6,
            "words_count_threshold": 150,
            "split_mode": "regex",  # regex 或 words
            "regex": ".*?[。？！~…]+|.+$",
            "split_words": [
                "。",
                "？",
                "！",
                "~",
                "…",
            ],  # 当 split_mode 为 words 时使用
            "content_cleanup_rule": "",
        },
        "no_permission_reply": True,
        "empty_mention_waiting": True,
        "empty_mention_waiting_need_reply": True,
        "friend_message_needs_wake_prefix": False,
        "ignore_bot_self_message": False,
        "ignore_at_all": False,
    },
    "provider_sources": [],  # provider sources
    "provider": [],  # models from provider_sources
    "provider_settings": {
        "enable": True,
        "default_provider_id": "",
        "fallback_chat_models": [],
        "default_image_caption_provider_id": "",
        "image_caption_prompt": "Please describe the image using Chinese.",
        "provider_pool": ["*"],  # "*" 表示使用所有可用的提供者
        "wake_prefix": "",
        "web_search": False,
        "websearch_provider": "default",
        "websearch_tavily_key": [],
        "websearch_bocha_key": [],
        "websearch_baidu_app_builder_key": "",
        "web_search_link": False,
        "display_reasoning_text": False,
        "identifier": False,
        "group_name_display": False,
        "datetime_system_prompt": True,
        "default_personality": "default",
        "persona_pool": ["*"],
        "prompt_prefix": "{{prompt}}",
        "context_limit_reached_strategy": "truncate_by_turns",  # or llm_compress
        "llm_compress_instruction": (
            "Based on our full conversation history, produce a concise summary of key takeaways and/or project progress.\n"
            "1. Systematically cover all core topics discussed and the final conclusion/outcome for each; clearly highlight the latest primary focus.\n"
            "2. If any tools were used, summarize tool usage (total call count) and extract the most valuable insights from tool outputs.\n"
            "3. If there was an initial user goal, state it first and describe the current progress/status.\n"
            "4. Write the summary in the user's language.\n"
        ),
        "llm_compress_keep_recent": 6,
        "llm_compress_provider_id": "",
        "max_context_length": -1,
        "dequeue_context_length": 1,
        "streaming_response": False,
        "show_tool_use_status": False,
        "sanitize_context_by_modalities": False,
        "max_quoted_fallback_images": 20,
        "quoted_message_parser": {
            "max_component_chain_depth": 4,
            "max_forward_node_depth": 6,
            "max_forward_fetch": 32,
            "warn_on_action_failure": False,
        },
        "agent_runner_type": "local",
        "dify_agent_runner_provider_id": "",
        "coze_agent_runner_provider_id": "",
        "dashscope_agent_runner_provider_id": "",
        "unsupported_streaming_strategy": "realtime_segmenting",
        "reachability_check": False,
        "max_agent_step": 30,
        "tool_call_timeout": 60,
        "tool_schema_mode": "full",
        "llm_safety_mode": True,
        "safety_mode_strategy": "system_prompt",  # TODO: llm judge
        "file_extract": {
            "enable": False,
            "provider": "moonshotai",
            "moonshotai_api_key": "",
        },
        "proactive_capability": {
            "add_cron_tools": True,
        },
        "computer_use_runtime": "local",
        "computer_use_require_admin": True,
        "sandbox": {
            "booter": "shipyard",
            "shipyard_endpoint": "",
            "shipyard_access_token": "",
            "shipyard_ttl": 3600,
            "shipyard_max_sessions": 10,
        },
    },
    # SubAgent orchestrator mode:
    # - main_enable = False: disabled; main LLM mounts tools normally (persona selection).
    # - main_enable = True: enabled; main LLM keeps its own tools and includes handoff
    #   tools (transfer_to_*). remove_main_duplicate_tools can remove tools that are
    #   duplicated on subagents from the main LLM toolset.
    "subagent_orchestrator": {
        "main_enable": False,
        "remove_main_duplicate_tools": False,
        "router_system_prompt": (
            "You are a task router. Your job is to chat naturally, recognize user intent, "
            "and delegate work to the most suitable subagent using transfer_to_* tools. "
            "Do not try to use domain tools yourself. If no subagent fits, respond directly."
        ),
        "agents": [],
    },
    "provider_stt_settings": {
        "enable": False,
        "provider_id": "",
    },
    "provider_tts_settings": {
        "enable": False,
        "provider_id": "",
        "dual_output": False,
        "use_file_service": False,
        "trigger_probability": 1.0,
    },
    "provider_ltm_settings": {
        "group_icl_enable": False,
        "group_message_max_cnt": 300,
        "image_caption": False,
        "image_caption_provider_id": "",
        "active_reply": {
            "enable": False,
            "method": "possibility_reply",
            "possibility_reply": 0.1,
            "whitelist": [],
        },
    },
    "content_safety": {
        "also_use_in_response": False,
        "internal_keywords": {"enable": True, "extra_keywords": []},
        "baidu_aip": {"enable": False, "app_id": "", "api_key": "", "secret_key": ""},
    },
    "admins_id": ["astrbot"],
    "t2i": False,
    "t2i_word_threshold": 150,
    "t2i_strategy": "remote",
    "t2i_endpoint": "",
    "t2i_use_file_service": False,
    "t2i_active_template": "base",
    "http_proxy": "",
    "no_proxy": ["localhost", "127.0.0.1", "::1", "10.*", "192.168.*"],
    "dashboard": {
        "enable": True,
        "username": "astrbot",
        "password": "77b90590a8945a7d36c963981a307dc9",
        "jwt_secret": "",
        "host": "0.0.0.0",
        "port": 6185,
        "disable_access_log": True,
        "ssl": {
            "enable": False,
            "cert_file": "",
            "key_file": "",
            "ca_certs": "",
        },
    },
    "platform": [],
    "platform_specific": {
        # 平台特异配置：按平台分类，平台下按功能分组
        "lark": {
            "pre_ack_emoji": {"enable": False, "emojis": ["Typing"]},
        },
        "telegram": {
            "pre_ack_emoji": {"enable": False, "emojis": ["✍️"]},
        },
    },
    "wake_prefix": ["/"],
    "log_level": "INFO",
    "log_file_enable": False,
    "log_file_path": "logs/astrbot.log",
    "log_file_max_mb": 20,
    "temp_dir_max_size": 1024,
    "trace_enable": False,
    "trace_log_enable": False,
    "trace_log_path": "logs/astrbot.trace.log",
    "trace_log_max_mb": 20,
    "pip_install_arg": "",
    "pypi_index_url": "https://mirrors.aliyun.com/pypi/simple/",
    "persona": [],  # deprecated
    "timezone": "Asia/Shanghai",
    "callback_api_base": "",
    "default_kb_collection": "",  # 默认知识库名称, 已经过时
    "plugin_set": ["*"],  # "*" 表示使用所有可用的插件, 空列表表示不使用任何插件
    "kb_names": [],  # 默认知识库名称列表
    "kb_fusion_top_k": 20,  # 知识库检索融合阶段返回结果数量
    "kb_final_top_k": 5,  # 知识库检索最终返回结果数量
    "kb_agentic_mode": False,
    "disable_builtin_commands": False,
}


class ChatProviderTemplate(TypedDict):
    id: str
    provider_source_id: str
    model: str
    modalities: list
    custom_extra_body: dict[str, Any]
    max_context_tokens: int


CHAT_PROVIDER_TEMPLATE = {
    "id": "",
    "provide_source_id": "",
    "model": "",
    "modalities": [],
    "custom_extra_body": {},
    "max_context_tokens": 0,
}

"""
AstrBot v3 时代的配置元数据，目前仅承担以下功能：

1. 保存配置时，配置项的类型验证
2. WebUI 展示提供商和平台适配器模版

WebUI 的配置文件在 `CONFIG_METADATA_3` 中。

未来将会逐步淘汰此配置元数据。
"""
CONFIG_METADATA_2 = {
    "platform_group": {
        "metadata": {
            "platform": {
                "description": t("core-config-default-messaging_platform_adapter_desc"),
                "type": "list",
                "config_template": {
                    t("core-config-default-qq_official_websocket"): {
                        "id": "default",
                        "type": "qq_official",
                        "enable": False,
                        "appid": "",
                        "secret": "",
                        "enable_group_c2c": True,
                        "enable_guild_direct_message": True,
                    },
                    t("core-config-default-qq_official_webhook"): {
                        "id": "default",
                        "type": "qq_official_webhook",
                        "enable": False,
                        "appid": "",
                        "secret": "",
                        "is_sandbox": False,
                        "unified_webhook_mode": True,
                        "webhook_uuid": "",
                        "callback_server_host": "0.0.0.0",
                        "port": 6196,
                    },
                    "OneBot v11": {
                        "id": "default",
                        "type": "aiocqhttp",
                        "enable": False,
                        "ws_reverse_host": "0.0.0.0",
                        "ws_reverse_port": 6199,
                        "ws_reverse_token": "",
                    },
                    t("core-config-default-wechat_official_account"): {
                        "id": "weixin_official_account",
                        "type": "weixin_official_account",
                        "enable": False,
                        "appid": "",
                        "secret": "",
                        "token": "",
                        "encoding_aes_key": "",
                        "api_base_url": "https://api.weixin.qq.com/cgi-bin/",
                        "unified_webhook_mode": True,
                        "webhook_uuid": "",
                        "callback_server_host": "0.0.0.0",
                        "port": 6194,
                        "active_send_mode": False,
                    },
                    t("core-config-default-enterprise_wechat"): {
                        "id": "wecom",
                        "type": "wecom",
                        "enable": False,
                        "corpid": "",
                        "secret": "",
                        "token": "",
                        "encoding_aes_key": "",
                        "kf_name": "",
                        "api_base_url": "https://qyapi.weixin.qq.com/cgi-bin/",
                        "unified_webhook_mode": True,
                        "webhook_uuid": "",
                        "callback_server_host": "0.0.0.0",
                        "port": 6195,
                    },
                    t("core-config-default-enterprise_wechat_bot"): {
                        "id": "wecom_ai_bot",
                        "type": "wecom_ai_bot",
                        "enable": True,
                        "wecomaibot_init_respond_text": "",
                        "wecomaibot_friend_message_welcome_text": "",
                        "wecom_ai_bot_name": "",
                        "msg_push_webhook_url": "",
                        "only_use_webhook_url_to_send": False,
                        "token": "",
                        "encoding_aes_key": "",
                        "unified_webhook_mode": True,
                        "webhook_uuid": "",
                        "callback_server_host": "0.0.0.0",
                        "port": 6198,
                    },
                    t("core-config-default-feishu_lark"): {
                        "id": "lark",
                        "type": "lark",
                        "enable": False,
                        "lark_bot_name": "",
                        "app_id": "",
                        "app_secret": "",
                        "domain": "https://open.feishu.cn",
                        "lark_connection_mode": "socket",  # webhook, socket
                        "webhook_uuid": "",
                        "lark_encrypt_key": "",
                        "lark_verification_token": "",
                    },
                    t("core-config-default-dingtalk"): {
                        "id": "dingtalk",
                        "type": "dingtalk",
                        "enable": False,
                        "client_id": "",
                        "client_secret": "",
                        "card_template_id": "",
                    },
                    "Telegram": {
                        "id": "telegram",
                        "type": "telegram",
                        "enable": False,
                        "telegram_token": "your_bot_token",
                        "start_message": "Hello, I'm AstrBot!",
                        "telegram_api_base_url": "https://api.telegram.org/bot",
                        "telegram_file_base_url": "https://api.telegram.org/file/bot",
                        "telegram_command_register": True,
                        "telegram_command_auto_refresh": True,
                        "telegram_command_register_interval": 300,
                    },
                    "Discord": {
                        "id": "discord",
                        "type": "discord",
                        "enable": False,
                        "discord_token": "",
                        "discord_proxy": "",
                        "discord_command_register": True,
                        "discord_guild_id_for_debug": "",
                        "discord_activity_name": "",
                    },
                    "Misskey": {
                        "id": "misskey",
                        "type": "misskey",
                        "enable": False,
                        "misskey_instance_url": "https://misskey.example",
                        "misskey_token": "",
                        "misskey_default_visibility": "public",
                        "misskey_local_only": False,
                        "misskey_enable_chat": True,
                        # download / security options
                        "misskey_allow_insecure_downloads": False,
                        "misskey_download_timeout": 15,
                        "misskey_download_chunk_size": 65536,
                        "misskey_max_download_bytes": None,
                        "misskey_enable_file_upload": True,
                        "misskey_upload_concurrency": 3,
                        "misskey_upload_folder": "",
                    },
                    "Slack": {
                        "id": "slack",
                        "type": "slack",
                        "enable": False,
                        "bot_token": "",
                        "app_token": "",
                        "signing_secret": "",
                        "slack_connection_mode": "socket",  # webhook, socket
                        "unified_webhook_mode": True,
                        "webhook_uuid": "",
                        "slack_webhook_host": "0.0.0.0",
                        "slack_webhook_port": 6197,
                        "slack_webhook_path": "/astrbot-slack-webhook/callback",
                    },
                    # LINE's config is located in line_adapter.py
                    "Satori": {
                        "id": "satori",
                        "type": "satori",
                        "enable": False,
                        "satori_api_base_url": "http://localhost:5140/satori/v1",
                        "satori_endpoint": "ws://localhost:5140/satori/v1/events",
                        "satori_token": "",
                        "satori_auto_reconnect": True,
                        "satori_heartbeat_interval": 10,
                        "satori_reconnect_delay": 5,
                    },
                    # "WebChat": {
                    #     "id": "webchat",
                    #     "type": "webchat",
                    #     "enable": False,
                    #     "webchat_link_path": "",
                    #     "webchat_present_type": "fullscreen",
                    # },
                },
                "items": {
                    # "webchat_link_path": {
                    #     "description": "链接路径",
                    #     "_special": "webchat_link_path",
                    #     "type": "string",
                    # },
                    # "webchat_present_type": {
                    #     "_special": "webchat_present_type",
                    #     "description": "展现形式",
                    #     "type": "string",
                    #     "options": ["fullscreen", "embedded"],
                    # },
                    "lark_connection_mode": {
                        "description": t(
                            "core-config-default-subscription_method_desc"
                        ),
                        "type": "string",
                        "options": ["socket", "webhook"],
                        "labels": [
                            t("core-config-default-connection_mode_labels-part1"),
                            t("core-config-default-connection_mode_labels-part2"),
                        ],
                    },
                    "lark_encrypt_key": {
                        "description": "Encrypt Key",
                        "type": "string",
                        "hint": t(
                            "core-config-default-feishu_callback_encryption_key_hint"
                        ),
                        "condition": {
                            "lark_connection_mode": "webhook",
                        },
                    },
                    "lark_verification_token": {
                        "description": "Verification Token",
                        "type": "string",
                        "hint": t(
                            "core-config-default-feishu_callback_verification_token_hint"
                        ),
                        "condition": {
                            "lark_connection_mode": "webhook",
                        },
                    },
                    "is_sandbox": {
                        "description": t("core-config-default-sandbox_mode_desc"),
                        "type": "bool",
                    },
                    "satori_api_base_url": {
                        "description": t(
                            "core-config-default-satori_api_endpoint_desc"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-satori_api_base_url_hint"),
                    },
                    "satori_endpoint": {
                        "description": t(
                            "core-config-default-satori_websocket_endpoint_desc"
                        ),
                        "type": "string",
                        "hint": t(
                            "core-config-default-satori_event_websocket_endpoint"
                        ),
                    },
                    "satori_token": {
                        "description": t("core-config-default-satori_token"),
                        "type": "string",
                        "hint": t("core-config-default-satori_authentication_token"),
                    },
                    "satori_auto_reconnect": {
                        "description": t("core-config-default-enable_auto_reconnect"),
                        "type": "bool",
                        "hint": t("core-config-default-auto_reconnect_on_disconnect"),
                    },
                    "satori_heartbeat_interval": {
                        "description": t(
                            "core-config-default-satori_heartbeat_interval"
                        ),
                        "type": "int",
                        "hint": t(
                            "core-config-default-heartbeat_send_interval_seconds"
                        ),
                    },
                    "satori_reconnect_delay": {
                        "description": t("core-config-default-satori_reconnect_delay"),
                        "type": "int",
                        "hint": t("core-config-default-reconnect_delay_seconds"),
                    },
                    "slack_connection_mode": {
                        "description": "Slack Connection Mode",
                        "type": "string",
                        "options": ["webhook", "socket"],
                        "hint": "The connection mode for Slack. `webhook` uses a webhook server, `socket` uses Slack's Socket Mode.",
                    },
                    "slack_webhook_host": {
                        "description": "Slack Webhook Host",
                        "type": "string",
                        "hint": "Only valid when Slack connection mode is `webhook`.",
                        "condition": {
                            "slack_connection_mode": "webhook",
                            "unified_webhook_mode": False,
                        },
                    },
                    "slack_webhook_port": {
                        "description": "Slack Webhook Port",
                        "type": "int",
                        "hint": "Only valid when Slack connection mode is `webhook`.",
                        "condition": {
                            "slack_connection_mode": "webhook",
                            "unified_webhook_mode": False,
                        },
                    },
                    "slack_webhook_path": {
                        "description": "Slack Webhook Path",
                        "type": "string",
                        "hint": "Only valid when Slack connection mode is `webhook`.",
                        "condition": {
                            "slack_connection_mode": "webhook",
                            "unified_webhook_mode": False,
                        },
                    },
                    "active_send_mode": {
                        "description": t(
                            "core-config-default-use_active_sending_interface"
                        ),
                        "type": "bool",
                        "desc": t(
                            "core-config-default-active_sending_enterprise_only_note"
                        ),
                    },
                    "wpp_active_message_poll": {
                        "description": t(
                            "core-config-default-enable_active_message_polling"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-active_polling_enable_hint"),
                    },
                    "wpp_active_message_poll_interval": {
                        "description": t(
                            "core-config-default-active_message_polling_interval"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-polling_interval_seconds_hint"),
                    },
                    "kf_name": {
                        "description": t("core-config-default-wechat_kf_account_name"),
                        "type": "string",
                        "hint": t("core-config-default-wechat_kf_account_name_hint"),
                    },
                    "telegram_token": {
                        "description": "Bot Token",
                        "type": "string",
                        "hint": t("core-config-default-china_network_proxy_hint"),
                    },
                    "misskey_instance_url": {
                        "description": t("core-config-default-misskey_instance_url"),
                        "type": "string",
                        "hint": t("core-config-default-misskey_instance_url_hint"),
                    },
                    "misskey_token": {
                        "description": "Misskey Access Token",
                        "type": "string",
                        "hint": t("core-config-default-api_auth_access_token_hint"),
                    },
                    "misskey_default_visibility": {
                        "description": t(
                            "core-config-default-default_post_visibility_description"
                        ),
                        "type": "string",
                        "options": ["public", "home", "followers"],
                        "hint": t("core-config-default-bot_default_visibility_hint"),
                    },
                    "misskey_local_only": {
                        "description": t(
                            "core-config-default-local_only_no_federation_description"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-local_only_posts_hint"),
                    },
                    "misskey_enable_chat": {
                        "description": t(
                            "core-config-default-enable_chat_responses_description"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-enable_chat_responses_hint"),
                    },
                    "misskey_enable_file_upload": {
                        "description": t(
                            "core-config-default-enable_misskey_file_upload_description"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-misskey_file_upload_hint"),
                    },
                    "misskey_allow_insecure_downloads": {
                        "description": t(
                            "core-config-default-allow_insecure_downloads_description"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-insecure_download_fallback_hint"
                        ),
                    },
                    "misskey_download_timeout": {
                        "description": t(
                            "core-config-default-remote_download_timeout_description"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-download_timeout_hint"),
                    },
                    "misskey_download_chunk_size": {
                        "description": t(
                            "core-config-default-streaming_chunk_size_description"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-chunk_size_hint"),
                    },
                    "misskey_max_download_bytes": {
                        "description": t(
                            "core-config-default-max_download_bytes_description"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-max_download_limit_hint"),
                    },
                    "misskey_upload_concurrency": {
                        "description": t(
                            "core-config-default-concurrent_upload_limit_description"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-concurrent_uploads_hint"),
                    },
                    "misskey_upload_folder": {
                        "description": t(
                            "core-config-default-cloud_drive_target_folder_id_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-hint_misskey_drive_folder_id"),
                    },
                    "card_template_id": {
                        "description": t(
                            "core-config-default-description_dingtalk_card_template_id"
                        ),
                        "type": "string",
                        "hint": t(
                            "core-config-default-hint_dingtalk_interactive_card_template_id"
                        ),
                    },
                    "telegram_command_register": {
                        "description": t(
                            "core-config-default-description_telegram_command_registration"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-hint_telegram_auto_register_commands"
                        ),
                    },
                    "telegram_command_auto_refresh": {
                        "description": t(
                            "core-config-default-description_telegram_command_auto_refresh"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-hint_telegram_auto_refresh_commands"
                        ),
                    },
                    "telegram_command_register_interval": {
                        "description": t(
                            "core-config-default-description_telegram_command_refresh_interval"
                        ),
                        "type": "int",
                        "hint": t(
                            "core-config-default-hint_telegram_command_refresh_interval_seconds"
                        ),
                    },
                    "id": {
                        "description": t("core-config-default-description_bot_name"),
                        "type": "string",
                        "hint": t("core-config-default-hint_bot_name"),
                    },
                    "type": {
                        "description": t(
                            "core-config-default-description_adapter_type"
                        ),
                        "type": "string",
                        "invisible": True,
                    },
                    "enable": {
                        "description": t("core-config-default-description_enable"),
                        "type": "bool",
                        "hint": t("core-config-default-hint_enable_adapter"),
                    },
                    "appid": {
                        "description": "appid",
                        "type": "string",
                        "hint": t("core-config-default-hint_qq_official_appid"),
                    },
                    "secret": {
                        "description": "secret",
                        "type": "string",
                        "hint": t("core-config-default-hint_required_field"),
                    },
                    "enable_group_c2c": {
                        "description": t(
                            "core-config-default-description_enable_private_msg_from_list"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-hint_enable_qq_private_from_list"
                        ),
                    },
                    "enable_guild_direct_message": {
                        "description": t(
                            "core-config-default-description_enable_channel_private_msg"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-hint_enable_channel_private_messages"
                        ),
                    },
                    "ws_reverse_host": {
                        "description": t("core-config-default-reverse_websocket_host"),
                        "type": "string",
                        "hint": t("core-config-default-reverse_websocket_hint"),
                    },
                    "ws_reverse_port": {
                        "description": t("core-config-default-reverse_websocket_port"),
                        "type": "int",
                    },
                    "ws_reverse_token": {
                        "description": t("core-config-default-reverse_websocket_token"),
                        "type": "string",
                        "hint": t("core-config-default-reverse_websocket_token_hint"),
                    },
                    "wecom_ai_bot_name": {
                        "description": t("core-config-default-wecom_robot_name"),
                        "type": "string",
                        "hint": t("core-config-default-wecom_robot_name_hint"),
                    },
                    "wecomaibot_init_respond_text": {
                        "description": t("core-config-default-wecom_initial_response"),
                        "type": "string",
                        "hint": t("core-config-default-wecom_initial_response_hint"),
                    },
                    "wecomaibot_friend_message_welcome_text": {
                        "description": t("core-config-default-wecom_private_welcome"),
                        "type": "string",
                        "hint": t("core-config-default-wecom_private_welcome_hint"),
                    },
                    "msg_push_webhook_url": {
                        "description": t("core-config-default-wecom_webhook_url"),
                        "type": "string",
                        "hint": t("core-config-default-wecom_webhook_url_hint"),
                    },
                    "only_use_webhook_url_to_send": {
                        "description": t("core-config-default-wecom_webhook_only"),
                        "type": "bool",
                        "hint": t("core-config-default-wecom_webhook_only_hint"),
                    },
                    "lark_bot_name": {
                        "description": t("core-config-default-feishu_robot_name"),
                        "type": "string",
                        "hint": t("core-config-default-feishu_robot_name_hint"),
                    },
                    "discord_token": {
                        "description": "Discord Bot Token",
                        "type": "string",
                        "hint": t("core-config-default-discord_bot_token_hint"),
                    },
                    "discord_proxy": {
                        "description": t("core-config-default-discord_proxy"),
                        "type": "string",
                        "hint": t("core-config-default-discord_proxy_hint"),
                    },
                    "discord_command_register": {
                        "description": t(
                            "core-config-default-auto_register_discord_slash"
                        ),
                        "type": "bool",
                    },
                    "discord_activity_name": {
                        "description": t("core-config-default-discord_activity_name"),
                        "type": "string",
                        "hint": t("core-config-default-discord_activity_name_hint"),
                    },
                    "port": {
                        "description": t("core-config-default-callback_server_port"),
                        "type": "int",
                        "hint": t("core-config-default-callback_server_port_hint"),
                        "condition": {
                            "unified_webhook_mode": False,
                        },
                    },
                    "callback_server_host": {
                        "description": t("core-config-default-callback_server_host"),
                        "type": "string",
                        "hint": t("core-config-default-callback_server_host_hint"),
                        "condition": {
                            "unified_webhook_mode": False,
                        },
                    },
                    "unified_webhook_mode": {
                        "description": t("core-config-default-unified_webhook_mode"),
                        "type": "bool",
                        "hint": t("core-config-default-webhook_hint"),
                    },
                    "webhook_uuid": {
                        "invisible": True,
                        "description": "Webhook UUID",
                        "type": "string",
                        "hint": t("core-config-default-webhook_uuid_hint"),
                    },
                },
            },
            "platform_settings": {
                "type": "object",
                "items": {
                    "unique_session": {
                        "type": "bool",
                    },
                    "rate_limit": {
                        "type": "object",
                        "items": {
                            "time": {"type": "int"},
                            "count": {"type": "int"},
                            "strategy": {
                                "type": "string",
                                "options": ["stall", "discard"],
                            },
                        },
                    },
                    "no_permission_reply": {
                        "type": "bool",
                        "hint": t("core-config-default-reply_on_no_permission"),
                    },
                    "empty_mention_waiting": {
                        "type": "bool",
                        "hint": t("core-config-default-wait_on_mention_only"),
                    },
                    "empty_mention_waiting_need_reply": {
                        "type": "bool",
                        "hint": t("core-config-default-generate_reply_during_wait"),
                    },
                    "friend_message_needs_wake_prefix": {
                        "type": "bool",
                        "hint": t("core-config-default-require_prefix_in_dm"),
                    },
                    "ignore_bot_self_message": {
                        "type": "bool",
                        "hint": t(
                            "core-config-default-self_message_from_other_client_note"
                        ),
                    },
                    "ignore_at_all": {
                        "type": "bool",
                        "hint": t("core-config-default-ignore_everyone_mention"),
                    },
                    "segmented_reply": {
                        "type": "object",
                        "items": {
                            "enable": {
                                "type": "bool",
                            },
                            "only_llm_result": {
                                "type": "bool",
                            },
                            "interval_method": {
                                "type": "string",
                                "options": ["random", "log"],
                            },
                            "interval": {
                                "type": "string",
                            },
                            "log_base": {
                                "type": "float",
                            },
                            "words_count_threshold": {
                                "type": "int",
                            },
                            "regex": {
                                "type": "string",
                            },
                            "content_cleanup_rule": {
                                "type": "string",
                            },
                        },
                    },
                    "reply_prefix": {
                        "type": "string",
                        "hint": t("core-config-default-reply_prefix"),
                    },
                    "forward_threshold": {
                        "type": "int",
                        "hint": t("core-config-default-fold_long_messages_qq"),
                    },
                    "enable_id_white_list": {
                        "type": "bool",
                    },
                    "id_whitelist": {
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t("core-config-default-session_whitelist_hint"),
                    },
                    "id_whitelist_log": {
                        "type": "bool",
                        "hint": t("core-config-default-log_whitelist_failure"),
                    },
                    "wl_ignore_admin_on_group": {
                        "type": "bool",
                    },
                    "wl_ignore_admin_on_friend": {
                        "type": "bool",
                    },
                    "reply_with_mention": {
                        "type": "bool",
                        "hint": t("core-config-default-enable_mention_sender"),
                    },
                    "reply_with_quote": {
                        "type": "bool",
                        "hint": t("core-config-default-enable_quote_reply"),
                    },
                    "path_mapping": {
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t("core-config-default-path_mapping"),
                    },
                },
            },
            "content_safety": {
                "type": "object",
                "items": {
                    "also_use_in_response": {
                        "type": "bool",
                        "hint": t("core-config-default-enable_llm_content_moderation"),
                    },
                    "baidu_aip": {
                        "type": "object",
                        "items": {
                            "enable": {
                                "type": "bool",
                                "hint": t("core-config-default-baidu_aip_install_hint"),
                            },
                            "app_id": {"description": "APP ID", "type": "string"},
                            "api_key": {"description": "API Key", "type": "string"},
                            "secret_key": {
                                "type": "string",
                            },
                        },
                    },
                    "internal_keywords": {
                        "type": "object",
                        "items": {
                            "enable": {
                                "type": "bool",
                            },
                            "extra_keywords": {
                                "type": "list",
                                "items": {"type": "string"},
                                "hint": t("core-config-default-extra_blocked_keywords"),
                            },
                        },
                    },
                },
            },
        },
    },
    "provider_group": {
        "name": t("core-config-default-service_provider"),
        "metadata": {
            "provider": {
                "type": "list",
                # provider sources templates
                "config_template": {
                    "OpenAI": {
                        "id": "openai",
                        "provider": "openai",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.openai.com/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Google Gemini": {
                        "id": "google_gemini",
                        "provider": "google",
                        "type": "googlegenai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://generativelanguage.googleapis.com/",
                        "timeout": 120,
                        "gm_resp_image_modal": False,
                        "gm_native_search": False,
                        "gm_native_coderunner": False,
                        "gm_url_context": False,
                        "gm_safety_settings": {
                            "harassment": "BLOCK_MEDIUM_AND_ABOVE",
                            "hate_speech": "BLOCK_MEDIUM_AND_ABOVE",
                            "sexually_explicit": "BLOCK_MEDIUM_AND_ABOVE",
                            "dangerous_content": "BLOCK_MEDIUM_AND_ABOVE",
                        },
                        "gm_thinking_config": {"budget": 0, "level": "HIGH"},
                        "proxy": "",
                    },
                    "Anthropic": {
                        "id": "anthropic",
                        "provider": "anthropic",
                        "type": "anthropic_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.anthropic.com/v1",
                        "timeout": 120,
                        "proxy": "",
                        "anth_thinking_config": {"type": "", "budget": 0, "effort": ""},
                    },
                    "Moonshot": {
                        "id": "moonshot",
                        "provider": "moonshot",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "timeout": 120,
                        "api_base": "https://api.moonshot.cn/v1",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "xAI": {
                        "id": "xai",
                        "provider": "xai",
                        "type": "xai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.x.ai/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                        "xai_native_search": False,
                    },
                    "DeepSeek": {
                        "id": "deepseek",
                        "provider": "deepseek",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.deepseek.com/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Zhipu": {
                        "id": "zhipu",
                        "provider": "zhipu",
                        "type": "zhipu_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "timeout": 120,
                        "api_base": "https://open.bigmodel.cn/api/paas/v4/",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "AIHubMix": {
                        "id": "aihubmix",
                        "provider": "aihubmix",
                        "type": "aihubmix_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "timeout": 120,
                        "api_base": "https://aihubmix.com/v1",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "OpenRouter": {
                        "id": "openrouter",
                        "provider": "openrouter",
                        "type": "openrouter_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "timeout": 120,
                        "api_base": "https://openrouter.ai/v1",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "NVIDIA": {
                        "id": "nvidia",
                        "provider": "nvidia",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://integrate.api.nvidia.com/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Azure OpenAI": {
                        "id": "azure_openai",
                        "provider": "azure",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "api_version": "2024-05-01-preview",
                        "key": [],
                        "api_base": "",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Ollama": {
                        "id": "ollama",
                        "provider": "ollama",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": ["ollama"],  # ollama 的 key 默认是 ollama
                        "api_base": "http://127.0.0.1:11434/v1",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "LM Studio": {
                        "id": "lm_studio",
                        "provider": "lm_studio",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": ["lmstudio"],
                        "api_base": "http://127.0.0.1:1234/v1",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Gemini_OpenAI_API": {
                        "id": "google_gemini_openai",
                        "provider": "google",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://generativelanguage.googleapis.com/v1beta/openai/",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Groq": {
                        "id": "groq",
                        "provider": "groq",
                        "type": "groq_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.groq.com/openai/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "302.AI": {
                        "id": "302ai",
                        "provider": "302ai",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.302.ai/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "SiliconFlow": {
                        "id": "siliconflow",
                        "provider": "siliconflow",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "timeout": 120,
                        "api_base": "https://api.siliconflow.cn/v1",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "PPIO": {
                        "id": "ppio",
                        "provider": "ppio",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.ppinfra.com/v3/openai",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "TokenPony": {
                        "id": "tokenpony",
                        "provider": "tokenpony",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.tokenpony.cn/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Compshare": {
                        "id": "compshare",
                        "provider": "compshare",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.modelverse.cn/v1",
                        "timeout": 120,
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "ModelScope": {
                        "id": "modelscope",
                        "provider": "modelscope",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "timeout": 120,
                        "api_base": "https://api-inference.modelscope.cn/v1",
                        "proxy": "",
                        "custom_headers": {},
                    },
                    "Dify": {
                        "id": "dify_app_default",
                        "provider": "dify",
                        "type": "dify",
                        "provider_type": "agent_runner",
                        "enable": True,
                        "dify_api_type": "chat",
                        "dify_api_key": "",
                        "dify_api_base": "https://api.dify.ai/v1",
                        "dify_workflow_output_key": "astrbot_wf_output",
                        "dify_query_input_key": "astrbot_text_query",
                        "variables": {},
                        "timeout": 60,
                        "proxy": "",
                    },
                    "Coze": {
                        "id": "coze",
                        "provider": "coze",
                        "provider_type": "agent_runner",
                        "type": "coze",
                        "enable": True,
                        "coze_api_key": "",
                        "bot_id": "",
                        "coze_api_base": "https://api.coze.cn",
                        "timeout": 60,
                        "proxy": "",
                        # "auto_save_history": True,
                    },
                    t("core-config-default-aliyun_bailian_app"): {
                        "id": "dashscope",
                        "provider": "dashscope",
                        "type": "dashscope",
                        "provider_type": "agent_runner",
                        "enable": True,
                        "dashscope_app_type": "agent",
                        "dashscope_api_key": "",
                        "dashscope_app_id": "",
                        "rag_options": {
                            "pipeline_ids": [],
                            "file_ids": [],
                            "output_reference": False,
                        },
                        "variables": {},
                        "timeout": 60,
                        "proxy": "",
                    },
                    "FastGPT": {
                        "id": "fastgpt",
                        "provider": "fastgpt",
                        "type": "openai_chat_completion",
                        "provider_type": "chat_completion",
                        "enable": True,
                        "key": [],
                        "api_base": "https://api.fastgpt.in/api/v1",
                        "timeout": 60,
                        "proxy": "",
                        "custom_headers": {},
                        "custom_extra_body": {},
                    },
                    "Whisper(API)": {
                        "id": "whisper",
                        "provider": "openai",
                        "type": "openai_whisper_api",
                        "provider_type": "speech_to_text",
                        "enable": False,
                        "api_key": "",
                        "api_base": "",
                        "model": "whisper-1",
                        "proxy": "",
                    },
                    "Whisper(Local)": {
                        "provider": "openai",
                        "type": "openai_whisper_selfhost",
                        "provider_type": "speech_to_text",
                        "enable": False,
                        "id": "whisper_selfhost",
                        "model": "tiny",
                    },
                    "SenseVoice(Local)": {
                        "type": "sensevoice_stt_selfhost",
                        "provider": "sensevoice",
                        "provider_type": "speech_to_text",
                        "enable": False,
                        "id": "sensevoice",
                        "stt_model": "iic/SenseVoiceSmall",
                        "is_emotion": False,
                    },
                    "OpenAI TTS(API)": {
                        "id": "openai_tts",
                        "type": "openai_tts_api",
                        "provider": "openai",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "api_key": "",
                        "api_base": "",
                        "model": "tts-1",
                        "openai-tts-voice": "alloy",
                        "timeout": "20",
                        "proxy": "",
                    },
                    "Genie TTS": {
                        "id": "genie_tts",
                        "provider": "genie_tts",
                        "type": "genie_tts",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "genie_character_name": "mika",
                        "genie_onnx_model_dir": "CharacterModels/v2ProPlus/mika/tts_models",
                        "genie_language": "Japanese",
                        "genie_refer_audio_path": "",
                        "genie_refer_text": "",
                        "timeout": 20,
                    },
                    "Edge TTS": {
                        "id": "edge_tts",
                        "provider": "microsoft",
                        "type": "edge_tts",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "edge-tts-voice": "zh-CN-XiaoxiaoNeural",
                        "rate": "+0%",
                        "volume": "+0%",
                        "pitch": "+0Hz",
                        "timeout": 20,
                    },
                    "GSV TTS(Local)": {
                        "id": "gsv_tts",
                        "enable": False,
                        "provider": "gpt_sovits",
                        "type": "gsv_tts_selfhost",
                        "provider_type": "text_to_speech",
                        "api_base": "http://127.0.0.1:9880",
                        "gpt_weights_path": "",
                        "sovits_weights_path": "",
                        "timeout": 60,
                        "gsv_default_parms": {
                            "gsv_ref_audio_path": "",
                            "gsv_prompt_text": "",
                            "gsv_prompt_lang": "zh",
                            "gsv_aux_ref_audio_paths": "",
                            "gsv_text_lang": "zh",
                            "gsv_top_k": 5,
                            "gsv_top_p": 1.0,
                            "gsv_temperature": 1.0,
                            "gsv_text_split_method": "cut3",
                            "gsv_batch_size": 1,
                            "gsv_batch_threshold": 0.75,
                            "gsv_split_bucket": True,
                            "gsv_speed_factor": 1,
                            "gsv_fragment_interval": 0.3,
                            "gsv_streaming_mode": False,
                            "gsv_seed": -1,
                            "gsv_parallel_infer": True,
                            "gsv_repetition_penalty": 1.35,
                            "gsv_media_type": "wav",
                        },
                    },
                    "GSVI TTS(API)": {
                        "id": "gsvi_tts",
                        "type": "gsvi_tts_api",
                        "provider": "gpt_sovits_inference",
                        "provider_type": "text_to_speech",
                        "api_base": "http://127.0.0.1:5000",
                        "character": "",
                        "emotion": "default",
                        "enable": False,
                        "timeout": 20,
                    },
                    "FishAudio TTS(API)": {
                        "id": "fishaudio_tts",
                        "provider": "fishaudio",
                        "type": "fishaudio_tts_api",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "api_key": "",
                        "api_base": "https://api.fish.audio/v1",
                        "fishaudio-tts-character": t(
                            "core-config-default-fishaudio_tts_character"
                        ),
                        "fishaudio-tts-reference-id": "",
                        "timeout": "20",
                        "proxy": "",
                    },
                    t("core-config-default-aliyun_bailian_tts"): {
                        "hint": t("core-config-default-aliyun_bailian_tts_hint"),
                        "id": "dashscope_tts",
                        "provider": "dashscope",
                        "type": "dashscope_tts",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "api_key": "",
                        "model": "cosyvoice-v1",
                        "dashscope_tts_voice": "loongstella",
                        "timeout": "20",
                    },
                    "Azure TTS": {
                        "id": "azure_tts",
                        "type": "azure_tts",
                        "provider": "azure",
                        "provider_type": "text_to_speech",
                        "enable": True,
                        "azure_tts_voice": "zh-CN-YunxiaNeural",
                        "azure_tts_style": "cheerful",
                        "azure_tts_role": "Boy",
                        "azure_tts_rate": "1",
                        "azure_tts_volume": "100",
                        "azure_tts_subscription_key": "",
                        "azure_tts_region": "eastus",
                        "proxy": "",
                    },
                    "MiniMax TTS(API)": {
                        "id": "minimax_tts",
                        "type": "minimax_tts_api",
                        "provider": "minimax",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "api_key": "",
                        "api_base": "https://api.minimax.chat/v1/t2a_v2",
                        "minimax-group-id": "",
                        "model": "speech-02-turbo",
                        "minimax-langboost": "auto",
                        "minimax-voice-speed": 1.0,
                        "minimax-voice-vol": 1.0,
                        "minimax-voice-pitch": 0,
                        "minimax-is-timber-weight": False,
                        "minimax-voice-id": "female-shaonv",
                        "minimax-timber-weight": '[\n    {\n        "voice_id": "Chinese (Mandarin)_Warm_Girl",\n        "weight": 25\n    },\n    {\n        "voice_id": "Chinese (Mandarin)_BashfulGirl",\n        "weight": 50\n    }\n]',
                        "minimax-voice-emotion": "auto",
                        "minimax-voice-latex": False,
                        "minimax-voice-english-normalization": False,
                        "timeout": 20,
                        "proxy": "",
                    },
                    t("core-config-default-volcengine_tts"): {
                        "id": "volcengine_tts",
                        "type": "volcengine_tts",
                        "provider": "volcengine",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "api_key": "",
                        "appid": "",
                        "volcengine_cluster": "volcano_tts",
                        "volcengine_voice_type": "",
                        "volcengine_speed_ratio": 1.0,
                        "api_base": "https://openspeech.bytedance.com/api/v1/tts",
                        "timeout": 20,
                        "proxy": "",
                    },
                    "Gemini TTS": {
                        "id": "gemini_tts",
                        "type": "gemini_tts",
                        "provider": "google",
                        "provider_type": "text_to_speech",
                        "enable": False,
                        "gemini_tts_api_key": "",
                        "gemini_tts_api_base": "",
                        "gemini_tts_timeout": 20,
                        "gemini_tts_model": "gemini-2.5-flash-preview-tts",
                        "gemini_tts_prefix": "",
                        "gemini_tts_voice_name": "Leda",
                        "proxy": "",
                    },
                    "OpenAI Embedding": {
                        "id": "openai_embedding",
                        "type": "openai_embedding",
                        "provider": "openai",
                        "provider_type": "embedding",
                        "enable": True,
                        "embedding_api_key": "",
                        "embedding_api_base": "",
                        "embedding_model": "",
                        "embedding_dimensions": 1024,
                        "timeout": 20,
                        "proxy": "",
                    },
                    "Gemini Embedding": {
                        "id": "gemini_embedding",
                        "type": "gemini_embedding",
                        "provider": "google",
                        "provider_type": "embedding",
                        "enable": True,
                        "embedding_api_key": "",
                        "embedding_api_base": "",
                        "embedding_model": "gemini-embedding-exp-03-07",
                        "embedding_dimensions": 768,
                        "timeout": 20,
                        "proxy": "",
                    },
                    "vLLM Rerank": {
                        "id": "vllm_rerank",
                        "type": "vllm_rerank",
                        "provider": "vllm",
                        "provider_type": "rerank",
                        "enable": True,
                        "rerank_api_key": "",
                        "rerank_api_base": "http://127.0.0.1:8000",
                        "rerank_model": "BAAI/bge-reranker-base",
                        "timeout": 20,
                    },
                    "Xinference Rerank": {
                        "id": "xinference_rerank",
                        "type": "xinference_rerank",
                        "provider": "xinference",
                        "provider_type": "rerank",
                        "enable": True,
                        "rerank_api_key": "",
                        "rerank_api_base": "http://127.0.0.1:9997",
                        "rerank_model": "BAAI/bge-reranker-base",
                        "timeout": 20,
                        "launch_model_if_not_running": False,
                    },
                    t("core-config-default-aliyun_bailian_rerank"): {
                        "id": "bailian_rerank",
                        "type": "bailian_rerank",
                        "provider": "bailian",
                        "provider_type": "rerank",
                        "enable": True,
                        "rerank_api_key": "",
                        "rerank_api_base": "https://dashscope.aliyuncs.com/api/v1/services/rerank/text-rerank/text-rerank",
                        "rerank_model": "qwen3-rerank",
                        "timeout": 30,
                        "return_documents": False,
                        "instruct": "",
                    },
                    "Xinference STT": {
                        "id": "xinference_stt",
                        "type": "xinference_stt",
                        "provider": "xinference",
                        "provider_type": "speech_to_text",
                        "enable": False,
                        "api_key": "",
                        "api_base": "http://127.0.0.1:9997",
                        "model": "whisper-large-v3",
                        "timeout": 180,
                        "launch_model_if_not_running": False,
                    },
                },
                "items": {
                    "genie_onnx_model_dir": {
                        "description": "ONNX Model Directory",
                        "type": "string",
                        "hint": "The directory path containing the ONNX model files",
                    },
                    "genie_language": {
                        "description": "Language",
                        "type": "string",
                        "options": ["Japanese", "English", "Chinese"],
                    },
                    "provider_source_id": {
                        "invisible": True,
                        "type": "string",
                    },
                    "xai_native_search": {
                        "description": t("core-config-default-enable_native_search"),
                        "type": "bool",
                        "hint": t("core-config-default-xai_native_search_hint"),
                        "condition": {"provider": "xai"},
                    },
                    "rerank_api_base": {
                        "description": t("core-config-default-rerank_model_api_base"),
                        "type": "string",
                        "hint": t("core-config-default-rerank_api_base_hint"),
                    },
                    "rerank_api_key": {
                        "description": "API Key",
                        "type": "string",
                        "hint": t("core-config-default-api_key_optional_hint"),
                    },
                    "rerank_model": {
                        "description": t("core-config-default-rerank_model_name"),
                        "type": "string",
                    },
                    "return_documents": {
                        "description": t("core-config-default-rerank_return_documents"),
                        "type": "bool",
                        "hint": t("core-config-default-hint_reduce_network_overhead"),
                    },
                    "instruct": {
                        "description": t(
                            "core-config-default-description_custom_sort_task_type"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-hint_qwen3_rerank_english"),
                    },
                    "launch_model_if_not_running": {
                        "description": t(
                            "core-config-default-description_auto_start_model"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-hint_auto_start_production_note"
                        ),
                    },
                    "modalities": {
                        "description": t(
                            "core-config-default-description_model_capabilities"
                        ),
                        "type": "list",
                        "items": {"type": "string"},
                        "options": ["text", "image", "tool_use"],
                        "labels": [
                            t("core-config-default-content_type_labels-part1"),
                            t("core-config-default-content_type_labels-part2"),
                            t("core-config-default-content_type_labels-part3"),
                        ],
                        "render_type": "checkbox",
                        "hint": t(
                            "core-config-default-hint_select_supported_modalities"
                        ),
                    },
                    "custom_headers": {
                        "description": t(
                            "core-config-default-description_custom_request_headers"
                        ),
                        "type": "dict",
                        "items": {},
                        "hint": t("core-config-default-hint_custom_headers_sdk_merge"),
                    },
                    "custom_extra_body": {
                        "description": t(
                            "core-config-default-description_custom_body_params"
                        ),
                        "type": "dict",
                        "items": {},
                        "hint": t("core-config-default-hint_extra_body_parameters"),
                        "template_schema": {
                            "temperature": {
                                "name": "Temperature",
                                "description": t(
                                    "core-config-default-description_temperature_parameter"
                                ),
                                "hint": t(
                                    "core-config-default-hint_temperature_randomness"
                                ),
                                "type": "float",
                                "default": 0.6,
                                "slider": {"min": 0, "max": 2, "step": 0.1},
                            },
                            "top_p": {
                                "name": "Top-p",
                                "description": t(
                                    "core-config-default-description_top_p_sampling"
                                ),
                                "hint": t("core-config-default-hint_top_p_nucleus"),
                                "type": "float",
                                "default": 1.0,
                                "slider": {"min": 0, "max": 1, "step": 0.01},
                            },
                            "max_tokens": {
                                "name": "Max Tokens",
                                "description": t(
                                    "core-config-default-description_max_tokens"
                                ),
                                "hint": t(
                                    "core-config-default-hint_max_generation_tokens"
                                ),
                                "type": "int",
                                "default": 8192,
                            },
                        },
                    },
                    "provider": {
                        "type": "string",
                        "invisible": True,
                    },
                    "gpt_weights_path": {
                        "description": t(
                            "core-config-default-description_gpt_model_path"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-hint_sovits_ckpt_path"),
                    },
                    "sovits_weights_path": {
                        "description": t("core-config-default-sovits_model_file_path"),
                        "type": "string",
                        "hint": t("core-config-default-sovits_model_path_hint"),
                    },
                    "gsv_default_parms": {
                        "description": t(
                            "core-config-default-gpt_sovits_default_params"
                        ),
                        "hint": t("core-config-default-gpt_sovits_params_hint"),
                        "type": "object",
                        "items": {
                            "gsv_ref_audio_path": {
                                "description": t(
                                    "core-config-default-reference_audio_file_path"
                                ),
                                "type": "string",
                                "hint": t(
                                    "core-config-default-reference_audio_path_hint"
                                ),
                            },
                            "gsv_prompt_text": {
                                "description": t(
                                    "core-config-default-reference_audio_text"
                                ),
                                "type": "string",
                                "hint": t(
                                    "core-config-default-reference_audio_text_hint"
                                ),
                            },
                            "gsv_prompt_lang": {
                                "description": t(
                                    "core-config-default-reference_audio_text_language"
                                ),
                                "type": "string",
                                "hint": t(
                                    "core-config-default-reference_audio_language_hint"
                                ),
                            },
                            "gsv_aux_ref_audio_paths": {
                                "description": t(
                                    "core-config-default-aux_reference_audio_file_path"
                                ),
                                "type": "string",
                                "hint": t(
                                    "core-config-default-aux_reference_audio_path_hint"
                                ),
                            },
                            "gsv_text_lang": {
                                "description": t("core-config-default-text_language"),
                                "type": "string",
                                "hint": t("core-config-default-text_language_hint"),
                            },
                            "gsv_top_k": {
                                "description": t(
                                    "core-config-default-speech_diversity"
                                ),
                                "type": "int",
                                "hint": "",
                            },
                            "gsv_top_p": {
                                "description": t("core-config-default-top_p_threshold"),
                                "type": "float",
                                "hint": "",
                            },
                            "gsv_temperature": {
                                "description": t(
                                    "core-config-default-speech_randomness"
                                ),
                                "type": "float",
                                "hint": "",
                            },
                            "gsv_text_split_method": {
                                "description": t(
                                    "core-config-default-text_splitting_method"
                                ),
                                "type": "string",
                                "hint": t("core-config-default-text_split_method_hint"),
                                "options": [
                                    "cut0",
                                    "cut1",
                                    "cut2",
                                    "cut3",
                                    "cut4",
                                    "cut5",
                                ],
                            },
                            "gsv_batch_size": {
                                "description": t("core-config-default-batch_size"),
                                "type": "int",
                                "hint": "",
                            },
                            "gsv_batch_threshold": {
                                "description": t(
                                    "core-config-default-batch_processing_threshold"
                                ),
                                "type": "float",
                                "hint": "",
                            },
                            "gsv_split_bucket": {
                                "description": t(
                                    "core-config-default-text_bucket_parallel_processing"
                                ),
                                "type": "bool",
                                "hint": "",
                            },
                            "gsv_speed_factor": {
                                "description": t(
                                    "core-config-default-speech_playback_speed"
                                ),
                                "type": "float",
                                "hint": t(
                                    "core-config-default-speech_speed_original_hint"
                                ),
                            },
                            "gsv_fragment_interval": {
                                "description": t(
                                    "core-config-default-speech_segment_interval"
                                ),
                                "type": "float",
                                "hint": "",
                            },
                            "gsv_streaming_mode": {
                                "description": t(
                                    "core-config-default-enable_streaming_mode"
                                ),
                                "type": "bool",
                                "hint": "",
                            },
                            "gsv_seed": {
                                "description": t("core-config-default-random_seed"),
                                "type": "int",
                                "hint": t(
                                    "core-config-default-random_seed_reproducibility_hint"
                                ),
                            },
                            "gsv_parallel_infer": {
                                "description": t(
                                    "core-config-default-parallel_inference_execution"
                                ),
                                "type": "bool",
                                "hint": "",
                            },
                            "gsv_repetition_penalty": {
                                "description": t(
                                    "core-config-default-repetition_penalty_factor"
                                ),
                                "type": "float",
                                "hint": "",
                            },
                            "gsv_media_type": {
                                "description": t(
                                    "core-config-default-output_media_type"
                                ),
                                "type": "string",
                                "hint": t(
                                    "core-config-default-output_media_type_wav_recommended"
                                ),
                            },
                        },
                    },
                    "embedding_dimensions": {
                        "description": t("core-config-default-embedding_dimension"),
                        "type": "int",
                        "hint": t("core-config-default-embedding_dimension_hint"),
                        "_special": "get_embedding_dim",
                    },
                    "embedding_model": {
                        "description": t("core-config-default-embedding_model"),
                        "type": "string",
                        "hint": t("core-config-default-embedding_model_name_hint"),
                    },
                    "embedding_api_key": {
                        "description": "API Key",
                        "type": "string",
                    },
                    "embedding_api_base": {
                        "description": "API Base URL",
                        "type": "string",
                    },
                    "volcengine_cluster": {
                        "type": "string",
                        "description": t("core-config-default-volcano_engine_cluster"),
                        "hint": t("core-config-default-volcano_engine_cluster_hint"),
                    },
                    "volcengine_voice_type": {
                        "type": "string",
                        "description": t(
                            "core-config-default-volcano_engine_voice_tone"
                        ),
                        "hint": t("core-config-default-volcano_engine_voice_id_hint"),
                    },
                    "volcengine_speed_ratio": {
                        "type": "float",
                        "description": t(
                            "core-config-default-speech_speed_description"
                        ),
                        "hint": t("core-config-default-speech_speed_hint"),
                    },
                    "volcengine_volume_ratio": {
                        "type": "float",
                        "description": t("core-config-default-volume_description"),
                        "hint": t("core-config-default-volume_hint"),
                    },
                    "azure_tts_voice": {
                        "type": "string",
                        "description": t("core-config-default-voice_description"),
                        "hint": t("core-config-default-voice_hint"),
                    },
                    "azure_tts_style": {
                        "type": "string",
                        "description": t("core-config-default-style_description"),
                        "hint": t("core-config-default-style_hint"),
                    },
                    "azure_tts_role": {
                        "type": "string",
                        "description": t("core-config-default-role_description"),
                        "hint": t("core-config-default-role_hint"),
                        "options": [
                            "Boy",
                            "Girl",
                            "YoungAdultFemale",
                            "YoungAdultMale",
                            "OlderAdultFemale",
                            "OlderAdultMale",
                            "SeniorFemale",
                            "SeniorMale",
                            t("core-config-default-disabled"),
                        ],
                    },
                    "azure_tts_rate": {
                        "type": "string",
                        "description": t("core-config-default-speech_rate_description"),
                        "hint": t("core-config-default-speech_rate_hint"),
                    },
                    "azure_tts_volume": {
                        "type": "string",
                        "description": t(
                            "core-config-default-speech_volume_description"
                        ),
                        "hint": t("core-config-default-speech_volume_hint"),
                    },
                    "azure_tts_region": {
                        "type": "string",
                        "description": t("core-config-default-api_region_description"),
                        "hint": t("core-config-default-api_region_hint"),
                        "options": [
                            "southafricanorth",
                            "eastasia",
                            "southeastasia",
                            "australiaeast",
                            "centralindia",
                            "japaneast",
                            "japanwest",
                            "koreacentral",
                            "canadacentral",
                            "northeurope",
                            "westeurope",
                            "francecentral",
                            "germanywestcentral",
                            "norwayeast",
                            "swedencentral",
                            "switzerlandnorth",
                            "switzerlandwest",
                            "uksouth",
                            "uaenorth",
                            "brazilsouth",
                            "qatarcentral",
                            "centralus",
                            "eastus",
                            "eastus2",
                            "northcentralus",
                            "southcentralus",
                            "westcentralus",
                            "westus",
                            "westus2",
                            "westus3",
                        ],
                    },
                    "azure_tts_subscription_key": {
                        "type": "string",
                        "description": t(
                            "core-config-default-subscription_key_description"
                        ),
                        "hint": t("core-config-default-subscription_key_hint"),
                    },
                    "dashscope_tts_voice": {
                        "description": t(
                            "core-config-default-dashscope_tts_voice_description"
                        ),
                        "type": "string",
                    },
                    "gm_resp_image_modal": {
                        "description": t("core-config-default-enable_image_modality"),
                        "type": "bool",
                        "hint": t("core-config-default-image_modality_hint"),
                    },
                    "gm_native_search": {
                        "description": t("core-config-default-enable_native_search"),
                        "type": "bool",
                        "hint": t("core-config-default-native_search_hint"),
                    },
                    "gm_native_coderunner": {
                        "description": t(
                            "core-config-default-enable_native_code_executor"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-native_code_executor_hint"),
                    },
                    "gm_url_context": {
                        "description": t("core-config-default-enable_url_context"),
                        "type": "bool",
                        "hint": t("core-config-default-url_context_hint"),
                    },
                    "gm_safety_settings": {
                        "description": t("core-config-default-safety_filters"),
                        "type": "object",
                        "hint": t("core-config-default-safety_filters_hint"),
                        "items": {
                            "harassment": {
                                "description": t(
                                    "core-config-default-harassment_content"
                                ),
                                "type": "string",
                                "hint": t("core-config-default-harassment_hint"),
                                "options": [
                                    "BLOCK_NONE",
                                    "BLOCK_ONLY_HIGH",
                                    "BLOCK_MEDIUM_AND_ABOVE",
                                    "BLOCK_LOW_AND_ABOVE",
                                ],
                            },
                            "hate_speech": {
                                "description": t("core-config-default-hate_speech"),
                                "type": "string",
                                "hint": t("core-config-default-hate_speech_hint"),
                                "options": [
                                    "BLOCK_NONE",
                                    "BLOCK_ONLY_HIGH",
                                    "BLOCK_MEDIUM_AND_ABOVE",
                                    "BLOCK_LOW_AND_ABOVE",
                                ],
                            },
                            "sexually_explicit": {
                                "description": t(
                                    "core-config-default-sexually_explicit"
                                ),
                                "type": "string",
                                "hint": t("core-config-default-sexually_explicit_hint"),
                                "options": [
                                    "BLOCK_NONE",
                                    "BLOCK_ONLY_HIGH",
                                    "BLOCK_MEDIUM_AND_ABOVE",
                                    "BLOCK_LOW_AND_ABOVE",
                                ],
                            },
                            "dangerous_content": {
                                "description": t(
                                    "core-config-default-dangerous_content"
                                ),
                                "type": "string",
                                "hint": t("core-config-default-dangerous_content_hint"),
                                "options": [
                                    "BLOCK_NONE",
                                    "BLOCK_ONLY_HIGH",
                                    "BLOCK_MEDIUM_AND_ABOVE",
                                    "BLOCK_LOW_AND_ABOVE",
                                ],
                            },
                        },
                    },
                    "gm_thinking_config": {
                        "description": "Thinking Config",
                        "type": "object",
                        "items": {
                            "budget": {
                                "description": "Thinking Budget",
                                "type": "int",
                                "hint": "Guides the model on the specific number of thinking tokens to use for reasoning. See: https://ai.google.dev/gemini-api/docs/thinking#set-budget",
                            },
                            "level": {
                                "description": "Thinking Level",
                                "type": "string",
                                "hint": "Recommended for Gemini 3 models and onwards, lets you control reasoning behavior.See: https://ai.google.dev/gemini-api/docs/thinking#thinking-levels",
                                "options": [
                                    "MINIMAL",
                                    "LOW",
                                    "MEDIUM",
                                    "HIGH",
                                ],
                            },
                        },
                    },
                    "anth_thinking_config": {
                        "description": t("core-config-default-thinking_config"),
                        "type": "object",
                        "items": {
                            "type": {
                                "description": t("core-config-default-thinking_type"),
                                "type": "string",
                                "options": ["", "adaptive"],
                                "hint": t(
                                    "core-config-default-hint_adaptive_thinking_recommendation"
                                ),
                            },
                            "budget": {
                                "description": t(
                                    "core-config-default-desc_thinking_budget"
                                ),
                                "type": "int",
                                "hint": t(
                                    "core-config-default-hint_manual_budget_tokens"
                                ),
                            },
                            "effort": {
                                "description": t(
                                    "core-config-default-desc_thinking_effort"
                                ),
                                "type": "string",
                                "options": ["", "low", "medium", "high", "max"],
                                "hint": t(
                                    "core-config-default-hint_adaptive_effort_levels"
                                ),
                            },
                        },
                    },
                    "minimax-group-id": {
                        "type": "string",
                        "description": t("core-config-default-desc_user_group"),
                        "hint": t("core-config-default-hint_user_group_location"),
                    },
                    "minimax-langboost": {
                        "type": "string",
                        "description": t(
                            "core-config-default-desc_specified_language_dialect"
                        ),
                        "hint": t(
                            "core-config-default-hint_language_dialect_enhancement"
                        ),
                        "options": [
                            "Chinese",
                            "Chinese,Yue",
                            "English",
                            "Arabic",
                            "Russian",
                            "Spanish",
                            "French",
                            "Portuguese",
                            "German",
                            "Turkish",
                            "Dutch",
                            "Ukrainian",
                            "Vietnamese",
                            "Indonesian",
                            "Japanese",
                            "Italian",
                            "Korean",
                            "Thai",
                            "Polish",
                            "Romanian",
                            "Greek",
                            "Czech",
                            "Finnish",
                            "Hindi",
                            "auto",
                        ],
                    },
                    "minimax-voice-speed": {
                        "type": "float",
                        "description": t("core-config-default-desc_speech_rate"),
                        "hint": t("core-config-default-hint_speech_rate_range"),
                    },
                    "minimax-voice-vol": {
                        "type": "float",
                        "description": t("core-config-default-desc_volume"),
                        "hint": t("core-config-default-hint_volume_range"),
                    },
                    "minimax-voice-pitch": {
                        "type": "int",
                        "description": t("core-config-default-desc_pitch"),
                        "hint": t("core-config-default-hint_pitch_range"),
                    },
                    "minimax-is-timber-weight": {
                        "type": "bool",
                        "description": t(
                            "core-config-default-desc_enable_blended_voice"
                        ),
                        "hint": t(
                            "core-config-default-hint_enable_blended_voice_behavior"
                        ),
                    },
                    "minimax-timber-weight": {
                        "type": "string",
                        "description": t("core-config-default-desc_blended_voice"),
                        "editor_mode": True,
                        "hint": t(
                            "core-config-default-hint_blended_voice_weights_format"
                        ),
                    },
                    "minimax-voice-id": {
                        "type": "string",
                        "description": t("core-config-default-desc_single_voice"),
                        "hint": t("core-config-default-single_timbre_id_hint"),
                    },
                    "minimax-voice-emotion": {
                        "type": "string",
                        "description": t("core-config-default-emotion_description"),
                        "hint": t("core-config-default-emotion_control_hint"),
                        "options": [
                            "auto",
                            "happy",
                            "sad",
                            "angry",
                            "fearful",
                            "disgusted",
                            "surprised",
                            "calm",
                            "fluent",
                            "whisper",
                        ],
                    },
                    "minimax-voice-latex": {
                        "type": "bool",
                        "description": t(
                            "core-config-default-latex_support_description"
                        ),
                        "hint": t("core-config-default-latex_reading_hint"),
                    },
                    "minimax-voice-english-normalization": {
                        "type": "bool",
                        "description": t(
                            "core-config-default-english_normalization_description"
                        ),
                        "hint": t("core-config-default-english_normalization_hint"),
                    },
                    "rag_options": {
                        "description": t("core-config-default-rag_options_description"),
                        "type": "object",
                        "hint": t("core-config-default-rag_settings_hint"),
                        "items": {
                            "pipeline_ids": {
                                "description": t(
                                    "core-config-default-knowledge_base_id_list_description"
                                ),
                                "type": "list",
                                "items": {"type": "string"},
                                "hint": t(
                                    "core-config-default-knowledge_base_search_hint"
                                ),
                            },
                            "file_ids": {
                                "description": t(
                                    "core-config-default-unstructured_doc_id_description"
                                ),
                                "type": "list",
                                "items": {"type": "string"},
                                "hint": t(
                                    "core-config-default-unstructured_doc_search_hint"
                                ),
                            },
                            "output_reference": {
                                "description": t(
                                    "core-config-default-include_citations_description"
                                ),
                                "type": "bool",
                                "hint": t("core-config-default-citations_hint"),
                            },
                        },
                    },
                    "sensevoice_hint": {
                        "description": t(
                            "core-config-default-sensevoice_deployment_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-sensevoice_install_hint"),
                    },
                    "is_emotion": {
                        "description": t(
                            "core-config-default-emotion_recognition_description"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-emotion_recognition_hint"),
                    },
                    "stt_model": {
                        "description": t("core-config-default-model_name_description"),
                        "type": "string",
                        "hint": t("core-config-default-modelscope_model_name_hint"),
                    },
                    "variables": {
                        "description": t(
                            "core-config-default-workflow_fixed_input_vars_description"
                        ),
                        "type": "object",
                        "items": {},
                        "hint": t("core-config-default-workflow_fixed_input_vars_hint"),
                        "invisible": True,
                    },
                    "dashscope_app_type": {
                        "description": t("core-config-default-app_type_description"),
                        "type": "string",
                        "hint": t("core-config-default-bailian_app_type_hint"),
                        "options": [
                            "agent",
                            "agent-arrange",
                            "dialog-workflow",
                            "task-workflow",
                        ],
                    },
                    "timeout": {
                        "description": t("core-config-default-timeout_description"),
                        "type": "int",
                        "hint": t("core-config-default-timeout_seconds_hint"),
                    },
                    "openai-tts-voice": {
                        "description": "voice",
                        "type": "string",
                        "hint": t("core-config-default-openai_tts_voice_hint"),
                    },
                    "fishaudio-tts-character": {
                        "description": "character",
                        "type": "string",
                        "hint": t("core-config-default-fishaudio_tts_character_hint"),
                    },
                    "fishaudio-tts-reference-id": {
                        "description": "reference_id",
                        "type": "string",
                        "hint": t("core-config-default-fishaudio_tts_model_id_hint"),
                    },
                    "whisper_hint": {
                        "description": t(
                            "core-config-default-local_whisper_deployment_notes_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-whisper_installation_hint"),
                    },
                    "id": {
                        "description": "ID",
                        "type": "string",
                    },
                    "type": {
                        "description": t(
                            "core-config-default-model_provider_types_description"
                        ),
                        "type": "string",
                        "invisible": True,
                    },
                    "provider_type": {
                        "description": t(
                            "core-config-default-model_provider_capability_types_description"
                        ),
                        "type": "string",
                        "invisible": True,
                    },
                    "enable": {
                        "description": t("core-config-default-enable_description"),
                        "type": "bool",
                    },
                    "key": {
                        "description": "API Key",
                        "type": "list",
                        "items": {"type": "string"},
                    },
                    "api_base": {
                        "description": "API Base URL",
                        "type": "string",
                    },
                    "proxy": {
                        "description": t(
                            "core-config-default-proxy_address_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-proxy_address_hint"),
                    },
                    "model": {
                        "description": t("core-config-default-model_id_description"),
                        "type": "string",
                        "hint": t("core-config-default-model_id_hint"),
                    },
                    "max_context_tokens": {
                        "description": t(
                            "core-config-default-model_context_window_size_description"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-model_max_context_size_hint"),
                    },
                    "dify_api_key": {
                        "description": "API Key",
                        "type": "string",
                        "hint": t("core-config-default-dify_api_key_hint"),
                    },
                    "dify_api_base": {
                        "description": "API Base URL",
                        "type": "string",
                        "hint": t("core-config-default-dify_api_base_url_hint"),
                    },
                    "dify_api_type": {
                        "description": t(
                            "core-config-default-dify_app_type_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-dify_api_type_hint"),
                        "options": ["chat", "chatflow", "agent", "workflow"],
                    },
                    "dify_workflow_output_key": {
                        "description": t(
                            "core-config-default-dify_workflow_output_var_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-dify_workflow_output_var_hint"),
                    },
                    "dify_query_input_key": {
                        "description": t(
                            "core-config-default-prompt_input_var_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-prompt_input_var_hint"),
                        "obvious": True,
                    },
                    "coze_api_key": {
                        "description": "Coze API Key",
                        "type": "string",
                        "hint": t("core-config-default-coze_api_key_hint"),
                    },
                    "bot_id": {
                        "description": "Bot ID",
                        "type": "string",
                        "hint": t("core-config-default-coze_bot_id_hint"),
                    },
                    "coze_api_base": {
                        "description": "API Base URL",
                        "type": "string",
                        "hint": t("core-config-default-coze_api_base_url_hint"),
                    },
                    "auto_save_history": {
                        "description": t(
                            "core-config-default-coze_manage_conversation_description"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-coze_manage_conversation_hint"),
                    },
                },
            },
            "provider_settings": {
                "type": "object",
                "items": {
                    "enable": {
                        "type": "bool",
                    },
                    "default_provider_id": {
                        "type": "string",
                    },
                    "fallback_chat_models": {
                        "type": "list",
                        "items": {"type": "string"},
                    },
                    "wake_prefix": {
                        "type": "string",
                    },
                    "web_search": {
                        "type": "bool",
                    },
                    "web_search_link": {
                        "type": "bool",
                    },
                    "display_reasoning_text": {
                        "type": "bool",
                    },
                    "identifier": {
                        "type": "bool",
                    },
                    "group_name_display": {
                        "type": "bool",
                    },
                    "datetime_system_prompt": {
                        "type": "bool",
                    },
                    "default_personality": {
                        "type": "string",
                    },
                    "prompt_prefix": {
                        "type": "string",
                    },
                    "max_context_length": {
                        "type": "int",
                    },
                    "dequeue_context_length": {
                        "type": "int",
                    },
                    "streaming_response": {
                        "type": "bool",
                    },
                    "show_tool_use_status": {
                        "type": "bool",
                    },
                    "unsupported_streaming_strategy": {
                        "type": "string",
                    },
                    "agent_runner_type": {
                        "type": "string",
                    },
                    "dify_agent_runner_provider_id": {
                        "type": "string",
                    },
                    "coze_agent_runner_provider_id": {
                        "type": "string",
                    },
                    "dashscope_agent_runner_provider_id": {
                        "type": "string",
                    },
                    "max_agent_step": {
                        "type": "int",
                    },
                    "tool_call_timeout": {
                        "type": "int",
                    },
                    "tool_schema_mode": {
                        "type": "string",
                    },
                    "file_extract": {
                        "type": "object",
                        "items": {
                            "enable": {
                                "type": "bool",
                            },
                            "provider": {
                                "type": "string",
                            },
                            "moonshotai_api_key": {
                                "type": "string",
                            },
                        },
                    },
                    "proactive_capability": {
                        "type": "object",
                        "items": {
                            "add_cron_tools": {
                                "type": "bool",
                            },
                        },
                    },
                },
            },
            "provider_stt_settings": {
                "type": "object",
                "items": {
                    "enable": {
                        "type": "bool",
                    },
                    "provider_id": {
                        "type": "string",
                    },
                },
            },
            "provider_tts_settings": {
                "type": "object",
                "items": {
                    "enable": {
                        "type": "bool",
                    },
                    "provider_id": {
                        "type": "string",
                    },
                    "dual_output": {
                        "type": "bool",
                    },
                    "use_file_service": {
                        "type": "bool",
                    },
                    "trigger_probability": {
                        "type": "float",
                    },
                },
            },
            "provider_ltm_settings": {
                "type": "object",
                "items": {
                    "group_icl_enable": {
                        "type": "bool",
                    },
                    "group_message_max_cnt": {
                        "type": "int",
                    },
                    "image_caption": {
                        "type": "bool",
                    },
                    "image_caption_provider_id": {
                        "type": "string",
                    },
                    "image_caption_prompt": {
                        "type": "string",
                    },
                    "active_reply": {
                        "type": "object",
                        "items": {
                            "enable": {
                                "type": "bool",
                            },
                            "whitelist": {
                                "type": "list",
                                "items": {"type": "string"},
                            },
                            "method": {
                                "type": "string",
                                "options": ["possibility_reply"],
                            },
                            "possibility_reply": {
                                "type": "float",
                            },
                        },
                    },
                },
            },
        },
    },
    "misc_config_group": {
        "metadata": {
            "wake_prefix": {
                "type": "list",
                "items": {"type": "string"},
            },
            "t2i": {
                "type": "bool",
            },
            "t2i_word_threshold": {
                "type": "int",
            },
            "admins_id": {
                "type": "list",
                "items": {"type": "string"},
            },
            "http_proxy": {
                "type": "string",
            },
            "no_proxy": {
                "description": t(
                    "core-config-default-direct_connection_list_description"
                ),
                "type": "list",
                "items": {"type": "string"},
                "hint": t("core-config-default-direct_connection_list_hint"),
            },
            "timezone": {
                "type": "string",
            },
            "callback_api_base": {
                "type": "string",
            },
            "log_level": {
                "type": "string",
                "options": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
            },
            "dashboard.ssl.enable": {"type": "bool"},
            "dashboard.ssl.cert_file": {
                "type": "string",
                "condition": {"dashboard.ssl.enable": True},
            },
            "dashboard.ssl.key_file": {
                "type": "string",
                "condition": {"dashboard.ssl.enable": True},
            },
            "dashboard.ssl.ca_certs": {
                "type": "string",
                "condition": {"dashboard.ssl.enable": True},
            },
            "log_file_enable": {"type": "bool"},
            "log_file_path": {"type": "string", "condition": {"log_file_enable": True}},
            "log_file_max_mb": {"type": "int", "condition": {"log_file_enable": True}},
            "temp_dir_max_size": {"type": "int"},
            "trace_log_enable": {"type": "bool"},
            "trace_log_path": {
                "type": "string",
                "condition": {"trace_log_enable": True},
            },
            "trace_log_max_mb": {
                "type": "int",
                "condition": {"trace_log_enable": True},
            },
            "t2i_strategy": {
                "type": "string",
                "options": ["remote", "local"],
            },
            "t2i_endpoint": {
                "type": "string",
            },
            "t2i_use_file_service": {
                "type": "bool",
            },
            "pip_install_arg": {
                "type": "string",
            },
            "pypi_index_url": {
                "type": "string",
            },
            "default_kb_collection": {
                "type": "string",
            },
            "kb_names": {"type": "list", "items": {"type": "string"}},
            "kb_fusion_top_k": {"type": "int", "default": 20},
            "kb_final_top_k": {"type": "int", "default": 5},
            "kb_agentic_mode": {"type": "bool"},
        },
    },
}


"""
v4.7.0 之后，name, description, hint 等字段已经实现 i18n 国际化。国际化资源文件位于：

- dashboard/src/i18n/locales/en-US/features/config-metadata.json
- dashboard/src/i18n/locales/zh-CN/features/config-metadata.json

如果在此文件中添加了新的配置字段，请务必同步更新上述两个国际化资源文件。
"""
CONFIG_METADATA_3 = {
    "ai_group": {
        "name": t("core-config-default-ai_config_name"),
        "metadata": {
            "agent_runner": {
                "description": t(
                    "core-config-default-agent_execution_mode_description"
                ),
                "hint": t("core-config-default-agent_execution_mode_hint"),
                "type": "object",
                "items": {
                    "provider_settings.enable": {
                        "description": t("core-config-default-enable_description"),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-ai_conversation_master_switch_hint"
                        ),
                    },
                    "provider_settings.agent_runner_type": {
                        "description": t("core-config-default-executor_description"),
                        "type": "string",
                        "options": ["local", "dify", "coze", "dashscope"],
                        "labels": [
                            t("core-config-default-agent_provider_labels-part1"),
                            "Dify",
                            "Coze",
                            t("core-config-default-agent_provider_labels-part2"),
                        ],
                        "condition": {
                            "provider_settings.enable": True,
                        },
                    },
                    "provider_settings.coze_agent_runner_provider_id": {
                        "description": t(
                            "core-config-default-coze_agent_provider_id_description"
                        ),
                        "type": "string",
                        "_special": "select_agent_runner_provider:coze",
                        "condition": {
                            "provider_settings.agent_runner_type": "coze",
                            "provider_settings.enable": True,
                        },
                    },
                    "provider_settings.dify_agent_runner_provider_id": {
                        "description": t(
                            "core-config-default-dify_agent_provider_id_description"
                        ),
                        "type": "string",
                        "_special": "select_agent_runner_provider:dify",
                        "condition": {
                            "provider_settings.agent_runner_type": "dify",
                            "provider_settings.enable": True,
                        },
                    },
                    "provider_settings.dashscope_agent_runner_provider_id": {
                        "description": t(
                            "core-config-default-bailian_agent_provider_id_description"
                        ),
                        "type": "string",
                        "_special": "select_agent_runner_provider:dashscope",
                        "condition": {
                            "provider_settings.agent_runner_type": "dashscope",
                            "provider_settings.enable": True,
                        },
                    },
                },
            },
            "ai": {
                "description": t("core-config-default-model_description"),
                "hint": t("core-config-default-non_builtin_model_fallback_hint"),
                "type": "object",
                "items": {
                    "provider_settings.default_provider_id": {
                        "description": t(
                            "core-config-default-default_conversation_model_description"
                        ),
                        "type": "string",
                        "_special": "select_provider",
                        "hint": t("core-config-default-default_model_fallback_hint"),
                    },
                    "provider_settings.fallback_chat_models": {
                        "description": t(
                            "core-config-default-fallback_conversation_models_description"
                        ),
                        "type": "list",
                        "items": {"type": "string"},
                        "_special": "select_providers",
                        "hint": t("core-config-default-fallback_models_switch_hint"),
                    },
                    "provider_settings.default_image_caption_provider_id": {
                        "description": t(
                            "core-config-default-default_image_caption_model_description"
                        ),
                        "type": "string",
                        "_special": "select_provider",
                        "hint": t("core-config-default-image_caption_blank_hint"),
                    },
                    "provider_stt_settings.enable": {
                        "description": t("core-config-default-enable_stt_description"),
                        "type": "bool",
                        "hint": t("core-config-default-stt_master_switch_hint"),
                    },
                    "provider_stt_settings.provider_id": {
                        "description": t(
                            "core-config-default-default_stt_model_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-stt_per_session_hint"),
                        "_special": "select_provider_stt",
                        "condition": {
                            "provider_stt_settings.enable": True,
                        },
                    },
                    "provider_tts_settings.enable": {
                        "description": t("core-config-default-enable_tts_description"),
                        "type": "bool",
                        "hint": t("core-config-default-tts_master_switch_hint"),
                    },
                    "provider_tts_settings.provider_id": {
                        "description": t("core-config-default-tts_default_model"),
                        "type": "string",
                        "_special": "select_provider_tts",
                        "condition": {
                            "provider_tts_settings.enable": True,
                        },
                    },
                    "provider_tts_settings.trigger_probability": {
                        "description": t("core-config-default-tts_trigger_probability"),
                        "type": "float",
                        "slider": {"min": 0, "max": 1, "step": 0.05},
                        "condition": {
                            "provider_tts_settings.enable": True,
                        },
                    },
                    "provider_settings.image_caption_prompt": {
                        "description": t("core-config-default-image_to_text_prompt"),
                        "type": "text",
                    },
                },
                "condition": {
                    "provider_settings.enable": True,
                },
            },
            "persona": {
                "description": t("core-config-default-persona"),
                "hint": "",
                "type": "object",
                "items": {
                    "provider_settings.default_personality": {
                        "description": t("core-config-default-default_persona"),
                        "type": "string",
                        "_special": "select_persona",
                    },
                },
                "condition": {
                    "provider_settings.agent_runner_type": "local",
                    "provider_settings.enable": True,
                },
            },
            "knowledgebase": {
                "description": t("core-config-default-knowledge_base"),
                "hint": "",
                "type": "object",
                "items": {
                    "kb_names": {
                        "description": t("core-config-default-knowledge_base_list"),
                        "type": "list",
                        "items": {"type": "string"},
                        "_special": "select_knowledgebase",
                        "hint": t("core-config-default-multi_select_supported"),
                    },
                    "kb_fusion_top_k": {
                        "description": t("core-config-default-merged_retrieval_count"),
                        "type": "int",
                        "hint": t("core-config-default-merged_result_count_hint"),
                    },
                    "kb_final_top_k": {
                        "description": t("core-config-default-final_result_count"),
                        "type": "int",
                        "hint": t("core-config-default-retrieval_count_hint"),
                    },
                    "kb_agentic_mode": {
                        "description": t("core-config-default-agentic_kb_retrieval"),
                        "type": "bool",
                        "hint": t("core-config-default-agentic_retrieval_hint"),
                    },
                },
                "condition": {
                    "provider_settings.agent_runner_type": "local",
                    "provider_settings.enable": True,
                },
            },
            "websearch": {
                "description": t("core-config-default-web_search"),
                "hint": "",
                "type": "object",
                "items": {
                    "provider_settings.web_search": {
                        "description": t("core-config-default-enable_web_search"),
                        "type": "bool",
                    },
                    "provider_settings.websearch_provider": {
                        "description": t("core-config-default-web_search_provider"),
                        "type": "string",
                        "options": ["default", "tavily", "baidu_ai_search", "bocha"],
                        "condition": {
                            "provider_settings.web_search": True,
                        },
                    },
                    "provider_settings.websearch_tavily_key": {
                        "description": "Tavily API Key",
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t("core-config-default-api_key_rotation_hint"),
                        "condition": {
                            "provider_settings.websearch_provider": "tavily",
                            "provider_settings.web_search": True,
                        },
                    },
                    "provider_settings.websearch_bocha_key": {
                        "description": "BoCha API Key",
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t("core-config-default-api_key_rotation_hint"),
                        "condition": {
                            "provider_settings.websearch_provider": "bocha",
                            "provider_settings.web_search": True,
                        },
                    },
                    "provider_settings.websearch_baidu_app_builder_key": {
                        "description": t(
                            "core-config-default-baidu_qianfan_app_builder_api_key"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-hint_baidu_apikey_reference"),
                        "condition": {
                            "provider_settings.websearch_provider": "baidu_ai_search",
                        },
                    },
                    "provider_settings.web_search_link": {
                        "description": t(
                            "core-config-default-description_show_source_citations"
                        ),
                        "type": "bool",
                        "condition": {
                            "provider_settings.web_search": True,
                        },
                    },
                },
                "condition": {
                    "provider_settings.agent_runner_type": "local",
                    "provider_settings.enable": True,
                },
            },
            "agent_computer_use": {
                "description": "Agent Computer Use",
                "hint": "",
                "type": "object",
                "items": {
                    "provider_settings.computer_use_runtime": {
                        "description": "Computer Use Runtime",
                        "type": "string",
                        "options": ["none", "local", "sandbox"],
                        "labels": [
                            t("core-config-default-execution_mode_labels-part1"),
                            t("core-config-default-execution_mode_labels-part2"),
                            t("core-config-default-execution_mode_labels-part3"),
                        ],
                        "hint": t("core-config-default-hint_computer_use_environment"),
                    },
                    "provider_settings.computer_use_require_admin": {
                        "description": t(
                            "core-config-default-description_requires_admin_privileges"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-hint_computer_use_admin_requirement"
                        ),
                    },
                    "provider_settings.sandbox.booter": {
                        "description": t(
                            "core-config-default-description_sandbox_driver"
                        ),
                        "type": "string",
                        "options": ["shipyard"],
                        "labels": ["Shipyard"],
                        "condition": {
                            "provider_settings.computer_use_runtime": "sandbox",
                        },
                    },
                    "provider_settings.sandbox.shipyard_endpoint": {
                        "description": "Shipyard API Endpoint",
                        "type": "string",
                        "hint": t("core-config-default-hint_shipyard_api_address"),
                        "condition": {
                            "provider_settings.computer_use_runtime": "sandbox",
                            "provider_settings.sandbox.booter": "shipyard",
                        },
                        "_special": "check_shipyard_connection",
                    },
                    "provider_settings.sandbox.shipyard_access_token": {
                        "description": "Shipyard Access Token",
                        "type": "string",
                        "hint": t("core-config-default-hint_shipyard_access_token"),
                        "condition": {
                            "provider_settings.computer_use_runtime": "sandbox",
                            "provider_settings.sandbox.booter": "shipyard",
                        },
                    },
                    "provider_settings.sandbox.shipyard_ttl": {
                        "description": "Shipyard Session TTL",
                        "type": "int",
                        "hint": t("core-config-default-hint_shipyard_session_ttl"),
                        "condition": {
                            "provider_settings.computer_use_runtime": "sandbox",
                            "provider_settings.sandbox.booter": "shipyard",
                        },
                    },
                    "provider_settings.sandbox.shipyard_max_sessions": {
                        "description": "Shipyard Max Sessions",
                        "type": "int",
                        "hint": t("core-config-default-hint_shipyard_max_sessions"),
                        "condition": {
                            "provider_settings.computer_use_runtime": "sandbox",
                            "provider_settings.sandbox.booter": "shipyard",
                        },
                    },
                },
                "condition": {
                    "provider_settings.agent_runner_type": "local",
                    "provider_settings.enable": True,
                },
            },
            # "file_extract": {
            #     "description": "文档解析能力 [beta]",
            #     "type": "object",
            #     "items": {
            #         "provider_settings.file_extract.enable": {
            #             "description": "启用文档解析能力",
            #             "type": "bool",
            #         },
            #         "provider_settings.file_extract.provider": {
            #             "description": "文档解析提供商",
            #             "type": "string",
            #             "options": ["moonshotai"],
            #             "condition": {
            #                 "provider_settings.file_extract.enable": True,
            #             },
            #         },
            #         "provider_settings.file_extract.moonshotai_api_key": {
            #             "description": "Moonshot AI API Key",
            #             "type": "string",
            #             "condition": {
            #                 "provider_settings.file_extract.provider": "moonshotai",
            #                 "provider_settings.file_extract.enable": True,
            #             },
            #         },
            #     },
            #     "condition": {
            #         "provider_settings.agent_runner_type": "local",
            #         "provider_settings.enable": True,
            #     },
            # },
            "proactive_capability": {
                "description": t("core-config-default-description_proactive_agent"),
                "hint": "https://docs.astrbot.app/use/proactive-agent.html",
                "type": "object",
                "items": {
                    "provider_settings.proactive_capability.add_cron_tools": {
                        "description": t("core-config-default-description_enable"),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-hint_proactive_agent_explanation"
                        ),
                    },
                },
                "condition": {
                    "provider_settings.agent_runner_type": "local",
                    "provider_settings.enable": True,
                },
            },
            "truncate_and_compress": {
                "hint": "",
                "description": t(
                    "core-config-default-description_context_management_strategy"
                ),
                "type": "object",
                "items": {
                    "provider_settings.max_context_length": {
                        "description": t(
                            "core-config-default-description_max_conversation_turns"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-hint_max_turns_explanation"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.dequeue_context_length": {
                        "description": t(
                            "core-config-default-description_turns_to_drop"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-hint_drop_turns_explanation"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.context_limit_reached_strategy": {
                        "description": t(
                            "core-config-default-description_context_window_overflow_handling"
                        ),
                        "type": "string",
                        "options": ["truncate_by_turns", "llm_compress"],
                        "labels": [
                            t("core-config-default-context_truncation_labels-part1"),
                            t("core-config-default-context_truncation_labels-part2"),
                        ],
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                        "hint": "",
                    },
                    "provider_settings.llm_compress_instruction": {
                        "description": t(
                            "core-config-default-context_compression_prompt"
                        ),
                        "type": "text",
                        "hint": t("core-config-default-compression_prompt_hint"),
                        "condition": {
                            "provider_settings.context_limit_reached_strategy": "llm_compress",
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.llm_compress_keep_recent": {
                        "description": t("core-config-default-preserve_recent_turns"),
                        "type": "int",
                        "hint": t("core-config-default-preserve_recent_turns_hint"),
                        "condition": {
                            "provider_settings.context_limit_reached_strategy": "llm_compress",
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.llm_compress_provider_id": {
                        "description": t(
                            "core-config-default-compression_model_provider"
                        ),
                        "type": "string",
                        "_special": "select_provider",
                        "hint": t(
                            "core-config-default-compression_provider_fallback_hint"
                        ),
                        "condition": {
                            "provider_settings.context_limit_reached_strategy": "llm_compress",
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                },
                "condition": {
                    "provider_settings.agent_runner_type": "local",
                    "provider_settings.enable": True,
                },
            },
            "others": {
                "description": t("core-config-default-other_settings"),
                "type": "object",
                "items": {
                    "provider_settings.display_reasoning_text": {
                        "description": t("core-config-default-show_thinking_content"),
                        "type": "bool",
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.streaming_response": {
                        "description": t("core-config-default-streaming_output"),
                        "type": "bool",
                    },
                    "provider_settings.unsupported_streaming_strategy": {
                        "description": t("core-config-default-non_streaming_platforms"),
                        "type": "string",
                        "options": ["realtime_segmenting", "turn_off"],
                        "hint": t("core-config-default-non_streaming_handling_hint"),
                        "labels": [
                            t("core-config-default-streaming_reply_labels-part1"),
                            t("core-config-default-streaming_reply_labels-part2"),
                        ],
                        "condition": {
                            "provider_settings.streaming_response": True,
                        },
                    },
                    "provider_settings.llm_safety_mode": {
                        "description": t("core-config-default-safe_mode"),
                        "type": "bool",
                        "hint": t("core-config-default-safe_mode_hint"),
                    },
                    "provider_settings.safety_mode_strategy": {
                        "description": t("core-config-default-safe_mode_strategy"),
                        "type": "string",
                        "options": ["system_prompt"],
                        "hint": t("core-config-default-safe_mode_strategy_hint"),
                        "condition": {
                            "provider_settings.llm_safety_mode": True,
                        },
                    },
                    "provider_settings.identifier": {
                        "description": t("core-config-default-user_identification"),
                        "type": "bool",
                        "hint": t("core-config-default-user_id_in_prompt_hint"),
                    },
                    "provider_settings.group_name_display": {
                        "description": t("core-config-default-show_group_name"),
                        "type": "bool",
                        "hint": t("core-config-default-group_name_in_prompt"),
                    },
                    "provider_settings.datetime_system_prompt": {
                        "description": t(
                            "core-config-default-real_world_time_awareness"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-append_current_time_to_prompt"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.show_tool_use_status": {
                        "description": t(
                            "core-config-default-output_function_call_status"
                        ),
                        "type": "bool",
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.sanitize_context_by_modalities": {
                        "description": t(
                            "core-config-default-clean_history_by_model_capability"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-prune_unsupported_content_by_model"
                        ),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.max_quoted_fallback_images": {
                        "description": t(
                            "core-config-default-quoted_image_fallback_limit"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-quoted_image_injection_max"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.quoted_message_parser.max_component_chain_depth": {
                        "description": t("core-config-default-reply_chain_max_depth"),
                        "type": "int",
                        "hint": t("core-config-default-reply_chain_recursion_limit"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.quoted_message_parser.max_forward_node_depth": {
                        "description": t(
                            "core-config-default-forwarded_node_max_depth"
                        ),
                        "type": "int",
                        "hint": t("core-config-default-forwarded_node_recursion_limit"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.quoted_message_parser.max_forward_fetch": {
                        "description": t(
                            "core-config-default-forwarded_msg_fetch_limit"
                        ),
                        "type": "int",
                        "hint": t(
                            "core-config-default-forwarded_msg_recursive_fetch_max"
                        ),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.quoted_message_parser.warn_on_action_failure": {
                        "description": t(
                            "core-config-default-alert_on_quoted_parse_failure"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-warn_on_all_msg_fetch_failure"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.max_agent_step": {
                        "description": t("core-config-default-tool_call_round_limit"),
                        "type": "int",
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.tool_call_timeout": {
                        "description": t(
                            "core-config-default-tool_call_timeout_seconds"
                        ),
                        "type": "int",
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.tool_schema_mode": {
                        "description": t("core-config-default-tool_call_mode"),
                        "type": "string",
                        "options": ["skills_like", "full"],
                        "labels": [
                            t("core-config-default-function_calling_mode_labels-part1"),
                            t("core-config-default-function_calling_mode_labels-part2"),
                        ],
                        "hint": t("core-config-default-llm_tool_calling_mode_hint"),
                        "condition": {
                            "provider_settings.agent_runner_type": "local",
                        },
                    },
                    "provider_settings.wake_prefix": {
                        "description": t(
                            "core-config-default-llm_chat_wakeup_prefix_description"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-llm_chat_wakeup_prefix_hint"),
                    },
                    "provider_settings.prompt_prefix": {
                        "description": t("core-config-default-user_prompt_description"),
                        "type": "string",
                        "hint": t("core-config-default-prompt_placeholder_hint"),
                    },
                    "provider_tts_settings.dual_output": {
                        "description": t(
                            "core-config-default-tts_output_both_description"
                        ),
                        "type": "bool",
                    },
                    "provider_settings.reachability_check": {
                        "description": t(
                            "core-config-default-provider_reachability_check_description"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-provider_reachability_concurrent_hint"
                        ),
                    },
                },
                "condition": {
                    "provider_settings.enable": True,
                },
            },
        },
    },
    "platform_group": {
        "name": t("core-config-default-platform_config_name"),
        "metadata": {
            "general": {
                "description": t("core-config-default-basic_section_description"),
                "type": "object",
                "items": {
                    "admins_id": {
                        "description": t("core-config-default-admin_id_description"),
                        "type": "list",
                        "items": {"type": "string"},
                    },
                    "platform_settings.unique_session": {
                        "description": t(
                            "core-config-default-isolate_sessions_description"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-isolate_sessions_hint"),
                    },
                    "wake_prefix": {
                        "description": t("core-config-default-wake_word_description"),
                        "type": "list",
                        "items": {"type": "string"},
                    },
                    "platform_settings.friend_message_needs_wake_prefix": {
                        "description": t(
                            "core-config-default-private_chat_require_wake_word_description"
                        ),
                        "type": "bool",
                    },
                    "platform_settings.reply_prefix": {
                        "description": t(
                            "core-config-default-reply_text_prefix_description"
                        ),
                        "type": "string",
                    },
                    "platform_settings.reply_with_mention": {
                        "description": t(
                            "core-config-default-reply_at_sender_description"
                        ),
                        "type": "bool",
                    },
                    "platform_settings.reply_with_quote": {
                        "description": t(
                            "core-config-default-reply_quote_message_description"
                        ),
                        "type": "bool",
                    },
                    "platform_settings.forward_threshold": {
                        "description": t(
                            "core-config-default-forward_message_word_threshold_description"
                        ),
                        "type": "int",
                    },
                    "platform_settings.empty_mention_waiting": {
                        "description": t(
                            "core-config-default-mention_only_bot_triggers_wait_description"
                        ),
                        "type": "bool",
                    },
                    "disable_builtin_commands": {
                        "description": t(
                            "core-config-default-disable_builtin_commands"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-hint_disable_all_builtin"),
                    },
                },
            },
            "whitelist": {
                "description": t("core-config-default-whitelist"),
                "type": "object",
                "items": {
                    "platform_settings.enable_id_white_list": {
                        "description": t("core-config-default-enable_whitelist"),
                        "type": "bool",
                        "hint": t("core-config-default-hint_whitelist_only"),
                    },
                    "platform_settings.id_whitelist": {
                        "description": t("core-config-default-whitelist_id_list"),
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t("core-config-default-hint_use_sid_get_id"),
                    },
                    "platform_settings.id_whitelist_log": {
                        "description": t("core-config-default-output_log"),
                        "type": "bool",
                        "hint": t("core-config-default-hint_log_on_whitelist_fail"),
                    },
                    "platform_settings.wl_ignore_admin_on_group": {
                        "description": t(
                            "core-config-default-admin_group_ignore_whitelist"
                        ),
                        "type": "bool",
                    },
                    "platform_settings.wl_ignore_admin_on_friend": {
                        "description": t(
                            "core-config-default-admin_private_ignore_whitelist"
                        ),
                        "type": "bool",
                    },
                },
            },
            "rate_limit": {
                "description": t("core-config-default-rate_limit"),
                "type": "object",
                "items": {
                    "platform_settings.rate_limit.time": {
                        "description": t("core-config-default-rate_limit_time_seconds"),
                        "type": "int",
                    },
                    "platform_settings.rate_limit.count": {
                        "description": t("core-config-default-rate_limit_count"),
                        "type": "int",
                    },
                    "platform_settings.rate_limit.strategy": {
                        "description": t("core-config-default-rate_limit_strategy"),
                        "type": "string",
                        "options": ["stall", "discard"],
                    },
                },
            },
            "content_safety": {
                "description": t("core-config-default-content_safety"),
                "type": "object",
                "items": {
                    "content_safety.also_use_in_response": {
                        "description": t("core-config-default-check_model_response"),
                        "type": "bool",
                    },
                    "content_safety.baidu_aip.enable": {
                        "description": t(
                            "core-config-default-use_baidu_content_safety"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-hint_install_baidu_aip"),
                    },
                    "content_safety.baidu_aip.app_id": {
                        "description": "App ID",
                        "type": "string",
                        "condition": {
                            "content_safety.baidu_aip.enable": True,
                        },
                    },
                    "content_safety.baidu_aip.api_key": {
                        "description": "API Key",
                        "type": "string",
                        "condition": {
                            "content_safety.baidu_aip.enable": True,
                        },
                    },
                    "content_safety.baidu_aip.secret_key": {
                        "description": "Secret Key",
                        "type": "string",
                        "condition": {
                            "content_safety.baidu_aip.enable": True,
                        },
                    },
                    "content_safety.internal_keywords.enable": {
                        "description": t("core-config-default-keyword_check"),
                        "type": "bool",
                    },
                    "content_safety.internal_keywords.extra_keywords": {
                        "description": t("core-config-default-additional_keywords"),
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t(
                            "core-config-default-additional_blocked_keywords_hint"
                        ),
                    },
                },
            },
            "t2i": {
                "description": t("core-config-default-text_to_image"),
                "type": "object",
                "items": {
                    "t2i": {
                        "description": t("core-config-default-text_to_image_output"),
                        "type": "bool",
                    },
                    "t2i_word_threshold": {
                        "description": t(
                            "core-config-default-text_to_image_char_threshold"
                        ),
                        "type": "int",
                    },
                },
            },
            "others": {
                "description": t("core-config-default-other_settings"),
                "type": "object",
                "items": {
                    "platform_settings.ignore_bot_self_message": {
                        "description": t("core-config-default-ignore_bot_own_messages"),
                        "type": "bool",
                    },
                    "platform_settings.ignore_at_all": {
                        "description": t(
                            "core-config-default-ignore_mention_all_events"
                        ),
                        "type": "bool",
                    },
                    "platform_settings.no_permission_reply": {
                        "description": t(
                            "core-config-default-reply_on_insufficient_permission"
                        ),
                        "type": "bool",
                    },
                    "platform_specific.lark.pre_ack_emoji.enable": {
                        "description": t(
                            "core-config-default-feishu_enable_pre_response_reactions"
                        ),
                        "type": "bool",
                    },
                    "platform_specific.lark.pre_ack_emoji.emojis": {
                        "description": t("core-config-default-feishu_reaction_list"),
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t("core-config-default-feishu_emoji_reference_hint"),
                        "condition": {
                            "platform_specific.lark.pre_ack_emoji.enable": True,
                        },
                    },
                    "platform_specific.telegram.pre_ack_emoji.enable": {
                        "description": t(
                            "core-config-default-telegram_enable_pre_response_reactions"
                        ),
                        "type": "bool",
                    },
                    "platform_specific.telegram.pre_ack_emoji.emojis": {
                        "description": t("core-config-default-telegram_reaction_list"),
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t(
                            "core-config-default-telegram_reaction_reference_hint"
                        ),
                        "condition": {
                            "platform_specific.telegram.pre_ack_emoji.enable": True,
                        },
                    },
                },
            },
        },
    },
    "plugin_group": {
        "name": t("core-config-default-plugin_configuration"),
        "metadata": {
            "plugin": {
                "description": t("core-config-default-plugins"),
                "type": "object",
                "items": {
                    "plugin_set": {
                        "description": t("core-config-default-available_plugins"),
                        "type": "bool",
                        "hint": t("core-config-default-available_plugins_hint"),
                        "_special": "select_plugin_set",
                    },
                },
            },
        },
    },
    "ext_group": {
        "name": t("core-config-default-extended_features"),
        "metadata": {
            "segmented_reply": {
                "description": t("core-config-default-segmented_replies"),
                "type": "object",
                "items": {
                    "platform_settings.segmented_reply.enable": {
                        "description": t(
                            "core-config-default-enable_segmented_replies"
                        ),
                        "type": "bool",
                    },
                    "platform_settings.segmented_reply.only_llm_result": {
                        "description": t(
                            "core-config-default-segment_llm_results_only"
                        ),
                        "type": "bool",
                    },
                    "platform_settings.segmented_reply.interval_method": {
                        "description": t("core-config-default-interval_method"),
                        "hint": t("core-config-default-interval_method_hint"),
                        "type": "string",
                        "options": ["random", "log"],
                    },
                    "platform_settings.segmented_reply.interval": {
                        "description": t("core-config-default-random_interval"),
                        "type": "string",
                        "hint": t("core-config-default-random_interval_format"),
                        "condition": {
                            "platform_settings.segmented_reply.interval_method": "random",
                        },
                    },
                    "platform_settings.segmented_reply.log_base": {
                        "description": t("core-config-default-log_base"),
                        "type": "float",
                        "hint": t("core-config-default-log_base_hint"),
                        "condition": {
                            "platform_settings.segmented_reply.interval_method": "log",
                        },
                    },
                    "platform_settings.segmented_reply.words_count_threshold": {
                        "description": t(
                            "core-config-default-segment_character_threshold"
                        ),
                        "hint": t("core-config-default-segment_threshold_hint"),
                        "type": "int",
                    },
                    "platform_settings.segmented_reply.split_mode": {
                        "description": t("core-config-default-segmentation_mode"),
                        "type": "string",
                        "options": ["regex", "words"],
                        "labels": [
                            t("core-config-default-blocking_rule_type_labels-part1"),
                            t("core-config-default-blocking_rule_type_labels-part2"),
                        ],
                    },
                    "platform_settings.segmented_reply.regex": {
                        "description": t("core-config-default-segment_regex"),
                        "hint": t("core-config-default-segment_regex_hint"),
                        "type": "string",
                        "condition": {
                            "platform_settings.segmented_reply.split_mode": "regex",
                        },
                    },
                    "platform_settings.segmented_reply.split_words": {
                        "description": t("core-config-default-segment_word_list"),
                        "type": "list",
                        "hint": t("core-config-default-segment_word_list_hint"),
                        "condition": {
                            "platform_settings.segmented_reply.split_mode": "words",
                        },
                    },
                    "platform_settings.segmented_reply.content_cleanup_rule": {
                        "description": t("core-config-default-content_filter_regex"),
                        "type": "string",
                        "hint": t("core-config-default-content_filter_hint"),
                    },
                },
            },
            "ltm": {
                "description": t("core-config-default-group_context_awareness"),
                "type": "object",
                "items": {
                    "provider_ltm_settings.group_icl_enable": {
                        "description": t(
                            "core-config-default-enable_group_context_awareness"
                        ),
                        "type": "bool",
                    },
                    "provider_ltm_settings.group_message_max_cnt": {
                        "description": t("core-config-default-max_message_count"),
                        "type": "int",
                    },
                    "provider_ltm_settings.image_caption": {
                        "description": t("core-config-default-auto_understand_images"),
                        "type": "bool",
                        "hint": t("core-config-default-group_image_model_required"),
                    },
                    "provider_ltm_settings.image_caption_provider_id": {
                        "description": t(
                            "core-config-default-group_image_caption_model"
                        ),
                        "type": "string",
                        "_special": "select_provider",
                        "hint": t("core-config-default-group_image_model_description"),
                        "condition": {
                            "provider_ltm_settings.image_caption": True,
                        },
                    },
                    "provider_ltm_settings.active_reply.enable": {
                        "description": t("core-config-default-proactive_reply"),
                        "type": "bool",
                    },
                    "provider_ltm_settings.active_reply.method": {
                        "description": t("core-config-default-proactive_reply_method"),
                        "type": "string",
                        "options": ["possibility_reply"],
                        "condition": {
                            "provider_ltm_settings.active_reply.enable": True,
                        },
                    },
                    "provider_ltm_settings.active_reply.possibility_reply": {
                        "description": t("core-config-default-reply_probability"),
                        "type": "float",
                        "hint": t("core-config-default-reply_probability_hint"),
                        "slider": {"min": 0, "max": 1, "step": 0.05},
                        "condition": {
                            "provider_ltm_settings.active_reply.enable": True,
                        },
                    },
                    "provider_ltm_settings.active_reply.whitelist": {
                        "description": t(
                            "core-config-default-proactive_reply_whitelist"
                        ),
                        "type": "list",
                        "items": {"type": "string"},
                        "hint": t("core-config-default-proactive_whitelist_hint"),
                        "condition": {
                            "provider_ltm_settings.active_reply.enable": True,
                        },
                    },
                },
            },
        },
    },
}

CONFIG_METADATA_3_SYSTEM = {
    "system_group": {
        "name": t("core-config-default-system_configuration_name"),
        "metadata": {
            "system": {
                "description": t("core-config-default-system_configuration_desc"),
                "type": "object",
                "items": {
                    "t2i_strategy": {
                        "description": t("core-config-default-text_to_image_strategy"),
                        "type": "string",
                        "hint": t("core-config-default-text_to_image_strategy_hint"),
                        "options": ["remote", "local"],
                    },
                    "t2i_endpoint": {
                        "description": t(
                            "core-config-default-text_to_image_api_address"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-text_to_image_api_hint"),
                        "condition": {
                            "t2i_strategy": "remote",
                        },
                    },
                    "t2i_template": {
                        "description": t(
                            "core-config-default-text_to_image_custom_template"
                        ),
                        "type": "bool",
                        "hint": t(
                            "core-config-default-text_to_image_custom_template_hint"
                        ),
                        "condition": {
                            "t2i_strategy": "remote",
                        },
                        "_special": "t2i_template",
                    },
                    "t2i_active_template": {
                        "description": t(
                            "core-config-default-text_to_image_rendering_template"
                        ),
                        "type": "string",
                        "hint": t(
                            "core-config-default-text_to_image_template_maintained_by_page"
                        ),
                        "invisible": True,
                    },
                    "log_level": {
                        "description": t("core-config-default-console_log_level"),
                        "type": "string",
                        "hint": t("core-config-default-console_output_log_level"),
                        "options": ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
                    },
                    "dashboard.ssl.enable": {
                        "description": t("core-config-default-enable_webui_https"),
                        "type": "bool",
                        "hint": t("core-config-default-webui_serves_with_https"),
                    },
                    "dashboard.ssl.cert_file": {
                        "description": t(
                            "core-config-default-ssl_certificate_file_path"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-ssl_certificate_path_hint"),
                        "condition": {"dashboard.ssl.enable": True},
                    },
                    "dashboard.ssl.key_file": {
                        "description": t(
                            "core-config-default-ssl_private_key_file_path"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-ssl_private_key_path_hint"),
                        "condition": {"dashboard.ssl.enable": True},
                    },
                    "dashboard.ssl.ca_certs": {
                        "description": t(
                            "core-config-default-ssl_ca_certificate_file_path"
                        ),
                        "type": "string",
                        "hint": t("core-config-default-ssl_ca_certificate_optional"),
                        "condition": {"dashboard.ssl.enable": True},
                    },
                    "log_file_enable": {
                        "description": t("core-config-default-enable_file_logging"),
                        "type": "bool",
                        "hint": t("core-config-default-logs_written_to_file"),
                    },
                    "log_file_path": {
                        "description": t("core-config-default-log_file_path"),
                        "type": "string",
                        "hint": t("core-config-default-log_file_path_hint"),
                    },
                    "log_file_max_mb": {
                        "description": t("core-config-default-log_file_size_limit_mb"),
                        "type": "int",
                        "hint": t("core-config-default-log_rotation_size_default_20mb"),
                    },
                    "temp_dir_max_size": {
                        "description": t(
                            "core-config-default-temp_directory_size_limit_mb"
                        ),
                        "type": "int",
                        "hint": t(
                            "core-config-default-temp_dir_size_limit_cleanup_hint"
                        ),
                    },
                    "trace_log_enable": {
                        "description": t(
                            "core-config-default-enable_trace_file_logging"
                        ),
                        "type": "bool",
                        "hint": t("core-config-default-trace_to_file_hint"),
                    },
                    "trace_log_path": {
                        "description": t("core-config-default-trace_log_file_path"),
                        "type": "string",
                        "hint": t("core-config-default-trace_log_path_hint"),
                    },
                    "trace_log_max_mb": {
                        "description": t("core-config-default-trace_log_size_limit_mb"),
                        "type": "int",
                        "hint": t("core-config-default-trace_log_rotation_hint"),
                    },
                    "pip_install_arg": {
                        "description": t("core-config-default-pip_extra_args"),
                        "type": "string",
                        "hint": t("core-config-default-pip_extra_args_hint"),
                    },
                    "pypi_index_url": {
                        "description": t("core-config-default-pypi_mirror_url"),
                        "type": "string",
                        "hint": t("core-config-default-pypi_mirror_hint"),
                    },
                    "callback_api_base": {
                        "description": t("core-config-default-public_callback_url"),
                        "type": "string",
                        "hint": t("core-config-default-public_callback_url_hint"),
                    },
                    "timezone": {
                        "description": t("core-config-default-timezone_setting"),
                        "type": "string",
                        "hint": t("core-config-default-timezone_hint"),
                    },
                    "http_proxy": {
                        "description": t("core-config-default-http_proxy"),
                        "type": "string",
                        "hint": t("core-config-default-http_proxy_hint"),
                    },
                    "no_proxy": {
                        "description": t("core-config-default-no_proxy_list"),
                        "type": "list",
                        "items": {"type": "string"},
                    },
                },
            },
        },
    },
}


DEFAULT_VALUE_MAP = {
    "int": 0,
    "float": 0.0,
    "bool": False,
    "string": "",
    "text": "",
    "list": [],
    "file": [],
    "object": {},
    "template_list": [],
}
