### astrbot/dashboard/utils.py
dashboard-utils-tsne-lib-missing = 缺少必要的库以生成 t-SNE 可视化。请安装 matplotlib 和 scikit-learn: { $e }
dashboard-utils-kb-not-found = 未找到知识库
dashboard-utils-faiss-index-not-found = FAISS 索引不存在: { $index_path }
dashboard-utils-index-empty = 索引为空
dashboard-utils-extract-vectors = 提取 { $n } 个向量用于可视化...
dashboard-utils-tsne-reduction = 开始 t-SNE 降维...
dashboard-utils-gen-chart = 生成可视化图表...
dashboard-utils-kb-vectors-label = 知识库向量
dashboard-utils-query-label = 查询
dashboard-utils-vector-index-label = 向量索引
dashboard-utils-tsne-title = t-SNE 可视化: 知识库中的查询{"\u000A"}({ $n } 个向量, { $d } 维, 知识库: { $kb_name })
dashboard-utils-tsne-dim1 = t-SNE 维度 1
dashboard-utils-tsne-dim2 = t-SNE 维度 2
dashboard-utils-tsne-error = 生成 t-SNE 可视化时出错: { $e }

### astrbot/dashboard/server.py
dashboard-server-route-not-found = 未找到该路由
dashboard-server-unauthorized = 未授权
dashboard-server-token-expired = Token 过期
dashboard-server-token-invalid = Token 无效
dashboard-server-port-check-error = 检查端口 { $port } 时发生错误: { $e }
dashboard-server-proc-name = 进程名: { $name }
dashboard-server-pid = PID: { $pid }
dashboard-server-exec-path = 执行路径: { $exe }
dashboard-server-work-dir = 工作目录: { $cwd }
dashboard-server-cmd-line = 启动命令: { $cmd }
dashboard-server-access-denied = 无法获取进程详细信息(可能需要管理员权限): { $e }
dashboard-server-proc-not-found = 未找到占用进程
dashboard-server-get-proc-failed = 获取进程信息失败: { $e }
dashboard-server-webui-disabled = WebUI 已被禁用
dashboard-server-starting = 正在启动 WebUI, 监听地址: { $url }
dashboard-server-security-tip = 提示: WebUI 将监听所有网络接口，请注意安全。（可在 data/cmd_config.json 中配置 dashboard.host 以修改 host）
dashboard-server-port-in-use = 错误：端口 { $port } 已被占用{"\u000A"}占用信息: {"\u000A"}           { $info }{"\u000A"}请确保：{"\u000A"}1. 没有其他 AstrBot 实例正在运行{"\u000A"}2. 端口 { $port } 没有被其他程序占用{"\u000A"}3. 如需使用其他端口，请修改配置文件
dashboard-server-started-banner = {"\u000A"} ✨✨✨{"\u000A"}  AstrBot v{ $version } WebUI 已启动，可访问{"\u000A"}{"\u000A"}
dashboard-server-local-url = ➜  本地: { $url }{"\u000A"}
dashboard-server-network-url = ➜  网络: { $url }{"\u000A"}
dashboard-server-default-creds = ➜  默认用户名和密码: astrbot{"\u000A"} ✨✨✨{"\u000A"}
dashboard-server-remote-access-tip = 可在 data/cmd_config.json 中配置 dashboard.host 以便远程访问。{"\u000A"}
dashboard-server-ssl-config-required = dashboard.ssl.enable 为 true 时，必须配置 cert_file 和 key_file。
dashboard-server-ssl-cert-not-found = SSL 证书文件不存在: { $path }
dashboard-server-ssl-key-not-found = SSL 私钥文件不存在: { $path }
dashboard-server-ssl-ca-not-found = SSL CA 证书文件不存在: { $path }
dashboard-server-shutdown = AstrBot WebUI 已经被优雅地关闭

### astrbot/dashboard/routes/api_key.py


dashboard-server-jwt-secret-initialized = 已为仪表盘初始化随机 JWT 密钥。
dashboard-routes-update-migration-failed = 迁移失败: { $unknown }
dashboard-routes-update-check-failed-no-impact-normal-use = 检查更新失败: { $e } (不影响除项目更新外的正常使用)
dashboard-routes-update-api-releases = /api/update/releases: { $unknown }
dashboard-routes-update-download-dashboard-file-failed = 下载管理面板文件失败: { $e }。
dashboard-routes-update-updating-dependencies = 更新依赖中...
dashboard-routes-update-update-dependencies-failed = 更新依赖失败: { $e }
dashboard-routes-update-api-project = /api/update_project: { $unknown }
dashboard-routes-update-api-dashboard = /api/update_dashboard: { $unknown }
dashboard-routes-update-api-pip = /api/update_pip: { $unknown }
dashboard-routes-lang-route-lang = [LangRoute] lang:{ $lang }
dashboard-routes-backup-clean-expired-upload-session = 清理过期的上传会话: { $upload_id }
dashboard-routes-backup-clean-expired-upload-session-failed = 清理过期上传会话失败: { $e }
dashboard-routes-backup-clean-chunk-directory-failed = 清理分片目录失败: { $e }
dashboard-routes-backup-read-manifest-failed = 读取备份 manifest 失败: { $e }
dashboard-routes-backup-skip-invalid-file = 跳过无效备份文件: { $filename }
dashboard-routes-backup-get-list-failed = 获取备份列表失败: { $e }
dashboard-routes-backup-create-failed = 创建备份失败: { $e }
dashboard-routes-backup-export-task-failed = 后台导出任务 { $task_id } 失败: { $e }
dashboard-routes-backup-uploaded-file-saved-original-name = 上传的备份文件已保存: { $unique_filename } (原始名称: { $filename })
dashboard-routes-backup-upload-file-failed = 上传备份文件失败: { $e }
dashboard-routes-backup-init-chunk-upload = 初始化分片上传: upload_id={ $upload_id }, filename={ $unique_filename }, total_chunks={ $total_chunks }
dashboard-routes-backup-init-chunk-upload-failed = 初始化分片上传失败: { $e }
dashboard-routes-backup-receive-chunk = 接收分片: upload_id={ $upload_id }, chunk={ $unknown }/{ $total_chunks }
dashboard-routes-backup-upload-chunk-failed = 上传分片失败: { $e }
dashboard-routes-backup-marked-as-upload-source = 已标记备份为上传来源: { $zip_path }
dashboard-routes-backup-mark-source-failed = 标记备份来源失败: { $e }
dashboard-routes-backup-chunk-upload-complete = 分片上传完成: { $filename }, size={ $file_size }, chunks={ $total }
dashboard-routes-backup-complete-chunk-upload-failed = 完成分片上传失败: { $e }
dashboard-routes-backup-cancel-chunk-upload = 取消分片上传: { $upload_id }
dashboard-routes-backup-cancel-upload-failed = 取消上传失败: { $e }
dashboard-routes-backup-precheck-file-failed = 预检查备份文件失败: { $e }
dashboard-routes-backup-import-failed = 导入备份失败: { $e }
dashboard-routes-backup-import-task-failed = 后台导入任务 { $task_id } 失败: { $e }
dashboard-routes-backup-get-task-progress-failed = 获取任务进度失败: { $e }
dashboard-routes-backup-download-failed = 下载备份失败: { $e }
dashboard-routes-backup-delete-failed = 删除备份失败: { $e }
dashboard-routes-backup-file-rename = 备份文件重命名: { $filename } -> { $new_filename }
dashboard-routes-backup-rename-failed = 重命名备份失败: { $e }
dashboard-routes-config-item-no-type-definition-skip-validation = 配置项 { $path }{ $key } 没有类型定义, 跳过校验
dashboard-routes-config-saving-is-core = 正在保存配置, is_core={ $is_core }
dashboard-routes-config-exception-validating-config = 验证配置时出现异常: { $e }
dashboard-routes-config-checking-provider-details = 正在尝试检查提供者: { $unknown } (ID: { $unknown }, 类型: { $unknown }, 模型: { $unknown })
dashboard-routes-config-provider-available = 提供者 { $unknown } (ID: { $unknown }) 可用。
dashboard-routes-config-provider-unavailable-error = 提供者 { $unknown } (ID: { $unknown }) 不可用。错误: { $error_message }
dashboard-routes-config-traceback = { $unknown } 的回溯信息:
    { $unknown }
dashboard-routes-config-api-call-provider-check-one = API 调用: /config/provider/check_one id={ $provider_id }
dashboard-routes-config-provider-id-not-found = 在 provider_manager 中未找到 ID 为 '{ $provider_id }' 的提供者。
dashboard-routes-config-embedding-vector-dimension-detected = 检测到 { $unknown } 的嵌入向量维度为 { $dim }
dashboard-routes-config-provider-source-model-list = 获取到 provider_source { $provider_source_id } 的模型列表: { $models }
dashboard-routes-config-using-cached-platform-logo = 正在使用平台 { $name } 的缓存标志令牌。
dashboard-routes-config-platform-class-not-found = 未找到平台 { $name } 的平台类。
dashboard-routes-config-platform-logo-registered = 已为平台 { $name } 注册标志令牌。
dashboard-routes-config-platform-logo-file-missing = 未找到平台 { $name } 的标志文件: { $logo_file_path }
dashboard-routes-config-platform-import-modules-failed = 无法为平台 { $name } 导入所需的模块: { $e }
dashboard-routes-config-platform-logo-file-system-error = 平台 { $name } 标志的文件系统错误: { $e }
dashboard-routes-config-platform-logo-registration-error = 注册平台 { $name } 标志时发生意外错误: { $e }

### astrbot/dashboard/routes/knowledge_base.py
dashboard-routes-knowledge-base-upload-document-failed = 上传文档 { $unknown } 失败: { $e }
dashboard-routes-knowledge-base-background-upload-task-failed = 后台上传任务 { $task_id } 失败: { $e }
dashboard-routes-knowledge-base-import-document-failed = 导入文档 { $file_name } 失败: { $e }
dashboard-routes-knowledge-base-background-import-task-failed = 后台导入任务 { $task_id } 失败: { $e }
dashboard-routes-knowledge-base-get-list-failed = 获取知识库列表失败: { $e }
dashboard-routes-knowledge-base-create-failed = 创建知识库失败: { $e }
dashboard-routes-knowledge-base-get-details-failed = 获取知识库详情失败: { $e }
dashboard-routes-knowledge-base-update-failed = 更新知识库失败: { $e }
dashboard-routes-knowledge-base-delete-failed = 删除知识库失败: { $e }
dashboard-routes-knowledge-base-get-stats-failed = 获取知识库统计失败: { $e }
dashboard-routes-knowledge-base-document-list-failed = 获取文档列表失败: { $e }
dashboard-routes-knowledge-base-document-upload-failed = 上传文档失败: { $e }
dashboard-routes-knowledge-base-document-import-failed = 导入文档失败: { $e }
dashboard-routes-knowledge-base-get-upload-progress-failed = 获取上传进度失败: { $e }
dashboard-routes-knowledge-base-document-details-failed = 获取文档详情失败: { $e }
dashboard-routes-knowledge-base-delete-document-failed = 删除文档失败: { $e }
dashboard-routes-knowledge-base-delete-text-chunk-failed = 删除文本块失败: { $e }
dashboard-routes-knowledge-base-chunk-list-failed = 获取块列表失败: { $e }
dashboard-routes-knowledge-base-generate-t-sne-visualization-failed = 生成 t-SNE 可视化失败: { $e }
dashboard-routes-knowledge-base-retrieval-failed = 检索失败: { $e }
dashboard-routes-knowledge-base-upload-document-from-url-failed = 从URL上传文档失败: { $e }
dashboard-routes-knowledge-base-background-upload-url-task-failed = 后台上传URL任务 { $task_id } 失败: { $e }

### astrbot/dashboard/routes/skills.py
dashboard-routes-skills-remove-temp-file-failed = 移除临时技能文件失败: { $temp_path }

### astrbot/dashboard/routes/live_chat.py
dashboard-routes-live-chat-started-speaking = [实时聊天] { $username } 开始说话 stamp={ $stamp }
dashboard-routes-live-chat-stamp-mismatch-or-not-speaking = [实时聊天] stamp 不匹配或未在说话状态: { $stamp } vs { $current_stamp }
dashboard-routes-live-chat-no-audio-frame-data = [实时聊天] 没有音频帧数据
dashboard-routes-live-chat-audio-file-saved-size = [实时聊天] 音频文件已保存: { $audio_path }, 大小: { $unknown } bytes
dashboard-routes-live-chat-assemble-wav-file-failed = [实时聊天] 组装 WAV 文件失败: { $e }
dashboard-routes-live-chat-temp-file-deleted = [实时聊天] 已删除临时文件: { $temp_audio_path }
dashboard-routes-live-chat-delete-temp-file-failed = [实时聊天] 删除临时文件失败: { $e }
dashboard-routes-live-chat-websocket-connection-established = [实时聊天] WebSocket 连接建立: { $username }
dashboard-routes-live-chat-websocket-error = [实时聊天] WebSocket 错误: { $e }
dashboard-routes-live-chat-websocket-connection-closed = [实时聊天] WebSocket 连接关闭: { $username }
dashboard-routes-live-chat-start-speaking-missing-stamp = [实时聊天] start_speaking 缺少 stamp
dashboard-routes-live-chat-decode-audio-data-failed = [实时聊天] 解码音频数据失败: { $e }
dashboard-routes-live-chat-end-speaking-missing-stamp = [实时聊天] end_speaking 缺少 stamp
dashboard-routes-live-chat-user-interruption = [实时聊天] 用户打断: { $username }
dashboard-routes-live-chat-stt-provider-not-configured = [实时聊天] STT Provider 未配置
dashboard-routes-live-chat-stt-recognition-empty = [实时聊天] STT 识别结果为空
dashboard-routes-live-chat-stt-result = [实时聊天] STT 结果: { $user_text }
dashboard-routes-live-chat-user-interruption-detected = [实时聊天] 检测到用户打断
dashboard-routes-live-chat-message-id-mismatch = [实时聊天] 消息 ID 不匹配: { $result_message_id } != { $message_id }
dashboard-routes-live-chat-parse-agent-stats-failed = [实时聊天] 解析 AgentStats 失败: { $e }
dashboard-routes-live-chat-parse-tts-stats-failed = [实时聊天] 解析 TTSStats 失败: { $e }
dashboard-routes-live-chat-start-audio-stream-playback = [实时聊天] 开始播放音频流
dashboard-routes-live-chat-bot-reply-complete = [实时聊天] Bot 回复完成: { $bot_text }
dashboard-routes-live-chat-process-audio-failed = [实时聊天] 处理音频失败: { $e }
dashboard-routes-live-chat-save-interrupted-message = [实时聊天] 保存打断消息: { $interrupted_text }
dashboard-routes-live-chat-user-message-session-ts = [实时聊天] 用户消息: { $user_text } (session: { $session_id }, ts: { $timestamp })
dashboard-routes-live-chat-bot-interrupted-message-session-ts = [实时聊天] Bot 消息（打断）: { $interrupted_text } (session: { $session_id }, ts: { $timestamp })
dashboard-routes-live-chat-log-message-failed = [实时聊天] 记录消息失败: { $e }

### astrbot/dashboard/routes/log.py
dashboard-routes-log-sse-resend-history-error = Log SSE 补发历史错误: { $e }
dashboard-routes-log-sse-connection-error = Log SSE 连接错误: { $e }
dashboard-routes-log-get-log-history-failed = 获取日志历史失败: { $e }
dashboard-routes-log-get-trace-settings-failed = 获取 Trace 设置失败: { $e }
dashboard-routes-log-update-trace-settings-failed = 更新 Trace 设置失败: { $e }

### astrbot/dashboard/routes/conversation.py
dashboard-routes-conversation-db-query-error = 数据库查询出错: { $e }
    { $unknown }
dashboard-routes-conversation-get-details-failed = 获取对话详情失败: { $e }
    { $unknown }
dashboard-routes-conversation-update-info-failed = 更新对话信息失败: { $e }
    { $unknown }
dashboard-routes-conversation-delete-failed = 删除对话失败: { $e }
    { $unknown }
dashboard-routes-conversation-update-history-failed = 更新对话历史失败: { $e }
    { $unknown }
dashboard-routes-conversation-export-failed-user-id-cid-error = 导出对话失败: user_id={ $user_id }, cid={ $cid }, error={ $e }
dashboard-routes-conversation-batch-export-failed = 批量导出对话失败: { $e }
    { $unknown }

### astrbot/dashboard/routes/open_api.py
dashboard-routes-open-api-create-chat-session-failed = 创建聊天会话 { $session_id } 失败: { $e }
dashboard-routes-open-api-update-chat-config-route-failed = 更新 { $umo } 的聊天配置路由失败，配置ID为 { $config_id }: { $e }
dashboard-routes-open-api-send-message-failed = Open API send_message 失败: { $e }

### astrbot/dashboard/routes/session_management.py
dashboard-routes-session-management-get-knowledge-bases-failed = 获取知识库列表失败: { $e }
dashboard-routes-session-management-get-rules-failed = 获取规则列表失败: { $e }
dashboard-routes-session-management-update-session-rules-failed = 更新会话规则失败: { $e }

### astrbot/dashboard/routes/stat.py
dashboard-routes-stat-path-traversal-attempt-detected = 检测到路径遍历尝试: { $version } -> { $changelog_path }

### astrbot/dashboard/routes/plugin.py
dashboard-routes-plugin-api-plugin-reload-failed = /api/plugin/reload-failed: { $unknown }
dashboard-routes-plugin-api-plugin-reload = /api/plugin/reload: { $unknown }
dashboard-routes-plugin-md5-match-use-cached-market = 缓存MD5匹配，使用缓存的插件市场数据
dashboard-routes-plugin-remote-market-data-empty = 远程插件市场数据为空: { $url }
dashboard-routes-plugin-remote-market-data-fetched-with-count = 成功获取远程插件市场数据，包含 { $unknown } 个插件
dashboard-routes-plugin-request-failed-status-code = 请求 { $url } 失败，状态码：{ $status }
dashboard-routes-plugin-request-failed-error = 请求 { $url } 失败，错误：{ $e }
dashboard-routes-plugin-remote-market-data-fetch-failed-use-cache = 远程插件市场数据获取失败，使用缓存数据
dashboard-routes-plugin-load-cached-md5-failed = 加载缓存MD5失败: { $e }
dashboard-routes-plugin-get-remote-md5-failed = 获取远程MD5失败: { $e }
dashboard-routes-plugin-no-md5-in-cache-file = 缓存文件中没有MD5信息
dashboard-routes-plugin-cannot-get-remote-md5-use-cache = 无法获取远程MD5，将使用缓存
dashboard-routes-plugin-data-md5-local-remote-valid = 插件数据MD5: 本地={ $cached_md5 }, 远程={ $remote_md5 }, 有效={ $is_valid }
dashboard-routes-plugin-check-cache-validity-failed = 检查缓存有效性失败: { $e }
dashboard-routes-plugin-load-cache-file-cache-time = 加载缓存文件: { $cache_file }, 缓存时间: { $unknown }
dashboard-routes-plugin-load-plugin-market-cache-failed = 加载插件市场缓存失败: { $e }
dashboard-routes-plugin-market-data-cached-to-md5 = 插件市场数据已缓存到: { $cache_file }, MD5: { $md5 }
dashboard-routes-plugin-save-plugin-market-cache-failed = 保存插件市场缓存失败: { $e }
dashboard-routes-plugin-get-logo-failed = 获取插件 Logo 失败: { $e }
dashboard-routes-plugin-installing-repo = 正在安装插件 { $repo_url }
dashboard-routes-plugin-install-repo-success = 安装插件 { $repo_url } 成功。
dashboard-routes-plugin-installing-uploaded = 正在安装用户上传的插件 { $filename }
dashboard-routes-plugin-install-uploaded-success = 安装插件 { $filename } 成功
dashboard-routes-plugin-uninstalling = 正在卸载插件 { $plugin_name }
dashboard-routes-plugin-uninstall-success = 卸载插件 { $plugin_name } 成功
dashboard-routes-plugin-updating = 正在更新插件 { $plugin_name }
dashboard-routes-plugin-update-success = 更新插件 { $plugin_name } 成功。
dashboard-routes-plugin-api-update = /api/plugin/update: { $unknown }
dashboard-routes-plugin-batch-update = 批量更新插件 { $name }
dashboard-routes-plugin-api-update-all-failed = /api/plugin/update-all: 更新插件 { $name } 失败: { $unknown }
dashboard-routes-plugin-deactivate = 停用插件 { $plugin_name } 。
dashboard-routes-plugin-api-off = /api/plugin/off: { $unknown }
dashboard-routes-plugin-activate = 启用插件 { $plugin_name } 。
dashboard-routes-plugin-api-on = /api/plugin/on: { $unknown }
dashboard-routes-plugin-getting-readme-content = 正在获取插件 { $plugin_name } 的README文件内容
dashboard-routes-plugin-name-empty = 插件名称为空
dashboard-routes-plugin-not-exist = 插件 { $plugin_name } 不存在
dashboard-routes-plugin-dir-not-exist = 插件 { $plugin_name } 目录不存在
dashboard-routes-plugin-cannot-find-dir = 无法找到插件目录: { $plugin_dir }
dashboard-routes-plugin-no-readme = 插件 { $plugin_name } 没有README文件
dashboard-routes-plugin-api-readme = /api/plugin/readme: { $unknown }
dashboard-routes-plugin-getting-changelog = 正在获取插件 { $plugin_name } 的更新日志
dashboard-routes-plugin-api-changelog = /api/plugin/changelog: { $unknown }
dashboard-routes-plugin-api-source-save = /api/plugin/source/save: { $unknown }



### astrbot/dashboard/routes/auth.py
dashboard-auth-default-pwd-tip = 为了保证安全，请尽快修改默认密码。
dashboard-auth-invalid-creds = 用户名或密码错误。
dashboard-auth-demo-mode-denied = 演示模式下不允许此操作。
dashboard-auth-wrong-old-pwd = 原密码错误。
dashboard-auth-empty-fields = 新用户名和新密码不能同时为空，你改了个寂寞。
dashboard-auth-edit-success = 修改成功。
dashboard-auth-jwt-secret-not-found = 配置文件中未设置 JWT 秘钥