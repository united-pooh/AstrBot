### astrbot/builtin_stars/web_searcher/main.py
builtin-stars-web-searcher-legacy-tavily-key-migrated = Обнаружен устаревший websearch_tavily_key (строковый формат); автоматически мигрирован в формат списка и сохранен.
builtin-stars-web-searcher-scraping-web = web_searcher - скрапинг веб-страницы: {$title} - {$url}
builtin-stars-web-searcher-bing-search-error = ошибка поиска Bing: {$error}, пробую следующий движок...
builtin-stars-web-searcher-bing-search-failed = поиск Bing завершился ошибкой
builtin-stars-web-searcher-sogo-search-error = ошибка поиска Sogo: {$error}
builtin-stars-web-searcher-sogo-search-failed = поиск Sogo завершился ошибкой
builtin-stars-web-searcher-tavily-key-not-configured = Ошибка: API-ключ Tavily не настроен в AstrBot.
builtin-stars-web-searcher-tavily-search-failed = Ошибка веб-поиска Tavily: {$reason}, статус: {$status}
builtin-stars-web-searcher-tavily-no-results = Ошибка: веб-поиск Tavily не вернул результатов.
builtin-stars-web-searcher-command-deprecated = Эта команда устарела. Включите или отключите веб-поиск в WebUI.
builtin-stars-web-searcher-search-from-engine = web_searcher - search_from_search_engine: {$query}
builtin-stars-web-searcher-default-no-results = Ошибка: веб-поиск не вернул результатов.
builtin-stars-web-searcher-process-result-error = Ошибка обработки результата поиска: {$error}
builtin-stars-web-searcher-link-summary-instruction = По этому вопросу кратко изложите ключевые моменты на основе результатов выше и, при наличии, добавьте в конце ссылки-источники.
builtin-stars-web-searcher-baidu-key-not-configured = Ошибка: API-ключ Baidu AI Search не настроен в AstrBot.
builtin-stars-web-searcher-baidu-mcp-init-success = MCP-сервер Baidu AI Search успешно инициализирован.
builtin-stars-web-searcher-search-from-tavily = web_searcher - search_from_tavily: {$query}
builtin-stars-web-searcher-url-empty = Ошибка: url должен быть непустой строкой.
builtin-stars-web-searcher-bocha-key-not-configured = Ошибка: API-ключ BoCha не настроен в AstrBot.
builtin-stars-web-searcher-bocha-search-failed = Ошибка веб-поиска BoCha: {$reason}, статус: {$status}
builtin-stars-web-searcher-search-from-bocha = web_searcher - search_from_bocha: {$query}
builtin-stars-web-searcher-bocha-no-results = Ошибка: веб-поиск BoCha не вернул результатов.
builtin-stars-web-searcher-baidu-tool-not-found = Не удалось получить инструмент MCP Baidu AI Search.
builtin-stars-web-searcher-baidu-mcp-init-failed = Не удалось инициализировать MCP-сервер Baidu AI Search: {$error}

### astrbot/builtin_stars/astrbot/main.py
builtin-stars-astrbot-main-chat-enhance-error = Не удалось инициализировать улучшение чата: {$error}
builtin-stars-astrbot-main-record-message-error = Не удалось сохранить память группового чата: {$error}
builtin-stars-astrbot-main-no-llm-provider-for-active-reply = Не найден LLM-провайдер. Сначала настройте его. Активный ответ продолжить нельзя.
builtin-stars-astrbot-main-no-conversation-active-reply = Активный диалог не найден, выполнить активный ответ нельзя. Убедитесь, что \"Platform Settings -> Session Isolation (unique_session)\" отключен, затем переключитесь через /switch или создайте диалог через /new.
builtin-stars-astrbot-main-conversation-not-found-active-reply = Диалог не найден, выполнить активный ответ нельзя.
builtin-stars-astrbot-main-active-reply-failed = Активный ответ завершился ошибкой: {$error}
builtin-stars-astrbot-main-ltm-error = Ошибка обработки долгосрочной памяти: {$error}

### astrbot/builtin_stars/astrbot/long_term_memory.py
builtin-stars-astrbot-ltm-invalid-max-count = Некорректная настройка долгосрочной памяти group_message_max_cnt, используется значение по умолчанию 300: {$error}
builtin-stars-astrbot-ltm-provider-not-found = Провайдер с ID {$provider_id} не найден.
builtin-stars-astrbot-ltm-provider-type-invalid = Некорректный тип провайдера ({$provider_type}); не удалось получить подпись к изображению.
builtin-stars-astrbot-ltm-empty-image-url = URL изображения пуст.
builtin-stars-astrbot-ltm-image-caption-failed = Не удалось получить подпись к изображению: {$error}
builtin-stars-astrbot-ltm-recorded-message = ltm | {$umo} | {$message}
builtin-stars-astrbot-ltm-recorded-ai-response = Ответ ИИ записан: {$umo} | {$message}

### astrbot/builtin_stars/session_controller/main.py
builtin-stars-session-controller-llm-response-failed = Ошибка ответа LLM: {$error}
builtin-stars-session-controller-empty-mention-fallback-reply = Что вы хотите спросить? 😄
builtin-stars-session-controller-empty-mention-handler-error = Произошла ошибка, обратитесь к администратору: {$error}
builtin-stars-session-controller-handle-empty-mention-error = ошибка handle_empty_mention: {$error}

### astrbot/builtin_stars/builtin_commands/commands/plugin.py
builtin-stars-plugin-list-title = Загруженные плагины:
builtin-stars-plugin-list-line = - `{$name}` By {$author}: {$desc}
builtin-stars-plugin-list-disabled-tag =  (Отключен)
builtin-stars-plugin-list-empty = Нет загруженных плагинов.
builtin-stars-plugin-list-footer = Используйте /plugin help <plugin_name>, чтобы посмотреть справку и зарегистрированные команды плагина.Используйте /plugin on/off <plugin_name>, чтобы включить или отключить плагин.
builtin-stars-plugin-off-demo-mode = В демо-режиме плагины нельзя отключать.
builtin-stars-plugin-off-usage = /plugin off <plugin_name> для отключения плагина.
builtin-stars-plugin-off-success = Плагин {$plugin_name} отключен.
builtin-stars-plugin-on-demo-mode = В демо-режиме плагины нельзя включать.
builtin-stars-plugin-on-usage = /plugin on <plugin_name> для включения плагина.
builtin-stars-plugin-on-success = Плагин {$plugin_name} включен.
builtin-stars-plugin-get-demo-mode = В демо-режиме плагины нельзя устанавливать.
builtin-stars-plugin-get-usage = /plugin get <plugin_repo_url> для установки плагина
builtin-stars-plugin-get-install-start = Подготовка к установке плагина из {$plugin_repo}.
builtin-stars-plugin-get-success = Плагин успешно установлен.
builtin-stars-plugin-get-failed-log = Не удалось установить плагин: {$error}
builtin-stars-plugin-get-failed-user = Не удалось установить плагин: {$error}
builtin-stars-plugin-help-usage = /plugin help <plugin_name> для просмотра информации о плагине.
builtin-stars-plugin-help-not-found = Плагин не найден.
builtin-stars-plugin-help-author-version = ✨ Автор: {$author}✨ Версия: {$version}
builtin-stars-plugin-help-command-list-title = 🔧 Список команд:
builtin-stars-plugin-help-command-line = - {$command_name}
builtin-stars-plugin-help-command-line-with-desc = - {$command_name}: {$command_desc}
builtin-stars-plugin-help-command-tip = Подсказка: чтобы вызвать команду, добавьте префикс пробуждения, по умолчанию /.
builtin-stars-plugin-help-title = 🧩 Справка по плагину {$plugin_name}:
builtin-stars-plugin-help-readme-tip = Подробнее смотрите README репозитория плагина.

### astrbot/builtin_stars/builtin_commands/commands/provider.py
builtin-stars-provider-reachability-failed = Проверка доступности провайдера завершилась ошибкой: id={$provider_id} type={$provider_type} code={$err_code} reason={$err_reason}
builtin-stars-provider-list-llm-title = ## Загруженные LLM-провайдеры
builtin-stars-provider-reachability-checking = Выполняется проверка доступности провайдеров, подождите...
builtin-stars-provider-status-failed-with-code =  ❌(код: {$error_code})
builtin-stars-provider-status-current =  (Текущий)
builtin-stars-provider-list-tts-title = ## Загруженные TTS-провайдеры
builtin-stars-provider-list-stt-title = ## Загруженные STT-провайдеры
builtin-stars-provider-list-llm-switch-tip = Используйте /provider <index> для переключения LLM-провайдера.
builtin-stars-provider-list-tts-switch-tip = Используйте /provider tts <index> для переключения TTS-провайдера.
builtin-stars-provider-list-stt-switch-tip = Используйте /provider stt <index> для переключения STT-провайдера.
builtin-stars-provider-list-reachability-skipped = Проверка доступности провайдеров была пропущена. При необходимости включите ее в конфигурации.
builtin-stars-provider-switch-index-required = Введите индекс.
builtin-stars-provider-switch-invalid-index = Некорректный индекс провайдера.
builtin-stars-provider-switch-success = Успешно переключено на {$provider_id}.
builtin-stars-provider-switch-invalid-arg = Некорректный аргумент.
builtin-stars-provider-no-llm-provider = LLM-провайдер не найден. Сначала настройте его.
builtin-stars-provider-model-list-failed = Не удалось получить список моделей: {$error}
builtin-stars-provider-model-list-title = Доступные модели этого провайдера:
builtin-stars-provider-model-none = Нет
builtin-stars-provider-model-current = Текущая модель: [{$current_model}]
builtin-stars-provider-model-switch-tip = Подсказка: используйте /model <model_name/index> для переключения модели в реальном времени. Если нужной модели нет в списке, введите ее имя напрямую.
builtin-stars-provider-model-invalid-index = Некорректный индекс модели.
builtin-stars-provider-model-switch-unknown-error = Неизвестная ошибка при переключении модели: {$error}
builtin-stars-provider-model-switch-success = Модель успешно переключена. Текущий провайдер: [{$provider_id}] Текущая модель: [{$current_model}]
builtin-stars-provider-model-switch-to = Переключено на модель {$current_model}.
builtin-stars-provider-key-list-title = Ключ:
builtin-stars-provider-key-current = Текущий ключ: {$current_key}
builtin-stars-provider-model-current-inline = Текущая модель: {$current_model}
builtin-stars-provider-key-switch-tip = Используйте /key <idx> для переключения ключа.
builtin-stars-provider-key-invalid-index = Некорректный индекс ключа.
builtin-stars-provider-key-switch-unknown-error = Неизвестная ошибка при переключении ключа: {$error}
builtin-stars-provider-key-switch-success = Ключ успешно переключен.

### astrbot/builtin_stars/builtin_commands/commands/t2i.py
builtin-stars-t2i-disabled = Режим преобразования текста в изображение отключен.
builtin-stars-t2i-enabled = Режим преобразования текста в изображение включен.

### astrbot/builtin_stars/builtin_commands/commands/tts.py
builtin-stars-tts-status-enabled-prefix = Включено
builtin-stars-tts-status-disabled-prefix = Отключено
builtin-stars-tts-enabled-but-global-disabled = {$status_text} синтез речи для текущей сессии. Но TTS не включен в глобальной конфигурации. Включите его в WebUI.
builtin-stars-tts-toggle-result = {$status_text} синтез речи для текущей сессии.

### astrbot/builtin_stars/builtin_commands/commands/llm.py
builtin-stars-llm-status-disabled = Отключено
builtin-stars-llm-status-enabled = Включено
builtin-stars-llm-toggle-result = {$status} функцию LLM-чата.

### astrbot/builtin_stars/builtin_commands/commands/setunset.py
builtin-stars-setunset-set-success = Переменная сессии {$uid} {$key} успешно сохранена. Используйте /unset для удаления.
builtin-stars-setunset-key-not-found = Имя переменной не найдено. Использование: /unset <variable_name>.
builtin-stars-setunset-unset-success = Переменная сессии {$uid} {$key} успешно удалена.

### astrbot/builtin_stars/builtin_commands/commands/sid.py
builtin-stars-sid-base-info = UMO: "{$sid}" Это значение можно использовать для настроек белого списка.UID: "{$user_id}" Это значение можно использовать для настроек администратора.Информация об источнике сессии сообщения: ID бота: "{$umo_platform}" Тип сообщения: "{$umo_msg_type}" ID сессии: "{$umo_session_id}"Эту информацию об источнике можно использовать для настройки маршрутизации.
builtin-stars-sid-unique-session-group-tip = Сейчас включен режим уникальной сессии. ID группы: "{$group_id}". Вы также можете добавить этот ID в белый список, чтобы разрешить всю группу.

### astrbot/builtin_stars/builtin_commands/commands/admin.py
builtin-stars-admin-op-usage = Использование: /op <id> выдать админ-доступ; /deop <id> снять админ-доступ. Используйте /sid, чтобы получить ID.
builtin-stars-admin-op-success = Доступ администратора успешно выдан.
builtin-stars-admin-deop-usage = Использование: /deop <id> снять админ-доступ. Используйте /sid, чтобы получить ID.
builtin-stars-admin-deop-success = Доступ администратора успешно снят.
builtin-stars-admin-deop-not-in-list = Этого ID пользователя нет в списке администраторов.
builtin-stars-admin-wl-usage = Использование: /wl <id> добавить в белый список; /dwl <id> удалить. Используйте /sid, чтобы получить ID.
builtin-stars-admin-wl-success = Успешно добавлено в белый список.
builtin-stars-admin-dwl-usage = Использование: /dwl <id> удалить из белого списка. Используйте /sid, чтобы получить ID.
builtin-stars-admin-dwl-success = Успешно удалено из белого списка.
builtin-stars-admin-dwl-not-in-list = Этого SID нет в белом списке.
builtin-stars-admin-update-dashboard-start = Пытаюсь обновить dashboard...
builtin-stars-admin-update-dashboard-finished = Обновление dashboard завершено.

### astrbot/builtin_stars/builtin_commands/commands/help.py
builtin-stars-help-no-enabled-reserved-commands = Нет включенных встроенных команд.
builtin-stars-help-header = AstrBot v{$version} (WebUI: {$dashboard_version})
builtin-stars-help-reserved-command-title = Встроенные команды:

### astrbot/builtin_stars/builtin_commands/commands/alter_cmd.py
builtin-stars-alter-cmd-usage = Эта команда задает права для команды или группы команд.Формат: /alter_cmd <cmd_name> <admin/member>Пример 1: /alter_cmd c1 admin делает c1 командой только для админаПример 2: /alter_cmd g1 c1 admin делает подкоманду c1 в группе g1 командой только для админа/alter_cmd reset config открывает настройки прав reset
builtin-stars-alter-cmd-reset-config-menu = Тонкая настройка прав для команды resetТекущая конфигурация:1. Группа + уникальная сессия ВКЛ: {$group_unique_on}2. Группа + уникальная сессия ВЫКЛ: {$group_unique_off}3. Личный чат: {$private}Формат обновления:/alter_cmd reset scene <scene_index> <admin/member>Пример: /alter_cmd reset scene 2 member
builtin-stars-alter-cmd-scene-and-perm-required = Требуются индекс сцены и тип прав.
builtin-stars-alter-cmd-scene-index-invalid = Индекс сцены должен быть числом от 1 до 3.
builtin-stars-alter-cmd-perm-type-invalid = Неверный тип прав, допускаются только admin или member.
builtin-stars-alter-cmd-reset-scene-updated = Права команды reset обновлены до {$perm_type} в сцене {$scene_name}.
builtin-stars-alter-cmd-type-invalid = Неверный тип команды, доступны типы admin и member.
builtin-stars-alter-cmd-command-not-found = Команда не найдена.
builtin-stars-alter-cmd-updated = Уровень прав для "{$cmd_name}" {$cmd_group_str} установлен в {$cmd_type}.
builtin-stars-alter-cmd-group-label = группа команд
builtin-stars-alter-cmd-command-label = команда

### astrbot/builtin_stars/builtin_commands/commands/persona.py
builtin-stars-persona-none = Нет
builtin-stars-persona-current-conversation-not-found = Текущий диалог не существует. Сначала создайте его через /new.
builtin-stars-persona-name-with-custom-rule = {$persona_name} (пользовательское правило)
builtin-stars-persona-new-conversation = Новый диалог
builtin-stars-persona-overview = [Persona]- Список persona: `/persona list`- Установить persona: `/persona <persona_name>`- Детали persona: `/persona view <persona_name>`- Сбросить persona: `/persona unset`Persona по умолчанию: {$default_persona_name}Persona текущего диалога {$curr_cid_title}: {$curr_persona_name}Настройте persona в WebUI -> страница Config
builtin-stars-persona-list-title = 📂 Список persona:
builtin-stars-persona-list-total = Всего persona: {$total_count}
builtin-stars-persona-list-set-tip = *Используйте `/persona <persona_name>` для установки persona
builtin-stars-persona-list-view-tip = *Используйте `/persona view <persona_name>` для просмотра деталей
builtin-stars-persona-view-need-name = Введите имя persona.
builtin-stars-persona-view-detail-title = Детали persona {$persona_name}:
builtin-stars-persona-view-not-found = Persona {$persona_name} не существует.
builtin-stars-persona-unset-no-conversation = Нет текущего диалога, невозможно сбросить persona.
builtin-stars-persona-unset-success = Persona успешно сброшена.
builtin-stars-persona-set-no-conversation = Нет текущего диалога. Сначала начните его или создайте через /new.
builtin-stars-persona-custom-rule-warning = Напоминание: из-за пользовательских правил выбранная сейчас persona не вступит в силу.
builtin-stars-persona-set-success = Persona успешно установлена. Если вы переключились на другую persona, используйте /reset, чтобы очистить контекст и избежать влияния старого контекста. {$force_warn_msg}
builtin-stars-persona-set-not-found = Persona не существует. Используйте /persona list, чтобы посмотреть все.

### astrbot/builtin_stars/builtin_commands/commands/conversation.py
builtin-stars-conversation-reset-permission-denied = В сцене {$scene_name} команда reset требует права администратора. Вы (ID {$sender_id}) не администратор, поэтому операция запрещена.
builtin-stars-conversation-reset-success = Диалог успешно сброшен.
builtin-stars-conversation-no-llm-provider = LLM-провайдер не найден. Сначала настройте его.
builtin-stars-conversation-no-active-conversation = Нет активного диалога. Используйте /switch для переключения или /new для создания.
builtin-stars-conversation-clear-history-success = История чата успешно очищена!
builtin-stars-conversation-no-history = Нет записей истории
builtin-stars-conversation-history-result = История текущего диалога: {$history}Страница {$page} | Всего {$total_pages}*Введите /history 2 для перехода на страницу 2
builtin-stars-conversation-convs-not-supported = Список диалогов не поддерживается для {$runner_types}.
builtin-stars-conversation-list-title = Список диалогов:---
builtin-stars-conversation-new = Новый диалог
builtin-stars-conversation-list-line = {$index}. {$title}({$cid}) Persona: {$persona_id} Обновлено: {$updated_at}
builtin-stars-conversation-list-divider = ---
builtin-stars-conversation-current-with-id = Текущий диалог: {$title}({$cid})
builtin-stars-conversation-current-none = Текущий диалог: Нет
builtin-stars-conversation-scope-personal = Область изоляции сессии: Личная
builtin-stars-conversation-scope-group = Область изоляции сессии: Групповая
builtin-stars-conversation-page-info = Страница {$page} | Всего {$total_pages}
builtin-stars-conversation-page-jump-tip = *Введите /ls 2 для перехода на страницу 2
builtin-stars-conversation-new-conv-created = Новый диалог создан.
builtin-stars-conversation-switch-to-new = Переключено на новый диалог: Новый диалог({$cid}).
builtin-stars-conversation-group-switch-to-new = Группа {$session} переключена на новый диалог: Новый диалог({$cid}).
builtin-stars-conversation-groupnew-need-group-id = Укажите ID группы. Использование: /groupnew <group_id>.
builtin-stars-conversation-switch-type-invalid = Неверный тип, введите числовой индекс диалога.
builtin-stars-conversation-switch-need-index = Укажите индекс диалога. /switch <index>. Используйте /ls для списка или /new для создания.
builtin-stars-conversation-switch-index-invalid = Неверный индекс диалога, используйте /ls для просмотра допустимых.
builtin-stars-conversation-switch-success = Переключено на диалог: {$title}({$cid}).
builtin-stars-conversation-rename-need-name = Укажите новое имя диалога.
builtin-stars-conversation-rename-success = Диалог успешно переименован.
builtin-stars-conversation-delete-permission-denied = Сессия находится в групповом чате с отключенной unique session, и вы (ID {$sender_id}) не администратор, поэтому у вас нет прав удалять текущий диалог.
builtin-stars-conversation-no-active-conversation-with-index = Нет активного диалога. Используйте /switch <index> для переключения или /new для создания.
builtin-stars-conversation-delete-success = Текущий диалог успешно удален. Сейчас активного диалога нет. Используйте /switch <index> для переключения или /new для создания.
builtin_stars-astrbot-metadata-desc = desc: AstrBot 自带插件，包含人格注入、思考内容注入、群聊上下文感知等功能的实现，禁用后将无法使用这些功能。
builtin_stars-builtin_commands-commands-utils-rst_scene-group_unique_on = Групповой чат + изоляция сессий включена
builtin_stars-builtin_commands-commands-utils-rst_scene-group_unique_off = Групповой чат + изоляция сессий отключена
builtin_stars-builtin_commands-commands-utils-rst_scene-private = Личный чат
builtin_stars-builtin_commands-metadata-desc = desc: AstrBot 自带指令，提供常用的对话管理、工具使用、插件管理等功能。
builtin_stars-session_controller-main-social_media_wakeup_note = Обратите внимание, вы сейчас общаетесь с пользователем в социальной сети, пользователь просто упомянул вас через @, но в этом сообщении не ввёл никакого содержания, он может отправить то, что хотел сказать, в следующем сообщении.
builtin_stars-session_controller-main-ask_user_intent_friendly = Дружелюбно спросите пользователя, о чём он хочет поговорить или в чём нуждается в помощи, ответ должен соответствовать характеру, не будьте слишком механическими.
builtin_stars-session_controller-main-output_only_reply_content = Пожалуйста, обратите внимание, вам нужно вывести только текст ответа пользователю, ничего другого выводить не требуется
builtin_stars-session_controller-metadata-desc = desc: 为插件支持会话控制
builtin_stars-web_searcher-main-migrate_old_tavily_key = Обнаружен старый формат websearch_tavily_key (строка), автоматически преобразовано в формат списка и сохранено.
builtin_stars-web_searcher-main-missing_tavily_key_error = Ошибка: Ключ API Tavily не настроен в AstrBot.
builtin_stars-web_searcher-main-command_deprecated_use_webui = Эта команда устарела, пожалуйста, включайте или выключайте функцию веб-поиска через WebUI.
builtin_stars-web_searcher-main-summarize_with_bullets_and_links = \n\nПо вопросу, пожалуйста, сделайте пунктирное резюме на основе приведённых выше результатов и в конце добавьте соответствующие ссылки на источники (если имеются).
builtin_stars-web_searcher-main-missing_bocha_key_error = Ошибка: Ключ API BoCha не настроен в AstrBot.
builtin_stars-web_searcher-metadata-desc = desc: 让 LLM 具有网页检索能力
builtin_stars-session_controller-main-friendly_inquiry = Дружелюбно спросите у пользователя, о чём он хочет поговорить или в чём нуждается в помощи, ответ должен соответствовать характеру, не должен быть слишком механическим.
builtin_stars-session_controller-main-reply_only_instruction = Пожалуйста, обратите внимание, вам нужно вывести только текст ответа пользователю, не выводите ничего другого
builtin_stars-web_searcher-main-tavily_key_migration = Обнаружен старый формат websearch_tavily_key (строка), автоматически преобразован в список и сохранён.
builtin_stars-web_searcher-main-tavily_key_missing = Ошибка: Ключ API Tavily не настроен в AstrBot.
builtin_stars-web_searcher-main-command_deprecated = Эта команда устарела, пожалуйста, включайте или выключайте функцию веб-поиска в WebUI.
builtin_stars-web_searcher-main-summary_instruction = \n\nПо поставленному вопросу, пожалуйста, сделайте итоговое резюме по пунктам на основе приведённых выше результатов и в конце добавьте ссылки на соответствующие источники (если они есть).
builtin_stars-web_searcher-main-bocha_key_missing = Ошибка: Ключ API BoCha не настроен в AstrBot.
