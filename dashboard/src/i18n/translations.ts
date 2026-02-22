import { buildStaticTranslations } from './module-discovery';

export const translations = buildStaticTranslations();

export const localeList = Object.freeze(Object.keys(translations).sort());

export type TranslationData = typeof translations;
