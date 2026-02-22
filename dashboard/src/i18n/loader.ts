import { t } from '@/i18n/composables';
import {
  discoverModules,
  getLazyModuleLoaders,
  normalizeRequestedModuleName,
  resolveLazyLoaderKey,
} from './module-discovery';

export interface LoaderCache {
  [key: string]: unknown;
}

export interface ModuleInfo {
  name: string;
  path: string;
  loaded: boolean;
  data?: unknown;
}

type JsonModuleExport = { default: Record<string, unknown> } | Record<string, unknown>;

const lazyModuleLoaders = getLazyModuleLoaders();
const discoveredModules = discoverModules();

function unwrapJsonModule(moduleExport: JsonModuleExport): Record<string, unknown> {
  if (
    moduleExport &&
    typeof moduleExport === 'object' &&
    'default' in moduleExport
  ) {
    return moduleExport.default as Record<string, unknown>;
  }
  return moduleExport as Record<string, unknown>;
}

/**
 * Dynamic I18n Loader
 * 动态国际化加载器，支持按需加载和缓存机制
 */
export class I18nLoader {
  private cache: Map<string, unknown> = new Map();
  private moduleRegistry: Map<string, ModuleInfo> = new Map();

  constructor() {
    this.registerModules();
  }

  /**
   * 注册所有可用的翻译模块（自动发现）
   */
  private registerModules(): void {
    discoveredModules.forEach((module) => {
      this.moduleRegistry.set(module.name, {
        name: module.name,
        path: module.path,
        loaded: false,
      });
    });
  }

  /**
   * 加载单个模块
   */
  async loadModule(locale: string, moduleName: string): Promise<Record<string, unknown>> {
    const normalizedModuleName = normalizeRequestedModuleName(moduleName);
    const cacheKey = `${locale}:${normalizedModuleName}`;

    // 检查缓存
    if (this.cache.has(cacheKey)) {
      return this.cache.get(cacheKey) as Record<string, unknown>;
    }

    const moduleInfo = this.moduleRegistry.get(normalizedModuleName);
    if (!moduleInfo) {
      console.warn(
        t('src.i18n.loader.module_not_registered', { moduleName: normalizedModuleName }),
      );
      return {};
    }

    const loaderKey = resolveLazyLoaderKey(locale, moduleInfo.path);
    const moduleLoader = lazyModuleLoaders[loaderKey];
    if (!moduleLoader) {
      console.warn(
        t('src.i18n.loader.module_not_registered', {
          moduleName: `${normalizedModuleName}@${locale}`,
        }),
      );
      return {};
    }

    try {
      const loadedModule = (await moduleLoader()) as JsonModuleExport;
      const data = unwrapJsonModule(loadedModule);

      // 缓存结果
      this.cache.set(cacheKey, data);

      // 更新模块信息
      moduleInfo.loaded = true;
      moduleInfo.data = data;

      return data;
    } catch (error) {
      console.error(
        t('src.i18n.loader.failed_to_load_module', { moduleName: normalizedModuleName }),
        error,
      );
      return {};
    }
  }

  /**
   * 通用模块加载器 - 减少重复代码，提高可维护性
   */
  private async loadModules(
    locale: string,
    prefix: string,
    overrideList: string[] = [],
  ): Promise<Record<string, unknown>> {
    // 使用覆盖列表或从注册表中筛选符合前缀的模块名
    const moduleNames =
      overrideList.length > 0
        ? overrideList.map((moduleName) => normalizeRequestedModuleName(moduleName))
        : Array.from(this.moduleRegistry.keys()).filter((key) =>
            key.startsWith(`${prefix}/`),
          );

    const results = await Promise.all(
      moduleNames.map((moduleName) => this.loadModule(locale, moduleName)),
    );

    return this.mergeModules(results, moduleNames);
  }

  /**
   * 加载核心模块（最高优先级）
   */
  async loadCoreModules(locale: string): Promise<Record<string, unknown>> {
    return this.loadModules(locale, 'core');
  }

  /**
   * 加载功能模块
   */
  async loadFeatureModules(
    locale: string,
    features?: string[],
  ): Promise<Record<string, unknown>> {
    return this.loadModules(locale, 'features', features || []);
  }

  /**
   * 加载消息模块
   */
  async loadMessageModules(locale: string): Promise<Record<string, unknown>> {
    return this.loadModules(locale, 'messages');
  }

  /**
   * 加载所有模块
   */
  async loadAllModules(locale: string): Promise<Record<string, unknown>> {
    const [core, features, messages] = await Promise.all([
      this.loadCoreModules(locale),
      this.loadFeatureModules(locale),
      this.loadMessageModules(locale),
    ]);

    return {
      ...core,
      ...features,
      ...messages,
    };
  }

  /**
   * 加载完整语言包（所有模块合并）
   */
  async loadLocale(locale: string): Promise<Record<string, unknown>> {
    return this.loadAllModules(locale);
  }

  /**
   * 合并多个模块数据
   */
  private mergeModules(
    modules: Record<string, unknown>[],
    moduleNames: string[],
  ): Record<string, unknown> {
    const result: Record<string, unknown> = {};
    const pathRegistry = new Map<string, string>();

    modules.forEach((module, index) => {
      const moduleName = moduleNames[index];
      const nameParts = moduleName.split('/');

      // 构建嵌套对象结构（对所有模块统一处理）
      let current = result as Record<string, unknown>;
      for (let i = 0; i < nameParts.length - 1; i += 1) {
        const part = nameParts[i];
        const next = current[part];
        if (!next || typeof next !== 'object' || Array.isArray(next)) {
          current[part] = {};
        }
        current = current[part] as Record<string, unknown>;
      }

      // 冲突检测：检查最终键是否已存在
      const finalKey = nameParts[nameParts.length - 1];
      const fullPath = nameParts.join('.');
      const existingModule = pathRegistry.get(fullPath);

      if (current[finalKey] && existingModule) {
        console.warn(
          t('src.i18n.loader.i18n_module_path_conflict', {
            fullPath,
            existingModule,
            moduleName,
          }),
        );
      }

      // 记录路径和模块名的映射
      pathRegistry.set(fullPath, moduleName);

      // 设置最终值（保持原有的浅合并行为）
      if (current[finalKey] && typeof current[finalKey] === 'object') {
        current[finalKey] = {
          ...(current[finalKey] as Record<string, unknown>),
          ...module,
        };
      } else {
        current[finalKey] = module;
      }
    });

    return result;
  }

  /**
   * 预加载关键模块
   */
  async preloadEssentials(locale: string): Promise<void> {
    const essentials = ['core/common', 'core/navigation', 'features/chat'];
    await Promise.all(essentials.map((moduleName) => this.loadModule(locale, moduleName)));
  }

  /**
   * 清理缓存
   */
  clearCache(locale?: string): void {
    if (locale) {
      // 清理特定语言的缓存
      const keys = Array.from(this.cache.keys()).filter((key: string) =>
        key.startsWith(`${locale}:`),
      );
      keys.forEach((key: string) => this.cache.delete(key));
      return;
    }
    // 清理所有缓存
    this.cache.clear();
  }

  /**
   * 获取加载状态
   */
  getLoadingStatus(): { total: number; loaded: number; modules: ModuleInfo[] } {
    const modules = Array.from(this.moduleRegistry.values());
    const loaded = modules.filter((module) => module.loaded).length;

    return {
      total: modules.length,
      loaded,
      modules,
    };
  }

  /**
   * 热重载模块
   */
  async reloadModule(locale: string, moduleName: string): Promise<Record<string, unknown>> {
    const normalizedModuleName = normalizeRequestedModuleName(moduleName);
    const cacheKey = `${locale}:${normalizedModuleName}`;
    this.cache.delete(cacheKey);

    const moduleInfo = this.moduleRegistry.get(normalizedModuleName);
    if (moduleInfo) {
      moduleInfo.loaded = false;
    }

    return this.loadModule(locale, normalizedModuleName);
  }
}
