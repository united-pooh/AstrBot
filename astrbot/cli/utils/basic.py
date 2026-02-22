from pathlib import Path

import click

from astrbot.core.lang import t


def check_astrbot_root(path: str | Path) -> bool:
    """检查路径是否为 AstrBot 根目录"""
    if not isinstance(path, Path):
        path = Path(path)
    if not path.exists() or not path.is_dir():
        return False
    if not (path / ".astrbot").exists():
        return False
    return True


def get_astrbot_root() -> Path:
    """获取Astrbot根目录路径"""
    return Path.cwd()


async def check_dashboard(astrbot_root: Path) -> None:
    """检查是否安装了dashboard"""
    from astrbot.core.config.default import VERSION
    from astrbot.core.utils.io import download_dashboard, get_dashboard_version

    from .version_comparator import VersionComparator

    try:
        dashboard_version = await get_dashboard_version()
        match dashboard_version:
            case None:
                click.echo(t("cli-utils-basic-management_panel_not_installed"))
                if click.confirm(
                    t("cli-utils-basic-ask_install_management_panel"),
                    default=True,
                    abort=True,
                ):
                    click.echo(t("cli-utils-basic-installing_management_panel"))
                    await download_dashboard(
                        path="data/dashboard.zip",
                        extract_path=str(astrbot_root),
                        version=f"v{VERSION}",
                        latest=False,
                    )
                    click.echo(t("cli-utils-basic-management_panel_installed"))

            case str():
                if VersionComparator.compare_version(VERSION, dashboard_version) <= 0:
                    click.echo(t("cli-utils-basic-management_panel_up_to_date"))
                    return
                try:
                    version = dashboard_version.split("v")[1]
                    click.echo(
                        t(
                            "cli-utils-basic-management_panel_version_display",
                            version=version,
                        )
                    )
                    await download_dashboard(
                        path="data/dashboard.zip",
                        extract_path=str(astrbot_root),
                        version=f"v{VERSION}",
                        latest=False,
                    )
                except Exception as e:
                    click.echo(
                        t("cli-utils-basic-download_management_panel_failed", e=e)
                    )
                    return
    except FileNotFoundError:
        click.echo(t("cli-utils-basic-initializing_management_panel_dir"))
        try:
            await download_dashboard(
                path=str(astrbot_root / "dashboard.zip"),
                extract_path=str(astrbot_root),
                version=f"v{VERSION}",
                latest=False,
            )
            click.echo(t("cli-utils-basic-management_panel_init_completed"))
        except Exception as e:
            click.echo(t("cli-utils-basic-management_panel_download_failed", e=e))
            return
