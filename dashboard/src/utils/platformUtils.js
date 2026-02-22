/**
 * 平台相关工具函数
 */

/**
 * 获取平台图标
 * @param {string} name - 平台名称或类型
 * @returns {string|undefined} 图标URL
 */
export function getPlatformIcon(name) {
  if (name === 'aiocqhttp') {
    return new URL('@/assets/images/platform_logos/onebot.png', import.meta.url).href
  } else if (name === 'qq_official' || name === 'qq_official_webhook') {
    return new URL('@/assets/images/platform_logos/qq.png', import.meta.url).href
  } else if (name === 'wecom' || name === 'wecom_ai_bot') {
    return new URL('@/assets/images/platform_logos/wecom.png', import.meta.url).href
  } else if (name === 'weixin_official_account') {
    return new URL('@/assets/images/platform_logos/wechat.png', import.meta.url).href
  } else if (name === 'lark') {
    return new URL('@/assets/images/platform_logos/lark.png', import.meta.url).href
  } else if (name === 'dingtalk') {
    return new URL('@/assets/images/platform_logos/dingtalk.svg', import.meta.url).href
  } else if (name === 'telegram') {
    return new URL('@/assets/images/platform_logos/telegram.svg', import.meta.url).href
  } else if (name === 'discord') {
    return new URL('@/assets/images/platform_logos/discord.svg', import.meta.url).href
  } else if (name === 'slack') {
    return new URL('@/assets/images/platform_logos/slack.svg', import.meta.url).href
  } else if (name === 'kook') {
    return new URL('@/assets/images/platform_logos/kook.png', import.meta.url).href
  } else if (name === 'vocechat') {
    return new URL('@/assets/images/platform_logos/vocechat.png', import.meta.url).href
  } else if (name === 'satori' || name === 'Satori') {
    return new URL('@/assets/images/platform_logos/satori.png', import.meta.url).href
  } else if (name === 'misskey') {
    return new URL('@/assets/images/platform_logos/misskey.png', import.meta.url).href
  } else if (name === 'line') {
    return new URL('@/assets/images/platform_logos/line.png', import.meta.url).href
  }
}

/**
 * 获取平台教程链接
 * @param {string} platformType - 平台类型
 * @returns {string} 教程链接
 */
export function getTutorialLink(platformType) {
  const tutorialMap = {
    "qq_official_webhook": "https://docs.astrbot.app/deploy/platform/qqofficial/webhook.html",
    "qq_official": "https://docs.astrbot.app/deploy/platform/qqofficial/websockets.html",
    "aiocqhttp": "https://docs.astrbot.app/deploy/platform/aiocqhttp/napcat.html",
    "wecom": "https://docs.astrbot.app/deploy/platform/wecom.html",
    "wecom_ai_bot": "https://docs.astrbot.app/deploy/platform/wecom_ai_bot.html",
    "lark": "https://docs.astrbot.app/deploy/platform/lark.html",
    "telegram": "https://docs.astrbot.app/deploy/platform/telegram.html",
    "dingtalk": "https://docs.astrbot.app/deploy/platform/dingtalk.html",
    "weixin_official_account": "https://docs.astrbot.app/deploy/platform/weixin-official-account.html",
    "discord": "https://docs.astrbot.app/deploy/platform/discord.html",
    "slack": "https://docs.astrbot.app/deploy/platform/slack.html",
    "kook": "https://docs.astrbot.app/deploy/platform/kook.html",
    "vocechat": "https://docs.astrbot.app/deploy/platform/vocechat.html",
    "satori": "https://docs.astrbot.app/deploy/platform/satori/llonebot.html",
    "misskey": "https://docs.astrbot.app/deploy/platform/misskey.html",
  }
  return tutorialMap[platformType] || "https://docs.astrbot.app";
}

/**
 * 获取平台描述
 * @param {Object} template - 平台模板
 * @param {string} name - 平台名称
 * @returns {string} 平台描述
 */
export function getPlatformDescription(template, name) {
  // special judge for community platforms
  if (name.includes('vocechat')) {
    return t('src.utils.platformutils.provided_by_hikarifroya');
  } else if (name.includes('kook')) {
    return t('src.utils.platformutils.provided_by_wuyan1003')
  }
  return '';
}

/**
 * 获取平台展示名（用于插件支持平台显示）
 * @param {string} platformId - 平台适配器 ID
 * @returns {string}
 */
export function getPlatformDisplayName(platformId) {
  const displayNameMap = {
    aiocqhttp: 'aiocqhttp (OneBot v11)',
    qq_official: t('src.utils.platformutils.platform_qq_official_label'),
    weixin_official_account: t('src.utils.platformutils.platform_weixin_official_account_label'),
    wecom: t('src.utils.platformutils.platform_wecom_label'),
    wecom_ai_bot: t('src.utils.platformutils.platform_wecom_ai_bot_label'),
    lark: t('src.utils.platformutils.platform_lark_label'),
    dingtalk: t('src.utils.platformutils.platform_dingtalk_label'),
    telegram: 'telegram (Telegram)',
    discord: 'discord (Discord)',
    misskey: 'misskey (Misskey)',
    slack: 'slack (Slack)',
    kook: 'kook (KOOK)',
    vocechat: 'vocechat (VoceChat)',
    satori: 'satori (Satori)',
    line: 'line (LINE)',
  };
  return displayNameMap[platformId] || platformId;
}
