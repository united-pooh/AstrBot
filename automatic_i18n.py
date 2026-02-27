"""
从 Python 源文件中提取 logger / print / click.echo / raise XxxError 的消息，
转换为 FTL 格式，并将含变量的调用重写为 t("id", key=val) 形式。
扫描所有 .py 文件并将 FTL 条目统一输出到 astrbot/i18n/locales/zh-cn/** 下。
"""

import ast
import hashlib
import re
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# ID 生成：取消息内容的 MD5 前8位，相同内容永远生成同一个 id（幂等）
# ---------------------------------------------------------------------------


def make_id(ftl_value: str) -> str:
    digest = hashlib.md5(ftl_value.encode()).hexdigest()[:8]
    return f"msg-{digest}"


# ---------------------------------------------------------------------------
# 字符串表达式解析：提取 FTL 值 + 变量参数列表
# 返回 (ftl_value, kwargs) 或 None
#   ftl_value : FTL 格式字符串，如 "{$date}相反的你和我"
#   kwargs    : [(参数名, 源码表达式)] 列表，如 [("date", "date")]
# 纯字符串常量返回 ("原始字符串", [])，kwargs 为空表示无需替换
# ---------------------------------------------------------------------------


def extract_string_expr(node):
    # 纯字符串常量
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value, []

    # f-string
    if isinstance(node, ast.JoinedStr):
        return parse_fstring(node)

    # "..." % var 或 "..." % (var1, var2)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mod):
        return parse_percent_format(node)

    # "...".format(...)
    if (
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr == "format"
        and isinstance(node.func.value, ast.Constant)
        and isinstance(node.func.value.value, str)
    ):
        return parse_str_format(node)

    # 裸变量：logger.info(var) → "{$var}"
    if isinstance(node, ast.Name):
        return "{$" + node.id + "}", [(node.id, node.id)]

    # 裸函数调用：logger.info(get_msg()) → "{$res}"
    if isinstance(node, ast.Call):
        return "{$res}", [("res", ast.unparse(node))]

    return None


def parse_fstring(node: ast.JoinedStr):
    res_counter = [0]
    parts = []
    kwargs = []

    for value in node.values:
        if isinstance(value, ast.Constant):
            parts.append(str(value.value))
        elif isinstance(value, ast.FormattedValue):
            param, src = get_param_and_src(value.value, res_counter)
            parts.append("{$" + param + "}")
            kwargs.append((param, src))

    return "".join(parts), kwargs


def parse_percent_format(node: ast.BinOp):
    if not (isinstance(node.left, ast.Constant) and isinstance(node.left.value, str)):
        return None

    template = node.left.value
    right = node.right
    arg_nodes = list(right.elts) if isinstance(right, ast.Tuple) else [right]

    res_counter = [0]
    kwargs = []

    def replacer(m):
        fmt_letter = m.group(0)[-1]
        if fmt_letter == "%":
            return "%"
        if arg_nodes:
            param, src = get_param_and_src(arg_nodes.pop(0), res_counter, fmt_letter)
            kwargs.append((param, src))
            return "{$" + param + "}"
        return m.group(0)

    ftl_value = re.sub(r"%(?:\(\w+\))?[-+0-9*.]*[sdfrx%]", replacer, template)
    return ftl_value, kwargs


def parse_str_format(node: ast.Call):
    template = node.func.value.value
    res_counter = [0]

    # 命名占位符映射：占位符名 → (参数名, 源码表达式)
    kw_map = {}
    for kw in node.keywords:
        if kw.arg:
            kw_map[kw.arg] = (kw.arg, ast.unparse(kw.value))

    # 位置参数列表
    pos_args = [get_param_and_src(a, res_counter, "val") for a in node.args]

    kwargs = []

    def replacer(m):
        field = m.group(1).split(":")[0].strip()
        if field == "" or field.isdigit():
            idx = int(field) if field.isdigit() else 0
            param, src = pos_args[idx] if idx < len(pos_args) else ("arg", "arg")
        else:
            param, src = kw_map.get(field, (field, field))
        kwargs.append((param, src))
        return "{$" + param + "}"

    ftl_value = re.sub(r"\{([^{}]*)\}", replacer, template)
    return ftl_value, kwargs


def get_param_and_src(node, res_counter: list, fmt_letter: str = "val"):
    """返回 (参数名, 源码表达式字符串)"""
    if isinstance(node, ast.Name):
        return node.id, node.id
    if isinstance(node, ast.Constant):
        return fmt_letter, repr(node.value)
    # 复杂表达式 / 函数调用
    res_counter[0] += 1
    count = res_counter[0]
    param = "res_" + str(count) if count > 1 else "res"
    return param, ast.unparse(node)


# ---------------------------------------------------------------------------
# 目标调用判断
# ---------------------------------------------------------------------------


def is_logger_call(node: ast.Call) -> bool:
    """判断是否为 logger.info / warning / warn / error / debug / critical / exception"""
    func = node.func
    return (
        isinstance(func, ast.Attribute)
        and func.attr
        in ("info", "warning", "warn", "error", "debug", "critical", "exception")
        and isinstance(func.value, ast.Name)
    )


def is_print_call(node: ast.Call) -> bool:
    """判断是否为 print(...)"""
    return isinstance(node.func, ast.Name) and node.func.id == "print"


def is_click_echo_call(node: ast.Call) -> bool:
    """判断是否为 click.echo(...)"""
    func = node.func
    return (
        isinstance(func, ast.Attribute)
        and func.attr == "echo"
        and isinstance(func.value, ast.Name)
        and func.value.id == "click"
    )


def is_exception_call(node: ast.Call) -> bool:
    """判断是否为 XxxError(...) 或 XxxException(...) 的实例化"""
    func = node.func
    # 支持 ValueError(...) 和 module.ValueError(...) 两种形式
    name = (
        func.id
        if isinstance(func, ast.Name)
        else (func.attr if isinstance(func, ast.Attribute) else "")
    )
    return name.endswith("Error") or name.endswith("Exception")


def is_target_call(node: ast.Call) -> bool:
    return (
        is_logger_call(node)
        or is_print_call(node)
        or is_click_echo_call(node)
        or is_exception_call(node)
    )


# ---------------------------------------------------------------------------
# 核心：提取 + 重写
# ---------------------------------------------------------------------------


def extract_and_rewrite(source: str):
    """
    解析源码，找出所有含变量的目标调用，返回：
      ftl_entries : [(id, ftl_value), ...]
      new_source  : 将含变量的第一个参数替换为 t("id", key=val) 后的源码
    纯字符串（无变量）的调用保持原样不动。
    """
    try:
        tree = ast.parse(source)
    except Exception as e:
        print(f"Error parsing source: {e}")
        return [], source

    # 收集替换信息：(起始偏移, 结束偏移, 新文本, msg_id, ftl_value)
    replacements = []

    # 预计算每行的字符偏移量
    line_offsets = []
    offset = 0
    for line in source.splitlines(keepends=True):
        line_offsets.append(offset)
        offset += len(line)

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not is_target_call(node):
            continue
        if not node.args:
            continue

        # 第一个参数已经是 t(...) 调用，说明已处理过，跳过
        first = node.args[0]
        if (
            isinstance(first, ast.Call)
            and isinstance(first.func, ast.Name)
            and first.func.id == "t"
        ):
            continue

        result = extract_string_expr(node.args[0])
        if result is None:
            continue

        ftl_value, kwargs = result

        msg_id = make_id(ftl_value)

        # 构造新的第一个参数：t("id", key=val, ...)
        kw_parts = ", ".join(f"{p}={s}" for p, s in kwargs)
        t_call = f't("{msg_id}", {kw_parts})' if kw_parts else f't("{msg_id}")'

        # 用 get_source_segment 精确获取原始参数文本（正确处理中文字符偏移）
        arg_node = node.args[0]
        original_arg = ast.get_source_segment(source, arg_node)
        if original_arg is None:
            continue

        # 在源码中定位原始参数的精确位置
        approx = line_offsets[arg_node.lineno - 1] + arg_node.col_offset
        window_start = max(0, approx - 4)
        pos = source.find(original_arg, window_start)
        if pos == -1:
            continue

        replacements.append((pos, pos + len(original_arg), t_call, msg_id, ftl_value))

    # 从后往前替换，保证偏移量不受影响
    replacements.sort(key=lambda x: x[0], reverse=True)

    new_source = source
    ftl_entries_map = {}
    for start, end, new_text, msg_id, ftl_value in replacements:
        new_source = new_source[:start] + new_text + new_source[end:]
        ftl_entries_map[msg_id] = ftl_value

    # 按出现顺序返回 FTL 条目（去重）
    ordered_ftl = []
    seen = set()
    for _, _, _, msg_id, ftl_value in sorted(replacements, key=lambda x: x[0]):
        if msg_id not in seen:
            ordered_ftl.append((msg_id, ftl_value))
            seen.add(msg_id)

    return ordered_ftl, new_source


# ---------------------------------------------------------------------------
# 命令行入口
# ---------------------------------------------------------------------------

def get_ftl_category(file_path: Path) -> str:
    """根据文件路径确定 FTL 分类"""
    parts = file_path.parts
    if "astrbot" in parts:
        idx = parts.index("astrbot")
        if idx + 1 < len(parts):
            category = parts[idx + 1]
            # 排除 __init__.py 等文件直接在 astrbot 下的情况
            if category.endswith(".py"):
                return "main"
            return category
    return "main"

def main():
    import argparse

    parser = argparse.ArgumentParser(description="提取 i18n 消息并重写日志/异常调用")
    parser.add_argument("--rewrite", action="store_true", help="原地重写源文件")
    args = parser.parse_args()

    root_dir = Path(".")
    ftl_base_dir = Path("astrbot/i18n/locales/zh-cn")
    ftl_base_dir.mkdir(parents=True, exist_ok=True)

    # 记录所有生成的 FTL 条目，按类别分组
    # category -> { file_path -> [ (msg_id, ftl_value) ] }
    all_ftl_entries = {}

    exclude_dirs = {".git", "__pycache__", ".venv", "venv", "tests", ".pytest_cache", ".ruff_cache", ".idea", ".vscode", "data"}

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if not file.endswith(".py"):
                continue
            if file == "automatic_i18n.py" or file == "runtime_bootstrap.py":
                continue

            file_path = Path(root) / file
            print(f"Processing {file_path}...")

            try:
                source = file_path.read_text(encoding="utf-8")
                ftl_entries, new_source = extract_and_rewrite(source)

                if not ftl_entries:
                    continue

                if args.rewrite:
                    import_stmt = "from astrbot.core.lang import t"
                    if import_stmt not in new_source:
                        # 插入到 docstring 之后或文件开头
                        if new_source.startswith('"""') or new_source.startswith("'''"):
                            end_doc = new_source.find(new_source[:3], 3)
                            if end_doc != -1:
                                insert_pos = end_doc + 3
                                new_source = new_source[:insert_pos] + "\n" + import_stmt + new_source[insert_pos:]
                            else:
                                new_source = import_stmt + "\n" + new_source
                        else:
                            new_source = import_stmt + "\n" + new_source
                    file_path.write_text(new_source, encoding="utf-8")
                    print(f"  [Rewritten] {file_path}")

                category = get_ftl_category(file_path)
                if category not in all_ftl_entries:
                    all_ftl_entries[category] = {}
                
                # 使用相对于根目录的路径作为标识
                rel_path = file_path.relative_to(root_dir)
                all_ftl_entries[category][str(rel_path)] = ftl_entries

            except Exception as e:
                print(f"  [Error] Failed to process {file_path}: {e}")

    # 写入 FTL 文件
    for category, files_data in all_ftl_entries.items():
        ftl_file = ftl_base_dir / f"{category}.ftl"
        
        # 读取现有内容以避免重复写入相同文件的 header
        existing_content = ""
        if ftl_file.exists():
            existing_content = ftl_file.read_text(encoding="utf-8")
        
        new_ftl_lines = []
        for rel_path, entries in files_data.items():
            header = f"### {rel_path}"
            # 只有当 header 不存在时才添加 header 和内容
            # 这里简单处理，总是追加。如果需要更复杂的去重可以进一步优化。
            new_ftl_lines.append(f"\n{header}")
            for msg_id, ftl_value in entries:
                # 简单的去重逻辑：检查 msg_id 是否已存在
                if f"{msg_id} =" not in existing_content:
                    new_ftl_lines.append(f"{msg_id} = {ftl_value}")

        if new_ftl_lines:
            with open(ftl_file, "a", encoding="utf-8") as f:
                f.write("\n".join(new_ftl_lines) + "\n")
            print(f"[FTL] Updated {ftl_file} with {len(new_ftl_lines)} lines.")

if __name__ == "__main__":
    main()
