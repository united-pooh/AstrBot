type JsonRecord = Record<string, unknown>;
type JsonModuleExport = { default: JsonRecord } | JsonRecord;
type JsonModuleImporter = () => Promise<JsonModuleExport>;

export interface DiscoveredModule {
  name: string;
  path: string;
  sourcePath: string;
}

const MODULE_PATH_RE = /^\.\/locales\/([^/]+)\/(.+)\.json$/;

const MODULE_SEGMENT_ALIASES: Record<string, string> = {
  'tool-use': 'tooluse',
};

const EAGER_MODULES = import.meta.glob('./locales/*/**/*.json', {
  eager: true,
}) as Record<string, JsonModuleExport>;

const LAZY_MODULES = import.meta.glob('./locales/*/**/*.json') as Record<
  string,
  JsonModuleImporter
>;

function unwrapModule(moduleExport: JsonModuleExport): JsonRecord {
  if (
    moduleExport &&
    typeof moduleExport === 'object' &&
    'default' in moduleExport
  ) {
    return moduleExport.default as JsonRecord;
  }
  return moduleExport as JsonRecord;
}

function normalizeSegment(segment: string): string {
  return MODULE_SEGMENT_ALIASES[segment] ?? segment;
}

function normalizeModuleName(moduleName: string): string {
  return moduleName
    .split('/')
    .map((segment) => normalizeSegment(segment))
    .join('/');
}

function parseModulePath(sourcePath: string): {
  locale: string;
  moduleName: string;
  relativePath: string;
  segments: string[];
} | null {
  const match = sourcePath.match(MODULE_PATH_RE);
  if (!match) {
    return null;
  }

  const [, locale, relativeWithoutExt] = match;
  const rawSegments = relativeWithoutExt.split('/');
  const normalizedSegments = rawSegments.map((segment) => normalizeSegment(segment));

  return {
    locale,
    moduleName: normalizedSegments.join('/'),
    relativePath: `${relativeWithoutExt}.json`,
    segments: normalizedSegments,
  };
}

function assignNestedValue(
  target: Record<string, unknown>,
  segments: string[],
  value: JsonRecord,
) {
  let current: Record<string, unknown> = target;

  for (let i = 0; i < segments.length - 1; i += 1) {
    const segment = segments[i];
    const next = current[segment];

    if (!next || typeof next !== 'object' || Array.isArray(next)) {
      current[segment] = {};
    }

    current = current[segment] as Record<string, unknown>;
  }

  const lastSegment = segments[segments.length - 1];
  const existing = current[lastSegment];

  if (existing && typeof existing === 'object' && !Array.isArray(existing)) {
    current[lastSegment] = { ...(existing as JsonRecord), ...value };
    return;
  }

  current[lastSegment] = value;
}

export function buildStaticTranslations(): Record<string, Record<string, unknown>> {
  const messagesByLocale: Record<string, Record<string, unknown>> = {};
  const entries = Object.entries(EAGER_MODULES).sort(([a], [b]) => a.localeCompare(b));

  for (const [sourcePath, moduleExport] of entries) {
    const parsed = parseModulePath(sourcePath);
    if (!parsed) {
      continue;
    }

    if (!messagesByLocale[parsed.locale]) {
      messagesByLocale[parsed.locale] = {};
    }

    assignNestedValue(
      messagesByLocale[parsed.locale],
      parsed.segments,
      unwrapModule(moduleExport),
    );
  }

  return messagesByLocale;
}

export function discoverModules(): DiscoveredModule[] {
  const discovered = new Map<string, DiscoveredModule>();
  const entries = Object.keys(EAGER_MODULES).sort();

  for (const sourcePath of entries) {
    const parsed = parseModulePath(sourcePath);
    if (!parsed) {
      continue;
    }

    if (discovered.has(parsed.moduleName)) {
      continue;
    }

    discovered.set(parsed.moduleName, {
      name: parsed.moduleName,
      path: parsed.relativePath,
      sourcePath,
    });
  }

  return Array.from(discovered.values());
}

export function getLazyModuleLoaders(): Record<string, JsonModuleImporter> {
  return LAZY_MODULES;
}

export function resolveLazyLoaderKey(locale: string, modulePath: string): string {
  return `./locales/${locale}/${modulePath}`;
}

export function normalizeRequestedModuleName(moduleName: string): string {
  return normalizeModuleName(moduleName);
}
