### astrbot/core/astr_agent_run_util.py
agent-max-steps-reached = Agent 已达到最大步数限制 ({$max_step})，强制返回最终响应。
agent-tool-call = 🔨 调用工具: {$tool_name}
agent-tool-call-unknown = 🔨 调用工具...
agent-request-failed = {"\u000A"}{"\u000A"}AstrBot 请求失败。{"\u000A"}错误类型: {$error_type}{"\u000A"}错误信息: {$error_message}{"\u000A"}{"\u000A"}请在平台日志查看和分享错误详情。{"\u000A"}
agent-error-in-hook = on_agent_done 钩子执行错误
live-agent-stream-tts = [Live Agent] 使用流式 TTS（原生支持 get_audio_stream）
live-agent-tts-info = [Live Agent] 使用 TTS（{$provider_type} {"\u000A"}使用 get_audio，将按句子分块生成音频）
live-agent-runtime-error = [Live Agent] 运行时发生错误: {$error}
live-agent-feeder-error = [Live Agent Feeder] 错误: {$error}
live-tts-stream-error = [Live TTS Stream] 错误: {$error}
live-tts-simulated-error = [Live TTS Simulated] 处理文本 '{$text_preview}...' 时出错: {$error}
live-tts-simulated-critical = [Live TTS Simulated] 严重错误: {$error}
tts-stats-send-failed = 发送 TTS 统计信息失败: {$error}
live-agent-feeder-sentence = [Live Agent Feeder] 分句: {$sentence}

### astrbot/core/astr_agent_tool_exec.py
background-task-failed = 后台任务 {$task_id} 失败: {$error}
background-task-build-failed = 为后台任务{$tool_name}构建主代理失败。
background-task-no-response = 后台任务代理未返回响应
tool-send-message-failed = 工具直接发送消息失败: {$error}，追踪信息: {$traceback}
tool-execution-timeout = 工具 {$tool_name} 执行超时，已超过 {$timeout} 秒。
tool-execution-value-error = 工具执行值错误: {$error}
tool-parameter-mismatch = 工具处理函数参数不匹配，请检查处理函数定义。处理函数参数: {$handler_param_str}
tool-execution-error = 工具执行错误: {$error}。追踪信息: {$traceback}
unknown-method-name = 未知的方法名: {$method_name}
previous-error = 先前错误: {$traceback}

### astrbot/core/zip_updator.py
repo-request-failed = 请求 {$url} 失败，状态码: {$status_code}, 内容: {$content}
repo-parse-error = 解析版本信息时发生异常: {$error}
repo-parse-failed = 解析版本信息失败
repo-no-suitable-release = 未找到合适的发布版本
repo-downloading-update = 正在下载更新 {$repo} ...
repo-downloading-branch = 正在从指定分支 {$branch} 下载 {$author}/{$repo}
repo-fetch-releases-failed = 获取 {$author}/{$repo} 的 GitHub Releases 失败: {$error}，将尝试下载默认分支
repo-downloading-default = 正在从默认分支下载 {$author}/{$repo}
repo-using-mirror = 检查到设置了镜像站，将使用镜像站下载 {$author}/{$repo} 仓库源码: {$url}
repo-unzip-complete = 解压文件完成: {$zip_path}
repo-delete-temp = 删除临时更新文件: {$zip_path} 和 {$temp_dir}
repo-delete-failed = 删除更新文件失败，可以手动删除 {$zip_path} 和 {$temp_dir}
repo-invalid-url = 无效的 GitHub URL
repo-request-failed-exception = 请求失败，状态码: {$status_code}
release-info = 版本: {$version} | 发布于: {$published_at}


### agent/agent.py


### agent/context/compressor.py


### agent/context/config.py


### agent/context/manager.py


### agent/context/token_counter.py


### agent/context/truncator.py


### agent/handoff.py


### agent/hooks.py


### agent/mcp_client.py


### agent/message.py


### agent/response.py


### agent/run_context.py


### agent/runners/base.py


### agent/runners/coze/coze_agent_runner.py


### agent/runners/coze/coze_api_client.py


### agent/runners/dashscope/dashscope_agent_runner.py


### agent/runners/dify/dify_agent_runner.py


### agent/runners/dify/dify_api_client.py


### agent/runners/tool_loop_agent_runner.py


### agent/tool.py


### agent/tool_executor.py


### agent/tool_image_cache.py


### astr_agent_context.py


### astr_agent_hooks.py


### astr_main_agent.py


### astr_main_agent_resources.py


### astrbot_config_mgr.py


### backup/constants.py


### backup/exporter.py


### backup/importer.py


### computer/booters/base.py


### computer/booters/boxlite.py


### computer/booters/local.py


### computer/booters/shipyard.py


### computer/computer_client.py


### computer/olayer/filesystem.py


### computer/olayer/python.py


### computer/olayer/shell.py


### computer/tools/fs.py


### computer/tools/python.py


### computer/tools/shell.py


### config/astrbot_config.py


### config/default.py


### config/i18n_utils.py


### conversation_mgr.py


### core_lifecycle.py


### cron/events.py


### cron/manager.py


### db/migration/helper.py


### db/migration/migra_3_to_4.py


### db/migration/migra_45_to_46.py


### db/migration/migra_token_usage.py


### db/migration/migra_webchat_session.py


### db/migration/shared_preferences_v3.py


### db/migration/sqlite_v3.py


### db/po.py


### db/sqlite.py


### db/vec_db/base.py


### db/vec_db/faiss_impl/document_storage.py


### db/vec_db/faiss_impl/embedding_storage.py


### db/vec_db/faiss_impl/vec_db.py


### event_bus.py


### exceptions.py


### file_token_service.py


### initial_loader.py


### knowledge_base/chunking/base.py


### knowledge_base/chunking/fixed_size.py


### knowledge_base/chunking/recursive.py


### knowledge_base/kb_db_sqlite.py


### knowledge_base/kb_helper.py


### knowledge_base/kb_mgr.py


### knowledge_base/models.py


### knowledge_base/parsers/base.py


### knowledge_base/parsers/markitdown_parser.py


### knowledge_base/parsers/pdf_parser.py


### knowledge_base/parsers/text_parser.py


### knowledge_base/parsers/url_parser.py


### knowledge_base/parsers/util.py


### knowledge_base/prompts.py


### knowledge_base/retrieval/manager.py


### knowledge_base/retrieval/rank_fusion.py


### knowledge_base/retrieval/sparse_retriever.py


### lang.py


### log.py


### message/components.py


### message/message_event_result.py


### persona_mgr.py


### pipeline/content_safety_check/stage.py


### pipeline/content_safety_check/strategies/baidu_aip.py


### pipeline/content_safety_check/strategies/keywords.py


### pipeline/content_safety_check/strategies/strategy.py


### pipeline/context.py


### pipeline/context_utils.py


### pipeline/preprocess_stage/stage.py


### pipeline/process_stage/method/agent_request.py


### pipeline/process_stage/method/agent_sub_stages/internal.py


### pipeline/process_stage/method/agent_sub_stages/third_party.py


### pipeline/process_stage/method/star_request.py


### pipeline/process_stage/stage.py


### pipeline/rate_limit_check/stage.py


### pipeline/respond/stage.py


### pipeline/result_decorate/stage.py


### pipeline/scheduler.py


### pipeline/session_status_check/stage.py


### pipeline/stage.py


### pipeline/waking_check/stage.py


### pipeline/whitelist_check/stage.py


### platform/astr_message_event.py


### platform/astrbot_message.py


### platform/manager.py


### platform/message_session.py


### platform/message_type.py


### platform/platform.py


### platform/platform_metadata.py


### platform/register.py


### platform/sources/aiocqhttp/aiocqhttp_message_event.py


### platform/sources/aiocqhttp/aiocqhttp_platform_adapter.py


### platform/sources/dingtalk/dingtalk_adapter.py


### platform/sources/dingtalk/dingtalk_event.py


### platform/sources/discord/client.py


### platform/sources/discord/components.py


### platform/sources/discord/discord_platform_adapter.py


### platform/sources/discord/discord_platform_event.py


### platform/sources/lark/lark_adapter.py


### platform/sources/lark/lark_event.py


### platform/sources/lark/server.py


### platform/sources/line/line_adapter.py


### platform/sources/line/line_api.py


### platform/sources/line/line_event.py


### platform/sources/misskey/misskey_adapter.py


### platform/sources/misskey/misskey_api.py


### platform/sources/misskey/misskey_event.py


### platform/sources/misskey/misskey_utils.py


### platform/sources/qqofficial/qqofficial_message_event.py


### platform/sources/qqofficial/qqofficial_platform_adapter.py


### platform/sources/qqofficial_webhook/qo_webhook_adapter.py


### platform/sources/qqofficial_webhook/qo_webhook_event.py


### platform/sources/qqofficial_webhook/qo_webhook_server.py


### platform/sources/satori/satori_adapter.py


### platform/sources/satori/satori_event.py


### platform/sources/slack/client.py


### platform/sources/slack/slack_adapter.py


### platform/sources/slack/slack_event.py


### platform/sources/telegram/tg_adapter.py


### platform/sources/telegram/tg_event.py


### platform/sources/webchat/webchat_adapter.py


### platform/sources/webchat/webchat_event.py


### platform/sources/webchat/webchat_queue_mgr.py


### platform/sources/wecom/wecom_adapter.py


### platform/sources/wecom/wecom_event.py


### platform/sources/wecom/wecom_kf.py


### platform/sources/wecom/wecom_kf_message.py


### platform/sources/wecom_ai_bot/WXBizJsonMsgCrypt.py


### platform/sources/wecom_ai_bot/ierror.py


### platform/sources/wecom_ai_bot/wecomai_adapter.py


### platform/sources/wecom_ai_bot/wecomai_api.py


### platform/sources/wecom_ai_bot/wecomai_event.py


### platform/sources/wecom_ai_bot/wecomai_queue_mgr.py


### platform/sources/wecom_ai_bot/wecomai_server.py


### platform/sources/wecom_ai_bot/wecomai_utils.py


### platform/sources/wecom_ai_bot/wecomai_webhook.py


### platform/sources/weixin_official_account/weixin_offacc_adapter.py


### platform/sources/weixin_official_account/weixin_offacc_event.py


### platform_message_history_mgr.py


### provider/entites.py


### provider/entities.py


### provider/func_tool_manager.py


### provider/manager.py


### provider/provider.py


### provider/register.py


### provider/sources/anthropic_source.py


### provider/sources/azure_tts_source.py


### provider/sources/bailian_rerank_source.py


### provider/sources/dashscope_tts.py


### provider/sources/edge_tts_source.py


### provider/sources/fishaudio_tts_api_source.py


### provider/sources/gemini_embedding_source.py


### provider/sources/gemini_source.py


### provider/sources/gemini_tts_source.py


### provider/sources/genie_tts.py


### provider/sources/groq_source.py


### provider/sources/gsv_selfhosted_source.py


### provider/sources/gsvi_tts_source.py


### provider/sources/minimax_tts_api_source.py


### provider/sources/oai_aihubmix_source.py


### provider/sources/openai_embedding_source.py


### provider/sources/openai_source.py


### provider/sources/openai_tts_api_source.py


### provider/sources/openrouter_source.py


### provider/sources/sensevoice_selfhosted_source.py


### provider/sources/vllm_rerank_source.py


### provider/sources/volcengine_tts.py


### provider/sources/whisper_api_source.py


### provider/sources/whisper_selfhosted_source.py


### provider/sources/xai_source.py


### provider/sources/xinference_rerank_source.py


### provider/sources/xinference_stt_provider.py


### provider/sources/zhipu_source.py


### skills/skill_manager.py


### star/command_management.py


### star/config.py


### star/context.py


### star/filter/command.py


### star/filter/command_group.py


### star/filter/custom_filter.py


### star/filter/event_message_type.py


### star/filter/permission.py


### star/filter/platform_adapter_type.py


### star/filter/regex.py


### star/register/star.py


### star/register/star_handler.py


### star/session_llm_manager.py


### star/session_plugin_manager.py


### star/star.py


### star/star_handler.py


### star/star_manager.py


### star/star_tools.py


### star/updator.py


### subagent_orchestrator.py


### tools/cron_tools.py


### umop_config_router.py


### updator.py


### utils/active_event_registry.py


### utils/astrbot_path.py


### utils/command_parser.py


### utils/file_extract.py


### utils/history_saver.py


### utils/http_ssl.py


### utils/io.py


### utils/llm_metadata.py


### utils/log_pipe.py


### utils/media_utils.py


### utils/metrics.py


### utils/migra_helper.py


### utils/network_utils.py


### utils/path_util.py


### utils/pip_installer.py


### utils/plugin_kv_store.py


### utils/quoted_message/chain_parser.py


### utils/quoted_message/extractor.py


### utils/quoted_message/image_refs.py


### utils/quoted_message/image_resolver.py


### utils/quoted_message/onebot_client.py


### utils/quoted_message/settings.py


### utils/quoted_message_parser.py


### utils/runtime_env.py


### utils/session_lock.py


### utils/session_waiter.py


### utils/shared_preferences.py


### utils/string_utils.py


### utils/t2i/local_strategy.py


### utils/t2i/network_strategy.py


### utils/t2i/renderer.py


### utils/t2i/template_manager.py


### utils/temp_dir_cleaner.py


### utils/tencent_record_helper.py


### utils/trace.py


### utils/version_comparator.py


### utils/webhook_utils.py
