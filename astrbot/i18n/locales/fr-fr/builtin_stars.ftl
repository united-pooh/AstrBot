### astrbot/builtin_stars/web_searcher/main.py
builtin-stars-web-searcher-legacy-tavily-key-migrated = Ancienne clé websearch_tavily_key détectée (format chaîne) ; migrée automatiquement vers le format liste et enregistrée.
builtin-stars-web-searcher-scraping-web = web_searcher - extraction web : { $title } - { $url }
builtin-stars-web-searcher-bing-search-error = erreur de recherche Bing : { $error }, essai du moteur suivant...
builtin-stars-web-searcher-bing-search-failed = échec de la recherche Bing
builtin-stars-web-searcher-sogo-search-error = erreur de recherche Sogo : { $error }
builtin-stars-web-searcher-sogo-search-failed = échec de la recherche Sogo
builtin-stars-web-searcher-tavily-key-not-configured = Erreur : la clé API Tavily n'est pas configurée dans AstrBot.
builtin-stars-web-searcher-tavily-search-failed = Échec de la recherche web Tavily : { $reason }, statut : { $status }
builtin-stars-web-searcher-tavily-no-results = Erreur : le moteur de recherche web Tavily n'a retourné aucun résultat.
builtin-stars-web-searcher-command-deprecated = Cette commande est obsolète. Veuillez activer ou désactiver la recherche web dans WebUI.
builtin-stars-web-searcher-search-from-engine = web_searcher - search_from_search_engine: { $query }
builtin-stars-web-searcher-default-no-results = Erreur : le moteur de recherche web n'a retourné aucun résultat.
builtin-stars-web-searcher-process-result-error = Erreur lors du traitement du résultat de recherche : { $error }
builtin-stars-web-searcher-link-summary-instruction = {"\u000A"}{"\u000A"}Pour la question, résumez les points clés à partir des résultats ci-dessus, puis ajoutez des liens de référence à la fin quand ils sont disponibles.
builtin-stars-web-searcher-baidu-key-not-configured = Erreur : la clé API Baidu AI Search n'est pas configurée dans AstrBot.
builtin-stars-web-searcher-baidu-mcp-init-success = Serveur MCP Baidu AI Search initialisé avec succès.
builtin-stars-web-searcher-search-from-tavily = web_searcher - search_from_tavily: { $query }
builtin-stars-web-searcher-url-empty = Erreur : url doit être une chaîne non vide.
builtin-stars-web-searcher-bocha-key-not-configured = Erreur : la clé API BoCha n'est pas configurée dans AstrBot.
builtin-stars-web-searcher-bocha-search-failed = Échec de la recherche web BoCha : { $reason }, statut : { $status }
builtin-stars-web-searcher-search-from-bocha = web_searcher - search_from_bocha: { $query }
builtin-stars-web-searcher-bocha-no-results = Erreur : le moteur de recherche web BoCha n'a retourné aucun résultat.
builtin-stars-web-searcher-baidu-tool-not-found = Impossible d'obtenir l'outil MCP Baidu AI Search.
builtin-stars-web-searcher-baidu-mcp-init-failed = Impossible d'initialiser le serveur MCP Baidu AI Search : { $error }

### astrbot/builtin_stars/astrbot/main.py
builtin-stars-astrbot-main-chat-enhance-error = Échec de l'initialisation de l'amélioration du chat : { $error }
builtin-stars-astrbot-main-record-message-error = Échec de l'enregistrement de la mémoire du chat de groupe : { $error }
builtin-stars-astrbot-main-no-llm-provider-for-active-reply = Aucun fournisseur LLM trouvé. Veuillez d'abord en configurer un. La réponse active ne peut pas continuer.
builtin-stars-astrbot-main-no-conversation-active-reply = Aucune conversation active trouvée, impossible d'effectuer une réponse active. Assurez-vous que "Platform Settings -> Session Isolation (unique_session)" est désactivé, puis basculez avec /switch ou créez-en une avec /new.
builtin-stars-astrbot-main-conversation-not-found-active-reply = Conversation introuvable, impossible d'effectuer une réponse active.
builtin-stars-astrbot-main-active-reply-failed = Échec de la réponse active : { $error }
builtin-stars-astrbot-main-ltm-error = Échec du traitement de la mémoire à long terme : { $error }

### astrbot/builtin_stars/astrbot/long_term_memory.py
builtin-stars-astrbot-ltm-invalid-max-count = Configuration de mémoire à long terme group_message_max_cnt invalide, retour à la valeur par défaut 300 : { $error }
builtin-stars-astrbot-ltm-provider-not-found = Le fournisseur avec l'ID { $provider_id } est introuvable.
builtin-stars-astrbot-ltm-provider-type-invalid = Type de fournisseur invalide ({ $provider_type }) ; impossible d'obtenir la légende d'image.
builtin-stars-astrbot-ltm-empty-image-url = L'URL de l'image est vide.
builtin-stars-astrbot-ltm-image-caption-failed = Échec de la génération de la légende d'image : { $error }
builtin-stars-astrbot-ltm-recorded-message = ltm | { $umo } | { $message }
builtin-stars-astrbot-ltm-recorded-ai-response = Réponse IA enregistrée : { $umo } | { $message }

### astrbot/builtin_stars/session_controller/main.py
builtin-stars-session-controller-llm-response-failed = Échec de la réponse LLM : { $error }
builtin-stars-session-controller-empty-mention-fallback-reply = Que souhaitez-vous demander ? 😄
builtin-stars-session-controller-empty-mention-handler-error = Une erreur s'est produite, veuillez contacter l'administrateur : { $error }
builtin-stars-session-controller-handle-empty-mention-error = erreur handle_empty_mention : { $error }

### astrbot/builtin_stars/builtin_commands/commands/plugin.py
builtin-stars-plugin-list-title = Plugins chargés :{"\u000A"}
builtin-stars-plugin-list-line = - `{ $name }` Par { $author } : { $desc }
builtin-stars-plugin-list-disabled-tag =  (Désactivé)
builtin-stars-plugin-list-empty = Aucun plugin n'est chargé.
builtin-stars-plugin-list-footer = {"\u000A"}Utilisez /plugin help <plugin_name> pour voir l'aide du plugin et ses commandes enregistrées.{"\u000A"}Utilisez /plugin on/off <plugin_name> pour activer ou désactiver un plugin.
builtin-stars-plugin-off-demo-mode = Les plugins ne peuvent pas être désactivés en mode démo.
builtin-stars-plugin-off-usage = /plugin off <plugin_name> pour désactiver un plugin.
builtin-stars-plugin-off-success = Le plugin { $plugin_name } a été désactivé.
builtin-stars-plugin-on-demo-mode = Les plugins ne peuvent pas être activés en mode démo.
builtin-stars-plugin-on-usage = /plugin on <plugin_name> pour activer un plugin.
builtin-stars-plugin-on-success = Le plugin { $plugin_name } a été activé.
builtin-stars-plugin-get-demo-mode = Les plugins ne peuvent pas être installés en mode démo.
builtin-stars-plugin-get-usage = /plugin get <plugin_repo_url> pour installer un plugin
builtin-stars-plugin-get-install-start = Préparation de l'installation du plugin depuis { $plugin_repo }.
builtin-stars-plugin-get-success = Plugin installé avec succès.
builtin-stars-plugin-get-failed-log = Échec de l'installation du plugin : { $error }
builtin-stars-plugin-get-failed-user = Échec de l'installation du plugin : { $error }
builtin-stars-plugin-help-usage = /plugin help <plugin_name> pour afficher les informations du plugin.
builtin-stars-plugin-help-not-found = Plugin introuvable.
builtin-stars-plugin-help-author-version = {"\u000A"}{"\u000A"}✨ Auteur : { $author }{"\u000A"}✨ Version : { $version }
builtin-stars-plugin-help-command-list-title = {"\u000A"}{"\u000A"}🔧 Liste des commandes :{"\u000A"}
builtin-stars-plugin-help-command-line = - { $command_name }
builtin-stars-plugin-help-command-line-with-desc = - { $command_name } : { $command_desc }
builtin-stars-plugin-help-command-tip = {"\u000A"}Astuce : ajoutez le préfixe de réveil pour déclencher les commandes, par défaut /.
builtin-stars-plugin-help-title = 🧩 Aide du plugin { $plugin_name } :{"\u000A"}
builtin-stars-plugin-help-readme-tip = Pour plus de détails, consultez le README du dépôt du plugin.

### astrbot/builtin_stars/builtin_commands/commands/provider.py
builtin-stars-provider-reachability-failed = Échec de la vérification d'accessibilité du fournisseur : id={ $provider_id } type={ $provider_type } code={ $err_code } raison={ $err_reason }
builtin-stars-provider-list-llm-title = ## Fournisseurs LLM chargés{"\u000A"}
builtin-stars-provider-reachability-checking = Vérification de l'accessibilité des fournisseurs en cours, veuillez patienter...
builtin-stars-provider-status-failed-with-code =  ❌(code : { $error_code })
builtin-stars-provider-status-current =  (Actuel)
builtin-stars-provider-list-tts-title = {"\u000A"}## Fournisseurs TTS chargés{"\u000A"}
builtin-stars-provider-list-stt-title = {"\u000A"}## Fournisseurs STT chargés{"\u000A"}
builtin-stars-provider-list-llm-switch-tip = {"\u000A"}Utilisez /provider <index> pour changer de fournisseur LLM.
builtin-stars-provider-list-tts-switch-tip = {"\u000A"}Utilisez /provider tts <index> pour changer de fournisseur TTS.
builtin-stars-provider-list-stt-switch-tip = {"\u000A"}Utilisez /provider stt <index> pour changer de fournisseur STT.
builtin-stars-provider-list-reachability-skipped = {"\u000A"}La vérification d'accessibilité des fournisseurs a été ignorée. Activez-la dans la configuration si nécessaire.
builtin-stars-provider-switch-index-required = Veuillez saisir un index.
builtin-stars-provider-switch-invalid-index = Index de fournisseur invalide.
builtin-stars-provider-switch-success = Basculé avec succès vers { $provider_id }.
builtin-stars-provider-switch-invalid-arg = Argument invalide.
builtin-stars-provider-no-llm-provider = Aucun fournisseur LLM trouvé. Veuillez d'abord en configurer un.
builtin-stars-provider-model-list-failed = Échec de récupération de la liste des modèles : { $error }
builtin-stars-provider-model-list-title = Modèles disponibles pour ce fournisseur :
builtin-stars-provider-model-none = Aucun
builtin-stars-provider-model-current = {"\u000A"}Modèle actuel : [{ $current_model }]
builtin-stars-provider-model-switch-tip = {"\u000A"}Astuce : utilisez /model <nom_modele/index> pour changer de modèle en temps réel. Si le modèle cible n'est pas listé, saisissez directement son nom.
builtin-stars-provider-model-invalid-index = Index de modèle invalide.
builtin-stars-provider-model-switch-unknown-error = Erreur inconnue lors du changement de modèle : { $error }
builtin-stars-provider-model-switch-success = Modèle changé avec succès. Fournisseur actuel : [{ $provider_id }] Modèle actuel : [{ $current_model }]
builtin-stars-provider-model-switch-to = Modèle changé vers { $current_model }.
builtin-stars-provider-key-list-title = Clé :
builtin-stars-provider-key-current = {"\u000A"}Clé actuelle : { $current_key }
builtin-stars-provider-model-current-inline = {"\u000A"}Modèle actuel : { $current_model }
builtin-stars-provider-key-switch-tip = {"\u000A"}Utilisez /key <idx> pour changer de clé.
builtin-stars-provider-key-invalid-index = Index de clé invalide.
builtin-stars-provider-key-switch-unknown-error = Erreur inconnue lors du changement de clé : { $error }
builtin-stars-provider-key-switch-success = Clé changée avec succès.

### astrbot/builtin_stars/builtin_commands/commands/t2i.py
builtin-stars-t2i-disabled = Le mode texte-vers-image a été désactivé.
builtin-stars-t2i-enabled = Le mode texte-vers-image a été activé.

### astrbot/builtin_stars/builtin_commands/commands/tts.py
builtin-stars-tts-status-enabled-prefix = Activé
builtin-stars-tts-status-disabled-prefix = Désactivé
builtin-stars-tts-enabled-but-global-disabled = { $status_text } la synthèse vocale pour la session actuelle. Mais le TTS n'est pas activé dans la configuration globale. Veuillez l'activer dans WebUI.
builtin-stars-tts-toggle-result = { $status_text } la synthèse vocale pour la session actuelle.

### astrbot/builtin_stars/builtin_commands/commands/llm.py
builtin-stars-llm-status-disabled = Désactivé
builtin-stars-llm-status-enabled = Activé
builtin-stars-llm-toggle-result = { $status } la fonction de chat LLM.

### astrbot/builtin_stars/builtin_commands/commands/setunset.py
builtin-stars-setunset-set-success = Variable de session { $uid } { $key } enregistrée avec succès. Utilisez /unset pour la supprimer.
builtin-stars-setunset-key-not-found = Nom de variable introuvable. Utilisation : /unset <variable_name>.
builtin-stars-setunset-unset-success = Variable de session { $uid } { $key } supprimée avec succès.

### astrbot/builtin_stars/builtin_commands/commands/sid.py
builtin-stars-sid-base-info = UMO : "{ $sid }" Cette valeur peut être utilisée pour les paramètres de liste blanche.{"\u000A"}UID : "{ $user_id }" Cette valeur peut être utilisée pour les paramètres d'administrateur.{"\u000A"}Informations source de session de message :{"\u000A"}  ID bot : "{ $umo_platform }"{"\u000A"}  Type de message : "{ $umo_msg_type }"{"\u000A"}  ID de session : "{ $umo_session_id }"{"\u000A"}Ces informations source peuvent être utilisées pour la configuration du routage.
builtin-stars-sid-unique-session-group-tip = {"\u000A"}{"\u000A"}Le mode session unique est actuellement activé. ID du groupe : "{ $group_id }". Vous pouvez aussi ajouter cet ID à la liste blanche pour autoriser tout le groupe.

### astrbot/builtin_stars/builtin_commands/commands/admin.py
builtin-stars-admin-op-usage = Utilisation : /op <id> pour accorder les droits admin ; /deop <id> pour les retirer. Utilisez /sid pour obtenir l'ID.
builtin-stars-admin-op-success = Autorisation accordée avec succès.
builtin-stars-admin-deop-usage = Utilisation : /deop <id> pour retirer les droits admin. Utilisez /sid pour obtenir l'ID.
builtin-stars-admin-deop-success = Autorisation retirée avec succès.
builtin-stars-admin-deop-not-in-list = Cet ID utilisateur n'est pas dans la liste des administrateurs.
builtin-stars-admin-wl-usage = Utilisation : /wl <id> pour ajouter à la liste blanche ; /dwl <id> pour retirer. Utilisez /sid pour obtenir l'ID.
builtin-stars-admin-wl-success = Ajout à la liste blanche réussi.
builtin-stars-admin-dwl-usage = Utilisation : /dwl <id> pour retirer de la liste blanche. Utilisez /sid pour obtenir l'ID.
builtin-stars-admin-dwl-success = Retrait de la liste blanche réussi.
builtin-stars-admin-dwl-not-in-list = Ce SID n'est pas dans la liste blanche.
builtin-stars-admin-update-dashboard-start = Tentative de mise à jour du tableau de bord...
builtin-stars-admin-update-dashboard-finished = Mise à jour du tableau de bord terminée.

### astrbot/builtin_stars/builtin_commands/commands/help.py
builtin-stars-help-no-enabled-reserved-commands = Aucune commande intégrée activée.
builtin-stars-help-header = AstrBot v{ $version } (WebUI : { $dashboard_version })
builtin-stars-help-reserved-command-title = Commandes intégrées :

### astrbot/builtin_stars/builtin_commands/commands/alter_cmd.py
builtin-stars-alter-cmd-usage = Cette commande définit les permissions d'une commande ou d'un groupe de commandes.{"\u000A"}Format : /alter_cmd <cmd_name> <admin/member>{"\u000A"}Exemple 1 : /alter_cmd c1 admin définit c1 comme commande admin uniquement{"\u000A"}Exemple 2 : /alter_cmd g1 c1 admin définit la sous-commande c1 du groupe g1 comme admin uniquement{"\u000A"}/alter_cmd reset config ouvre la configuration des permissions reset
builtin-stars-alter-cmd-reset-config-menu = Configuration fine des permissions pour la commande reset{"\u000A"}Configuration actuelle :{"\u000A"}1. Groupe + session unique ACTIVÉE : { $group_unique_on }{"\u000A"}2. Groupe + session unique DÉSACTIVÉE : { $group_unique_off }{"\u000A"}3. Chat privé : { $private }{"\u000A"}Format de mise à jour :{"\u000A"}/alter_cmd reset scene <scene_index> <admin/member>{"\u000A"}Exemple : /alter_cmd reset scene 2 member
builtin-stars-alter-cmd-scene-and-perm-required = L'index de scène et le type de permission sont requis.
builtin-stars-alter-cmd-scene-index-invalid = L'index de scène doit être un nombre entre 1 et 3.
builtin-stars-alter-cmd-perm-type-invalid = Type de permission invalide, seuls admin ou member sont autorisés.
builtin-stars-alter-cmd-reset-scene-updated = Permission de la commande reset mise à jour à { $perm_type } dans la scène { $scene_name }.
builtin-stars-alter-cmd-type-invalid = Type de commande invalide, les types disponibles sont admin et member.
builtin-stars-alter-cmd-command-not-found = Commande introuvable.
builtin-stars-alter-cmd-updated = Le niveau de permission de "{ $cmd_name }" { $cmd_group_str } a été défini sur { $cmd_type }.
builtin-stars-alter-cmd-group-label = groupe de commandes
builtin-stars-alter-cmd-command-label = commande

### astrbot/builtin_stars/builtin_commands/commands/persona.py
builtin-stars-persona-none = Aucun
builtin-stars-persona-current-conversation-not-found = La conversation actuelle n'existe pas. Veuillez d'abord en créer une avec /new.
builtin-stars-persona-name-with-custom-rule = { $persona_name } (règle personnalisée)
builtin-stars-persona-new-conversation = Nouvelle conversation
builtin-stars-persona-overview = [Persona]{"\u000A"}{"\u000A"}- Liste des personas : `/persona list`{"\u000A"}- Définir un persona : `/persona <persona_name>`{"\u000A"}- Détails d'un persona : `/persona view <persona_name>`{"\u000A"}- Retirer le persona : `/persona unset`{"\u000A"}{"\u000A"}Persona par défaut : { $default_persona_name }{"\u000A"}Persona de la conversation actuelle { $curr_cid_title } : { $curr_persona_name }{"\u000A"}{"\u000A"}Configurez les personas dans WebUI -> page Config{"\u000A"}
builtin-stars-persona-list-title = 📂 Liste des personas :{"\u000A"}
builtin-stars-persona-list-total = {"\u000A"}Total des personas : { $total_count }
builtin-stars-persona-list-set-tip = {"\u000A"}*Utilisez `/persona <persona_name>` pour définir un persona
builtin-stars-persona-list-view-tip = *Utilisez `/persona view <persona_name>` pour afficher les détails
builtin-stars-persona-view-need-name = Veuillez saisir un nom de persona.
builtin-stars-persona-view-detail-title = Détails du persona { $persona_name } :{"\u000A"}
builtin-stars-persona-view-not-found = Le persona { $persona_name } n'existe pas.
builtin-stars-persona-unset-no-conversation = Aucune conversation actuelle, impossible de retirer le persona.
builtin-stars-persona-unset-success = Persona retiré avec succès.
builtin-stars-persona-set-no-conversation = Aucune conversation actuelle. Veuillez d'abord en démarrer une ou en créer une avec /new.
builtin-stars-persona-custom-rule-warning = Rappel : en raison de règles personnalisées, le persona vers lequel vous basculez maintenant ne prendra pas effet.
builtin-stars-persona-set-success = Persona défini avec succès. Si vous avez changé de persona, utilisez /reset pour effacer le contexte et éviter que l'ancien contexte n'affecte le nouveau. { $force_warn_msg }
builtin-stars-persona-set-not-found = Le persona n'existe pas. Utilisez /persona list pour tous les afficher.

### astrbot/builtin_stars/builtin_commands/commands/conversation.py
builtin-stars-conversation-reset-permission-denied = Dans la scène { $scene_name }, la commande reset requiert une permission admin. Vous (ID { $sender_id }) n'êtes pas administrateur, cette opération n'est donc pas autorisée.
builtin-stars-conversation-reset-success = Réinitialisation de la conversation réussie.
builtin-stars-conversation-no-llm-provider = Aucun fournisseur LLM trouvé. Veuillez d'abord en configurer un.
builtin-stars-conversation-no-active-conversation = Aucune conversation active. Utilisez /switch pour basculer ou /new pour en créer une.
builtin-stars-conversation-clear-history-success = Historique du chat effacé avec succès !
builtin-stars-conversation-no-history = Aucun historique
builtin-stars-conversation-history-result = Historique de la conversation actuelle : { $history }{"\u000A"}{"\u000A"}Page { $page } | Total { $total_pages }{"\u000A"}*Entrez /history 2 pour aller à la page 2
builtin-stars-conversation-convs-not-supported = La liste des conversations n'est pas prise en charge pour { $runner_types }.
builtin-stars-conversation-list-title = Liste des conversations :{"\u000A"}---{"\u000A"}
builtin-stars-conversation-new = Nouvelle conversation
builtin-stars-conversation-list-line = { $index }. { $title }({ $cid }){"\u000A"}  Persona : { $persona_id }{"\u000A"}  Mis à jour le : { $updated_at }{"\u000A"}
builtin-stars-conversation-list-divider = ---{"\u000A"}
builtin-stars-conversation-current-with-id = {"\u000A"}Conversation actuelle : { $title }({ $cid })
builtin-stars-conversation-current-none = {"\u000A"}Conversation actuelle : Aucune
builtin-stars-conversation-scope-personal = {"\u000A"}Portée d'isolation de session : Personnelle
builtin-stars-conversation-scope-group = {"\u000A"}Portée d'isolation de session : Groupe
builtin-stars-conversation-page-info = {"\u000A"}Page { $page } | Total { $total_pages }
builtin-stars-conversation-page-jump-tip = {"\u000A"}*Entrez /ls 2 pour aller à la page 2
builtin-stars-conversation-new-conv-created = Nouvelle conversation créée.
builtin-stars-conversation-switch-to-new = Bascule vers une nouvelle conversation : Nouvelle conversation({ $cid }).
builtin-stars-conversation-group-switch-to-new = Le groupe { $session } a basculé vers une nouvelle conversation : Nouvelle conversation({ $cid }).
builtin-stars-conversation-groupnew-need-group-id = Veuillez fournir l'ID du groupe. Utilisation : /groupnew <group_id>.
builtin-stars-conversation-switch-type-invalid = Type invalide, veuillez saisir un index numérique de conversation.
builtin-stars-conversation-switch-need-index = Veuillez fournir l'index de conversation. /switch <index>. Utilisez /ls pour lister ou /new pour créer.
builtin-stars-conversation-switch-index-invalid = Index de conversation invalide, utilisez /ls pour voir les indices valides.
builtin-stars-conversation-switch-success = Bascule vers la conversation : { $title }({ $cid }).
builtin-stars-conversation-rename-need-name = Veuillez fournir un nouveau nom de conversation.
builtin-stars-conversation-rename-success = Conversation renommée avec succès.
builtin-stars-conversation-delete-permission-denied = La session est dans un chat de groupe avec session unique désactivée, et vous (ID { $sender_id }) n'êtes pas administrateur ; vous n'avez donc pas la permission de supprimer la conversation actuelle.
builtin-stars-conversation-no-active-conversation-with-index = Aucune conversation active. Utilisez /switch <index> pour basculer ou /new pour créer.
builtin-stars-conversation-delete-success = Conversation actuelle supprimée avec succès. Aucune conversation active maintenant. Utilisez /switch <index> pour basculer ou /new pour créer.
