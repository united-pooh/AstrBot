### astrbot/builtin_stars/web_searcher/main.py
builtin-stars-web-searcher-legacy-tavily-key-migrated = 旧形式の websearch_tavily_key（文字列形式）を検出しました。リスト形式へ自動移行して保存しました。
builtin-stars-web-searcher-scraping-web = web_searcher - Web 取得: { $title } - { $url }
builtin-stars-web-searcher-bing-search-error = Bing 検索エラー: { $error }、次のエンジンを試します...
builtin-stars-web-searcher-bing-search-failed = Bing 検索に失敗しました
builtin-stars-web-searcher-sogo-search-error = Sogo 検索エラー: { $error }
builtin-stars-web-searcher-sogo-search-failed = Sogo 検索に失敗しました
builtin-stars-web-searcher-tavily-key-not-configured = エラー: AstrBot に Tavily API キーが設定されていません。
builtin-stars-web-searcher-tavily-search-failed = Tavily Web 検索に失敗しました: { $reason }, status: { $status }
builtin-stars-web-searcher-tavily-no-results = エラー: Tavily Web 検索で結果が返りませんでした。
builtin-stars-web-searcher-command-deprecated = このコマンドは廃止予定です。WebUI で Web 検索を有効化または無効化してください。
builtin-stars-web-searcher-search-from-engine = web_searcher - search_from_search_engine: { $query }
builtin-stars-web-searcher-default-no-results = エラー: Web 検索で結果が返りませんでした。
builtin-stars-web-searcher-process-result-error = 検索結果の処理中にエラーが発生しました: { $error }
builtin-stars-web-searcher-link-summary-instruction = {"\u000A"}{"\u000A"}この質問について、上記の結果を基に要点を箇条書きで要約し、可能であれば末尾に参照リンクを付けてください。
builtin-stars-web-searcher-baidu-key-not-configured = エラー: AstrBot に Baidu AI Search API キーが設定されていません。
builtin-stars-web-searcher-baidu-mcp-init-success = Baidu AI Search MCP サーバーの初期化に成功しました。
builtin-stars-web-searcher-search-from-tavily = web_searcher - search_from_tavily: { $query }
builtin-stars-web-searcher-url-empty = エラー: url は空でない文字列である必要があります。
builtin-stars-web-searcher-bocha-key-not-configured = エラー: AstrBot に BoCha API キーが設定されていません。
builtin-stars-web-searcher-bocha-search-failed = BoCha Web 検索に失敗しました: { $reason }, status: { $status }
builtin-stars-web-searcher-search-from-bocha = web_searcher - search_from_bocha: { $query }
builtin-stars-web-searcher-bocha-no-results = エラー: BoCha Web 検索で結果が返りませんでした。
builtin-stars-web-searcher-baidu-tool-not-found = Baidu AI Search MCP ツールを取得できません。
builtin-stars-web-searcher-baidu-mcp-init-failed = Baidu AI Search MCP サーバーを初期化できません: { $error }

### astrbot/builtin_stars/astrbot/main.py
builtin-stars-astrbot-main-chat-enhance-error = チャット強化の初期化に失敗しました: { $error }
builtin-stars-astrbot-main-record-message-error = グループチャット記憶の記録に失敗しました: { $error }
builtin-stars-astrbot-main-no-llm-provider-for-active-reply = LLM プロバイダーが見つかりません。先に設定してください。アクティブ返信を続行できません。
builtin-stars-astrbot-main-no-conversation-active-reply = アクティブな会話が見つからないため、アクティブ返信を実行できません。\"Platform Settings -> Session Isolation (unique_session)\" が無効であることを確認し、/switch で切り替えるか /new で作成してください。
builtin-stars-astrbot-main-conversation-not-found-active-reply = 会話が見つからないため、アクティブ返信を実行できません。
builtin-stars-astrbot-main-active-reply-failed = アクティブ返信に失敗しました: { $error }
builtin-stars-astrbot-main-ltm-error = 長期記憶の処理に失敗しました: { $error }

### astrbot/builtin_stars/astrbot/long_term_memory.py
builtin-stars-astrbot-ltm-invalid-max-count = 長期記憶設定 group_message_max_cnt が不正です。既定値 300 にフォールバックします: { $error }
builtin-stars-astrbot-ltm-provider-not-found = ID { $provider_id } のプロバイダーが見つかりません。
builtin-stars-astrbot-ltm-provider-type-invalid = プロバイダー種別が不正です ({ $provider_type })。画像キャプションを取得できません。
builtin-stars-astrbot-ltm-empty-image-url = 画像 URL が空です。
builtin-stars-astrbot-ltm-image-caption-failed = 画像キャプションの取得に失敗しました: { $error }
builtin-stars-astrbot-ltm-recorded-message = ltm | { $umo } | { $message }
builtin-stars-astrbot-ltm-recorded-ai-response = AI 応答を記録しました: { $umo } | { $message }

### astrbot/builtin_stars/session_controller/main.py
builtin-stars-session-controller-llm-response-failed = LLM 応答に失敗しました: { $error }
builtin-stars-session-controller-empty-mention-fallback-reply = 何を聞きたいですか？😄
builtin-stars-session-controller-empty-mention-handler-error = エラーが発生しました。管理者に連絡してください: { $error }
builtin-stars-session-controller-handle-empty-mention-error = handle_empty_mention エラー: { $error }

### astrbot/builtin_stars/builtin_commands/commands/plugin.py
builtin-stars-plugin-list-title = 読み込み済みプラグイン:{"\u000A"}
builtin-stars-plugin-list-line = - `{ $name }` By { $author }: { $desc }
builtin-stars-plugin-list-disabled-tag =  (無効)
builtin-stars-plugin-list-empty = 読み込まれているプラグインはありません。
builtin-stars-plugin-list-footer = {"\u000A"}/plugin help <plugin_name> でプラグインヘルプと登録コマンドを確認できます。{"\u000A"}/plugin on/off <plugin_name> でプラグインを有効化/無効化できます。
builtin-stars-plugin-off-demo-mode = デモモードではプラグインを無効化できません。
builtin-stars-plugin-off-usage = /plugin off <plugin_name> でプラグインを無効化します。
builtin-stars-plugin-off-success = プラグイン { $plugin_name } を無効化しました。
builtin-stars-plugin-on-demo-mode = デモモードではプラグインを有効化できません。
builtin-stars-plugin-on-usage = /plugin on <plugin_name> でプラグインを有効化します。
builtin-stars-plugin-on-success = プラグイン { $plugin_name } を有効化しました。
builtin-stars-plugin-get-demo-mode = デモモードではプラグインをインストールできません。
builtin-stars-plugin-get-usage = /plugin get <plugin_repo_url> でプラグインをインストールします
builtin-stars-plugin-get-install-start = { $plugin_repo } からプラグインのインストールを準備しています。
builtin-stars-plugin-get-success = プラグインのインストールに成功しました。
builtin-stars-plugin-get-failed-log = プラグインのインストールに失敗しました: { $error }
builtin-stars-plugin-get-failed-user = プラグインのインストールに失敗しました: { $error }
builtin-stars-plugin-help-usage = /plugin help <plugin_name> でプラグイン情報を表示します。
builtin-stars-plugin-help-not-found = プラグインが見つかりません。
builtin-stars-plugin-help-author-version = {"\u000A"}{"\u000A"}✨ 作者: { $author }{"\u000A"}✨ バージョン: { $version }
builtin-stars-plugin-help-command-list-title = {"\u000A"}{"\u000A"}🔧 コマンド一覧:{"\u000A"}
builtin-stars-plugin-help-command-line = - { $command_name }
builtin-stars-plugin-help-command-line-with-desc = - { $command_name }: { $command_desc }
builtin-stars-plugin-help-command-tip = {"\u000A"}ヒント: コマンド実行にはウェイクプレフィックスが必要です。既定値は / です。
builtin-stars-plugin-help-title = 🧩 プラグイン { $plugin_name } ヘルプ:{"\u000A"}
builtin-stars-plugin-help-readme-tip = 詳細はプラグインリポジトリの README を確認してください。

### astrbot/builtin_stars/builtin_commands/commands/provider.py
builtin-stars-provider-reachability-failed = プロバイダー到達性チェックに失敗: id={ $provider_id } type={ $provider_type } code={ $err_code } reason={ $err_reason }
builtin-stars-provider-list-llm-title = ## 読み込み済み LLM プロバイダー{"\u000A"}
builtin-stars-provider-reachability-checking = プロバイダー到達性を確認中です。しばらくお待ちください...
builtin-stars-provider-status-failed-with-code =  ❌(code: { $error_code })
builtin-stars-provider-status-current =  (現在)
builtin-stars-provider-list-tts-title = {"\u000A"}## 読み込み済み TTS プロバイダー{"\u000A"}
builtin-stars-provider-list-stt-title = {"\u000A"}## 読み込み済み STT プロバイダー{"\u000A"}
builtin-stars-provider-list-llm-switch-tip = {"\u000A"}/provider <index> で LLM プロバイダーを切り替えます。
builtin-stars-provider-list-tts-switch-tip = {"\u000A"}/provider tts <index> で TTS プロバイダーを切り替えます。
builtin-stars-provider-list-stt-switch-tip = {"\u000A"}/provider stt <index> で STT プロバイダーを切り替えます。
builtin-stars-provider-list-reachability-skipped = {"\u000A"}プロバイダー到達性チェックはスキップされました。必要なら設定で有効化してください。
builtin-stars-provider-switch-index-required = インデックスを入力してください。
builtin-stars-provider-switch-invalid-index = 無効なプロバイダーインデックスです。
builtin-stars-provider-switch-success = { $provider_id } への切り替えに成功しました。
builtin-stars-provider-switch-invalid-arg = 無効な引数です。
builtin-stars-provider-no-llm-provider = LLM プロバイダーが見つかりません。先に設定してください。
builtin-stars-provider-model-list-failed = モデル一覧の取得に失敗しました: { $error }
builtin-stars-provider-model-list-title = このプロバイダーで利用可能なモデル:
builtin-stars-provider-model-none = なし
builtin-stars-provider-model-current = {"\u000A"}現在のモデル: [{ $current_model }]
builtin-stars-provider-model-switch-tip = {"\u000A"}ヒント: /model <model_name/index> でリアルタイムにモデルを切り替えられます。対象モデルが一覧にない場合はモデル名を直接入力してください。
builtin-stars-provider-model-invalid-index = 無効なモデルインデックスです。
builtin-stars-provider-model-switch-unknown-error = モデル切替時に不明なエラーが発生しました: { $error }
builtin-stars-provider-model-switch-success = モデル切替に成功しました。現在のプロバイダー: [{ $provider_id }] 現在のモデル: [{ $current_model }]
builtin-stars-provider-model-switch-to = モデルを { $current_model } に切り替えました。
builtin-stars-provider-key-list-title = Key:
builtin-stars-provider-key-current = {"\u000A"}現在のキー: { $current_key }
builtin-stars-provider-model-current-inline = {"\u000A"}現在のモデル: { $current_model }
builtin-stars-provider-key-switch-tip = {"\u000A"}/key <idx> でキーを切り替えます。
builtin-stars-provider-key-invalid-index = 無効なキーインデックスです。
builtin-stars-provider-key-switch-unknown-error = キー切替時に不明なエラーが発生しました: { $error }
builtin-stars-provider-key-switch-success = キーの切り替えに成功しました。

### astrbot/builtin_stars/builtin_commands/commands/t2i.py
builtin-stars-t2i-disabled = テキストから画像へのモードを無効化しました。
builtin-stars-t2i-enabled = テキストから画像へのモードを有効化しました。

### astrbot/builtin_stars/builtin_commands/commands/tts.py
builtin-stars-tts-status-enabled-prefix = 有効
builtin-stars-tts-status-disabled-prefix = 無効
builtin-stars-tts-enabled-but-global-disabled = 現在のセッションのテキスト読み上げを { $status_text }。ただし、グローバル設定で TTS が有効化されていません。WebUI で有効化してください。
builtin-stars-tts-toggle-result = 現在のセッションのテキスト読み上げを { $status_text }。

### astrbot/builtin_stars/builtin_commands/commands/llm.py
builtin-stars-llm-status-disabled = 無効
builtin-stars-llm-status-enabled = 有効
builtin-stars-llm-toggle-result = LLM チャット機能を { $status }。

### astrbot/builtin_stars/builtin_commands/commands/setunset.py
builtin-stars-setunset-set-success = セッション { $uid } の変数 { $key } を保存しました。削除するには /unset を使用してください。
builtin-stars-setunset-key-not-found = 変数名が見つかりません。使用法: /unset <variable_name>。
builtin-stars-setunset-unset-success = セッション { $uid } の変数 { $key } を削除しました。

### astrbot/builtin_stars/builtin_commands/commands/sid.py
builtin-stars-sid-base-info = UMO: "{ $sid }" この値はホワイトリスト設定に使用できます。{"\u000A"}UID: "{ $user_id }" この値は管理者設定に使用できます。{"\u000A"}メッセージセッションの送信元情報:{"\u000A"}  Bot ID: "{ $umo_platform }"{"\u000A"}  メッセージ種別: "{ $umo_msg_type }"{"\u000A"}  セッション ID: "{ $umo_session_id }"{"\u000A"}この送信元情報はルーティング設定に使用できます。
builtin-stars-sid-unique-session-group-tip = {"\u000A"}{"\u000A"}現在ユニークセッションモードが有効です。グループ ID: "{ $group_id }"。この ID をホワイトリストに追加してグループ全体を許可することもできます。

### astrbot/builtin_stars/builtin_commands/commands/admin.py
builtin-stars-admin-op-usage = 使用法: /op <id> で管理者付与、/deop <id> で管理者解除。ID は /sid で取得してください。
builtin-stars-admin-op-success = 権限の付与に成功しました。
builtin-stars-admin-deop-usage = 使用法: /deop <id> で管理者解除。ID は /sid で取得してください。
builtin-stars-admin-deop-success = 権限の解除に成功しました。
builtin-stars-admin-deop-not-in-list = このユーザー ID は管理者リストにありません。
builtin-stars-admin-wl-usage = 使用法: /wl <id> でホワイトリスト追加、/dwl <id> で削除。ID は /sid で取得してください。
builtin-stars-admin-wl-success = ホワイトリストに追加しました。
builtin-stars-admin-dwl-usage = 使用法: /dwl <id> でホワイトリストから削除。ID は /sid で取得してください。
builtin-stars-admin-dwl-success = ホワイトリストから削除しました。
builtin-stars-admin-dwl-not-in-list = この SID はホワイトリストにありません。
builtin-stars-admin-update-dashboard-start = ダッシュボードの更新を試行しています...
builtin-stars-admin-update-dashboard-finished = ダッシュボードの更新が完了しました。

### astrbot/builtin_stars/builtin_commands/commands/help.py
builtin-stars-help-no-enabled-reserved-commands = 有効な組み込みコマンドはありません。
builtin-stars-help-header = AstrBot v{ $version } (WebUI: { $dashboard_version })
builtin-stars-help-reserved-command-title = 組み込みコマンド:

### astrbot/builtin_stars/builtin_commands/commands/alter_cmd.py
builtin-stars-alter-cmd-usage = このコマンドは、コマンドまたはコマンドグループの権限を設定します。{"\u000A"}形式: /alter_cmd <cmd_name> <admin/member>{"\u000A"}例1: /alter_cmd c1 admin で c1 を管理者専用コマンドに設定{"\u000A"}例2: /alter_cmd g1 c1 admin でグループ g1 のサブコマンド c1 を管理者専用に設定{"\u000A"}/alter_cmd reset config で reset 権限設定を開く
builtin-stars-alter-cmd-reset-config-menu = reset コマンドの詳細権限設定{"\u000A"}現在の設定:{"\u000A"}1. グループ + ユニークセッション ON: { $group_unique_on }{"\u000A"}2. グループ + ユニークセッション OFF: { $group_unique_off }{"\u000A"}3. プライベートチャット: { $private }{"\u000A"}更新形式:{"\u000A"}/alter_cmd reset scene <scene_index> <admin/member>{"\u000A"}例: /alter_cmd reset scene 2 member
builtin-stars-alter-cmd-scene-and-perm-required = シーンインデックスと権限タイプは必須です。
builtin-stars-alter-cmd-scene-index-invalid = シーンインデックスは 1 から 3 の数値である必要があります。
builtin-stars-alter-cmd-perm-type-invalid = 無効な権限タイプです。admin または member のみ指定できます。
builtin-stars-alter-cmd-reset-scene-updated = シーン { $scene_name } における reset コマンド権限を { $perm_type } に更新しました。
builtin-stars-alter-cmd-type-invalid = 無効なコマンドタイプです。使用可能なのは admin と member です。
builtin-stars-alter-cmd-command-not-found = コマンドが見つかりません。
builtin-stars-alter-cmd-updated = "{ $cmd_name }" { $cmd_group_str } の権限レベルを { $cmd_type } に設定しました。
builtin-stars-alter-cmd-group-label = コマンドグループ
builtin-stars-alter-cmd-command-label = コマンド

### astrbot/builtin_stars/builtin_commands/commands/persona.py
builtin-stars-persona-none = なし
builtin-stars-persona-current-conversation-not-found = 現在の会話が存在しません。先に /new で作成してください。
builtin-stars-persona-name-with-custom-rule = { $persona_name } (カスタムルール)
builtin-stars-persona-new-conversation = 新しい会話
builtin-stars-persona-overview = [Persona]{"\u000A"}{"\u000A"}- Persona 一覧: `/persona list`{"\u000A"}- Persona 設定: `/persona <persona_name>`{"\u000A"}- Persona 詳細: `/persona view <persona_name>`{"\u000A"}- Persona 解除: `/persona unset`{"\u000A"}{"\u000A"}デフォルト Persona: { $default_persona_name }{"\u000A"}現在の会話 { $curr_cid_title } の Persona: { $curr_persona_name }{"\u000A"}{"\u000A"}Persona は WebUI -> Config ページで設定してください{"\u000A"}
builtin-stars-persona-list-title = 📂 Persona 一覧:{"\u000A"}
builtin-stars-persona-list-total = {"\u000A"}Persona 合計: { $total_count }
builtin-stars-persona-list-set-tip = {"\u000A"}*`/persona <persona_name>` で Persona を設定
builtin-stars-persona-list-view-tip = *`/persona view <persona_name>` で詳細を表示
builtin-stars-persona-view-need-name = Persona 名を入力してください。
builtin-stars-persona-view-detail-title = Persona { $persona_name } の詳細:{"\u000A"}
builtin-stars-persona-view-not-found = Persona { $persona_name } は存在しません。
builtin-stars-persona-unset-no-conversation = 現在の会話がないため、Persona を解除できません。
builtin-stars-persona-unset-success = Persona を解除しました。
builtin-stars-persona-set-no-conversation = 現在の会話がありません。先に会話を開始するか、/new で作成してください。
builtin-stars-persona-custom-rule-warning = 注意: カスタムルールにより、現在切り替えた Persona は有効になりません。
builtin-stars-persona-set-success = Persona を設定しました。別の Persona に切り替えた場合は、古い文脈の影響を避けるため /reset でコンテキストをクリアしてください。{ $force_warn_msg }
builtin-stars-persona-set-not-found = Persona が存在しません。/persona list で一覧を確認してください。

### astrbot/builtin_stars/builtin_commands/commands/conversation.py
builtin-stars-conversation-reset-permission-denied = シーン { $scene_name } では reset コマンドに管理者権限が必要です。あなた (ID { $sender_id }) は管理者ではないため、この操作は許可されません。
builtin-stars-conversation-reset-success = 会話のリセットに成功しました。
builtin-stars-conversation-no-llm-provider = LLM プロバイダーが見つかりません。先に設定してください。
builtin-stars-conversation-no-active-conversation = アクティブな会話がありません。/switch で切り替えるか /new で作成してください。
builtin-stars-conversation-clear-history-success = チャット履歴を正常にクリアしました！
builtin-stars-conversation-no-history = 履歴はありません
builtin-stars-conversation-history-result = 現在の会話履歴: { $history }{"\u000A"}{"\u000A"}Page { $page } | Total { $total_pages }{"\u000A"}*/history 2 で 2 ページ目へ移動
builtin-stars-conversation-convs-not-supported = { $runner_types } では会話一覧機能はサポートされていません。
builtin-stars-conversation-list-title = 会話一覧:{"\u000A"}---{"\u000A"}
builtin-stars-conversation-new = 新しい会話
builtin-stars-conversation-list-line = { $index }. { $title }({ $cid }){"\u000A"}  Persona: { $persona_id }{"\u000A"}  更新日時: { $updated_at }{"\u000A"}
builtin-stars-conversation-list-divider = ---{"\u000A"}
builtin-stars-conversation-current-with-id = {"\u000A"}現在の会話: { $title }({ $cid })
builtin-stars-conversation-current-none = {"\u000A"}現在の会話: なし
builtin-stars-conversation-scope-personal = {"\u000A"}セッション分離スコープ: 個人
builtin-stars-conversation-scope-group = {"\u000A"}セッション分離スコープ: グループ
builtin-stars-conversation-page-info = {"\u000A"}Page { $page } | Total { $total_pages }
builtin-stars-conversation-page-jump-tip = {"\u000A"}*/ls 2 で 2 ページ目へ移動
builtin-stars-conversation-new-conv-created = 新しい会話を作成しました。
builtin-stars-conversation-switch-to-new = 新しい会話に切り替えました: 新しい会話({ $cid })。
builtin-stars-conversation-group-switch-to-new = グループ { $session } を新しい会話に切り替えました: 新しい会話({ $cid })。
builtin-stars-conversation-groupnew-need-group-id = グループ ID を入力してください。使用法: /groupnew <group_id>。
builtin-stars-conversation-switch-type-invalid = 無効なタイプです。会話インデックスは数字で入力してください。
builtin-stars-conversation-switch-need-index = 会話インデックスを入力してください。/switch <index>。一覧は /ls、作成は /new。
builtin-stars-conversation-switch-index-invalid = 無効な会話インデックスです。有効な番号は /ls で確認してください。
builtin-stars-conversation-switch-success = 会話を切り替えました: { $title }({ $cid })。
builtin-stars-conversation-rename-need-name = 新しい会話名を入力してください。
builtin-stars-conversation-rename-success = 会話名の変更に成功しました。
builtin-stars-conversation-delete-permission-denied = セッションはグループチャットでユニークセッションが無効、かつあなた (ID { $sender_id }) は管理者ではないため、現在の会話を削除する権限がありません。
builtin-stars-conversation-no-active-conversation-with-index = アクティブな会話がありません。/switch <index> で切り替えるか /new で作成してください。
builtin-stars-conversation-delete-success = 現在の会話を削除しました。現在アクティブな会話はありません。/switch <index> で切り替えるか /new で作成してください。
