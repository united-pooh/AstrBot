import asyncio
import os
import sys
import traceback
from pathlib import Path

import click
from filelock import FileLock, Timeout

from astrbot.core.lang import t

from ..utils import check_astrbot_root, check_dashboard, get_astrbot_root


async def run_astrbot(astrbot_root: Path) -> None:
    """运行 AstrBot"""
    from astrbot.core import LogBroker, LogManager, db_helper, logger
    from astrbot.core.initial_loader import InitialLoader

    await check_dashboard(astrbot_root / "data")

    log_broker = LogBroker()
    LogManager.set_queue_handler(logger, log_broker)
    db = db_helper

    core_lifecycle = InitialLoader(db, log_broker)

    await core_lifecycle.start()


@click.option(
    "--reload",
    "-r",
    is_flag=True,
    help=t("cli-commands-cmd_run-option_plugin_auto_reload"),
)
@click.option(
    "--port",
    "-p",
    help=t("cli-commands-cmd_run-option_dashboard_port"),
    required=False,
    type=str,
)
@click.command()
def run(reload: bool, port: str) -> None:
    """运行 AstrBot"""
    try:
        os.environ["ASTRBOT_CLI"] = "1"
        astrbot_root = get_astrbot_root()

        if not check_astrbot_root(astrbot_root):
            raise click.ClickException(
                t(
                    "cli-commands-cmd_run-invalid_astrbot_root_dir",
                    astrbot_root=astrbot_root,
                ),
            )

        os.environ["ASTRBOT_ROOT"] = str(astrbot_root)
        sys.path.insert(0, str(astrbot_root))

        if port:
            os.environ["DASHBOARD_PORT"] = port

        if reload:
            click.echo(t("cli-commands-cmd_run-enabled_plugin_auto_reload"))
            os.environ["ASTRBOT_RELOAD"] = "1"

        lock_file = astrbot_root / "astrbot.lock"
        lock = FileLock(lock_file, timeout=5)
        with lock.acquire():
            asyncio.run(run_astrbot(astrbot_root))
    except KeyboardInterrupt:
        click.echo(t("cli-commands-cmd_run-astrbot_shut_down"))
    except Timeout:
        raise click.ClickException(t("cli-commands-cmd_run-cannot_acquire_lock_file"))
    except Exception as e:
        raise click.ClickException(
            t(
                "cli-commands-cmd_run-runtime_error",
                e=e,
                format_exc=traceback.format_exc(),
            )
        )
