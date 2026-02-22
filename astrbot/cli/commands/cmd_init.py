import asyncio
from pathlib import Path

import click
from filelock import FileLock, Timeout

from astrbot.core.lang import t

from ..utils import check_dashboard, get_astrbot_root


async def initialize_astrbot(astrbot_root: Path) -> None:
    """执行 AstrBot 初始化逻辑"""
    dot_astrbot = astrbot_root / ".astrbot"

    if not dot_astrbot.exists():
        click.echo(f"Current Directory: {astrbot_root}")
        click.echo(
            t("cli-commands-cmd_init-create_marker_file"),
        )
        if click.confirm(
            t("cli-commands-cmd_init-confirm_directory", astrbot_root=astrbot_root),
            default=True,
            abort=True,
        ):
            dot_astrbot.touch()
            click.echo(f"Created {dot_astrbot}")

    paths = {
        "data": astrbot_root / "data",
        "config": astrbot_root / "data" / "config",
        "plugins": astrbot_root / "data" / "plugins",
        "temp": astrbot_root / "data" / "temp",
    }

    for name, path in paths.items():
        path.mkdir(parents=True, exist_ok=True)
        click.echo(f"{'Created' if not path.exists() else 'Directory exists'}: {path}")

    await check_dashboard(astrbot_root / "data")


@click.command()
def init() -> None:
    """初始化 AstrBot"""
    click.echo("Initializing AstrBot...")
    astrbot_root = get_astrbot_root()
    lock_file = astrbot_root / "astrbot.lock"
    lock = FileLock(lock_file, timeout=5)

    try:
        with lock.acquire():
            asyncio.run(initialize_astrbot(astrbot_root))
    except Timeout:
        raise click.ClickException(t("cli-commands-cmd_init-lock_acquisition_failed"))

    except Exception as e:
        raise click.ClickException(t("cli-commands-cmd_init-init_failed", e=e))
