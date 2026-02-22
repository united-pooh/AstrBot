import re
import shutil
from pathlib import Path

import click

from astrbot.core.lang import t

from ..utils import (
    PluginStatus,
    build_plug_list,
    check_astrbot_root,
    get_astrbot_root,
    get_git_repo,
    manage_plugin,
)


@click.group()
def plug() -> None:
    """插件管理"""


def _get_data_path() -> Path:
    base = get_astrbot_root()
    if not check_astrbot_root(base):
        raise click.ClickException(
            t("cli-commands-cmd_plug-invalid_root_dir", base=base),
        )
    return (base / "data").resolve()


def display_plugins(plugins, title=None, color=None) -> None:
    if title:
        click.echo(click.style(title, fg=color, bold=True))

    click.echo(t("cli-commands-cmd_plug-list_header"))
    click.echo("-" * 85)

    for p in plugins:
        desc = p["desc"][:30] + ("..." if len(p["desc"]) > 30 else "")
        click.echo(
            f"{p['name']:<20} {p['version']:<10} {p['status']:<10} "
            f"{p['author']:<15} {desc:<30}",
        )


@plug.command()
@click.argument("name")
def new(name: str) -> None:
    """创建新插件"""
    base_path = _get_data_path()
    plug_path = base_path / "plugins" / name

    if plug_path.exists():
        raise click.ClickException(
            t("cli-commands-cmd_plug-plugin_already_exists", name=name)
        )

    author = click.prompt(t("cli-commands-cmd_plug-prompt_author"), type=str)
    desc = click.prompt(t("cli-commands-cmd_plug-prompt_description"), type=str)
    version = click.prompt(t("cli-commands-cmd_plug-prompt_version"), type=str)
    if not re.match(r"^\d+\.\d+(\.\d+)?$", version.lower().lstrip("v")):
        raise click.ClickException(t("cli-commands-cmd_plug-invalid_version_format"))
    repo = click.prompt(t("cli-commands-cmd_plug-prompt_repository"), type=str)
    if not repo.startswith("http"):
        raise click.ClickException(t("cli-commands-cmd_plug-invalid_repo_url"))

    click.echo(t("cli-commands-cmd_plug-downloading_template"))
    get_git_repo(
        "https://github.com/Soulter/helloworld",
        plug_path,
    )

    click.echo(t("cli-commands-cmd_plug-rewriting_info"))
    # 重写 metadata.yaml
    with open(plug_path / "metadata.yaml", "w", encoding="utf-8") as f:
        f.write(
            f"name: {name}\n"
            f"desc: {desc}\n"
            f"version: {version}\n"
            f"author: {author}\n"
            f"repo: {repo}\n",
        )

    # 重写 README.md
    with open(plug_path / "README.md", "w", encoding="utf-8") as f:
        f.write(t("cli-commands-cmd_plug-write_readme_content", name=name, desc=desc))

    # 重写 main.py
    with open(plug_path / "main.py", encoding="utf-8") as f:
        content = f.read()

    new_content = content.replace(
        t("cli-commands-cmd_plug-example_register_decorator"),
        f'@register("{name}", "{author}", "{desc}", "{version}")',
    )

    with open(plug_path / "main.py", "w", encoding="utf-8") as f:
        f.write(new_content)

    click.echo(t("cli-commands-cmd_plug-plugin_created_success", name=name))


@plug.command()
@click.option(
    "--all", "-a", is_flag=True, help=t("cli-commands-cmd_plug-option_list_all")
)
def list(all: bool) -> None:
    """列出插件"""
    base_path = _get_data_path()
    plugins = build_plug_list(base_path / "plugins")

    # 未发布的插件
    not_published_plugins = [
        p for p in plugins if p["status"] == PluginStatus.NOT_PUBLISHED
    ]
    if not_published_plugins:
        display_plugins(
            not_published_plugins, t("cli-commands-cmd_plug-display_unpublished"), "red"
        )

    # 需要更新的插件
    need_update_plugins = [
        p for p in plugins if p["status"] == PluginStatus.NEED_UPDATE
    ]
    if need_update_plugins:
        display_plugins(
            need_update_plugins,
            t("cli-commands-cmd_plug-display_needs_update"),
            "yellow",
        )

    # 已安装的插件
    installed_plugins = [p for p in plugins if p["status"] == PluginStatus.INSTALLED]
    if installed_plugins:
        display_plugins(
            installed_plugins, t("cli-commands-cmd_plug-display_installed"), "green"
        )

    # 未安装的插件
    not_installed_plugins = [
        p for p in plugins if p["status"] == PluginStatus.NOT_INSTALLED
    ]
    if not_installed_plugins and all:
        display_plugins(
            not_installed_plugins,
            t("cli-commands-cmd_plug-display_not_installed"),
            "blue",
        )

    if (
        not any([not_published_plugins, need_update_plugins, installed_plugins])
        and not all
    ):
        click.echo(t("cli-commands-cmd_plug-no_plugins_installed"))


@plug.command()
@click.argument("name")
@click.option("--proxy", help=t("cli-commands-cmd_plug-option_proxy"))
def install(name: str, proxy: str | None) -> None:
    """安装插件"""
    base_path = _get_data_path()
    plug_path = base_path / "plugins"
    plugins = build_plug_list(base_path / "plugins")

    plugin = next(
        (
            p
            for p in plugins
            if p["name"] == name and p["status"] == PluginStatus.NOT_INSTALLED
        ),
        None,
    )

    if not plugin:
        raise click.ClickException(
            t("cli-commands-cmd_plug-plugin_not_found_or_installed", name=name)
        )

    manage_plugin(plugin, plug_path, is_update=False, proxy=proxy)


@plug.command()
@click.argument("name")
def remove(name: str) -> None:
    """卸载插件"""
    base_path = _get_data_path()
    plugins = build_plug_list(base_path / "plugins")
    plugin = next((p for p in plugins if p["name"] == name), None)

    if not plugin or not plugin.get("local_path"):
        raise click.ClickException(
            t("cli-commands-cmd_plug-plugin_not_exist_or_not_installed", name=name)
        )

    plugin_path = plugin["local_path"]

    click.confirm(
        t("cli-commands-cmd_plug-confirm_uninstall_plugin", name=name),
        default=False,
        abort=True,
    )

    try:
        shutil.rmtree(plugin_path)
        click.echo(t("cli-commands-cmd_plug-plugin_uninstalled_success", name=name))
    except Exception as e:
        raise click.ClickException(
            t("cli-commands-cmd_plug-uninstall_plugin_failed", name=name, e=e)
        )


@plug.command()
@click.argument("name", required=False)
@click.option("--proxy", help=t("cli-commands-cmd_plug-option_github_proxy"))
def update(name: str, proxy: str | None) -> None:
    """更新插件"""
    base_path = _get_data_path()
    plug_path = base_path / "plugins"
    plugins = build_plug_list(base_path / "plugins")

    if name:
        plugin = next(
            (
                p
                for p in plugins
                if p["name"] == name and p["status"] == PluginStatus.NEED_UPDATE
            ),
            None,
        )

        if not plugin:
            raise click.ClickException(
                t(
                    "cli-commands-cmd_plug-plugin_no_update_needed_or_impossible",
                    name=name,
                )
            )

        manage_plugin(plugin, plug_path, is_update=True, proxy=proxy)
    else:
        need_update_plugins = [
            p for p in plugins if p["status"] == PluginStatus.NEED_UPDATE
        ]

        if not need_update_plugins:
            click.echo(t("cli-commands-cmd_plug-no_plugins_to_update"))
            return

        click.echo(
            t(
                "cli-commands-cmd_plug-plugins_need_update",
                need_update_plugins=need_update_plugins,
            )
        )
        for plugin in need_update_plugins:
            plugin_name = plugin["name"]
            click.echo(
                t("cli-commands-cmd_plug-updating_plugin", plugin_name=plugin_name)
            )
            manage_plugin(plugin, plug_path, is_update=True, proxy=proxy)


@plug.command()
@click.argument("query")
def search(query: str) -> None:
    """搜索插件"""
    base_path = _get_data_path()
    plugins = build_plug_list(base_path / "plugins")

    matched_plugins = [
        p
        for p in plugins
        if query.lower() in p["name"].lower()
        or query.lower() in p["desc"].lower()
        or query.lower() in p["author"].lower()
    ]

    if not matched_plugins:
        click.echo(t("cli-commands-cmd_plug-no_matching_plugins", query=query))
        return

    display_plugins(
        matched_plugins,
        t("cli-commands-cmd_plug-display_search_results", query=query),
        "cyan",
    )
