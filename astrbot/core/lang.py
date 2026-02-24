# lang.py
from pathlib import Path

from fluent.runtime import FluentLocalization, FluentResourceLoader

from astrbot.core.utils.astrbot_path import get_astrbot_path


class Lang:
    def __init__(
        self,
        locale: str = "zh-cn",
        files: list[str] | None = None,
        namespace_paths: dict[str, str | Path] | None = None,
        namespace_files: dict[str, list[str]] | None = None,
        default_namespace: str = "default",
    ):
        self.locale = locale
        self.files = files
        self.default_namespace = default_namespace

        base_dir = Path(get_astrbot_path()) / "astrbot" / "i18n" / "locales"
        if namespace_paths is None:
            self.namespace_paths: dict[str, Path] = {self.default_namespace: base_dir}
        else:
            self.namespace_paths = {
                namespace: Path(path) for namespace, path in namespace_paths.items()
            }
            if self.default_namespace not in self.namespace_paths:
                self.namespace_paths[self.default_namespace] = base_dir

        self.namespace_files = namespace_files or {}
        self.available_locales: list[str] = []
        self.available_locales_by_namespace: dict[str, list[str]] = {}
        self._l10n_map: dict[str, FluentLocalization] = {}
        self.load_locale(self.locale, self.files)

    @staticmethod
    def _collect_files(base_dir: Path, files: list[str] | None) -> list[str]:
        if files is not None:
            return files

        files_set = set()
        for locale_dir in (d for d in base_dir.iterdir() if d.is_dir()):
            for ftl_file in locale_dir.glob("*.ftl"):
                files_set.add(ftl_file.name)
        return sorted(files_set)

    @staticmethod
    def _match_locale(available_locales: list[str], locale: str) -> str:
        return next(
            (
                locale_name
                for locale_name in available_locales
                if locale_name.lower() == locale.lower()
            ),
            locale,
        )

    def _build_localization(
        self, base_dir: Path, locale: str, files: list[str] | None
    ) -> tuple[FluentLocalization, list[str]]:
        if not base_dir.exists() or not base_dir.is_dir():
            raise ValueError(f"Locale directory does not exist: {base_dir}")

        available_locales = [d.name for d in base_dir.iterdir() if d.is_dir()]
        if not available_locales:
            raise ValueError(f"No locale directories found under: {base_dir}")

        matched_locale = self._match_locale(available_locales, locale)
        merged_files = self._collect_files(base_dir, files)
        loader = FluentResourceLoader(str(base_dir / "{locale}"))

        locales_preference = [matched_locale]
        if "zh-cn" in available_locales and matched_locale.lower() != "zh-cn":
            locales_preference.append("zh-cn")

        return FluentLocalization(
            locales_preference, merged_files, loader
        ), available_locales

    def load_locale(
        self,
        locale: str = "zh-cn",
        files: list[str] | None = None,
        namespace_paths: dict[str, str | Path] | None = None,
        namespace_files: dict[str, list[str]] | None = None,
    ):
        if namespace_paths is not None:
            self.namespace_paths = {
                namespace: Path(path) for namespace, path in namespace_paths.items()
            }
            if self.default_namespace not in self.namespace_paths:
                base_dir = Path(get_astrbot_path()) / "astrbot" / "i18n" / "locales"
                self.namespace_paths[self.default_namespace] = base_dir
        if namespace_files is not None:
            self.namespace_files = namespace_files

        self.locale = locale
        if files is not None:
            self.files = files

        l10n_map: dict[str, FluentLocalization] = {}
        available_by_namespace: dict[str, list[str]] = {}
        for namespace, base_dir in self.namespace_paths.items():
            ns_files = self.namespace_files.get(namespace, self.files)
            l10n, available_locales = self._build_localization(
                base_dir, locale, ns_files
            )
            l10n_map[namespace] = l10n
            available_by_namespace[namespace] = available_locales

        self._l10n_map = l10n_map
        self.available_locales_by_namespace = available_by_namespace
        self.available_locales = available_by_namespace.get(
            self.default_namespace,
            sorted(set().union(*available_by_namespace.values())),
        )

    def _resolve_key(self, key: str) -> tuple[str, str]:
        if "." not in key:
            return self.default_namespace, key

        namespace, real_key = key.split(".", 1)
        if namespace in self._l10n_map and real_key:
            return namespace, real_key
        return self.default_namespace, key

    def __call__(self, key: str, **kwargs) -> str:
        namespace, real_key = self._resolve_key(key)
        l10n = self._l10n_map.get(namespace) or self._l10n_map[self.default_namespace]
        return l10n.format_value(real_key, kwargs)


t = Lang(locale="zh-cn")
