import ast
from pathlib import Path
import re


def generate_ftl_key(static_text: str, file_path: Path) -> str:
    """
    生成包含路径和文件名信息的、更具描述性的 FTL Key。
    格式: [路径部分]-[文件名部分]-[日志静态文本部分]
    """
    # 1. 路径部分: e.g., "astrbot/dashboard/routes/file.py" -> "dashboard-routes"
    # parts[1:-1] 提取 "dashboard", "routes"
    path_parts = file_path.parts[1:-1]
    path_prefix = "-".join(path_parts)

    # 2. 文件名部分: e.g., "file.py" -> "file"
    file_stem = file_path.stem

    # 3. 日志文本部分
    text_part = re.sub(r"[\s\W]+", "-", static_text.lower().strip())
    text_part = text_part.strip("-")

    # 组合所有部分
    full_key = (
        f"{path_prefix}-{file_stem}-{text_part}"
        if path_prefix
        else f"{file_stem}-{text_part}"
    )

    # 保证 key 的唯一性和可读性，但限制总长度
    return full_key[:100] if full_key else "unnamed-log-key"


class FStringParser:
    """
    专门解析 f-string (ast.JoinedStr) 节点,
    将其转换为 FTL 模板和变量名列表。
    """

    def parse(self, node: ast.JoinedStr):
        ftl_template = ""
        variables = []
        static_text_parts = []

        for value in node.values:
            if isinstance(value, ast.Constant):
                ftl_template += value.s
                static_text_parts.append(value.s)
            elif isinstance(value, ast.FormattedValue):
                var_name = "unknown"
                if hasattr(value.value, "id"):
                    var_name = value.value.id
                elif hasattr(value.value, "attr"):
                    var_name = value.value.attr

                ftl_template += f"{{ ${var_name} }}"
                variables.append(var_name)

        full_static_text = "".join(static_text_parts)
        return ftl_template, variables, full_static_text


class LogVisitor(ast.NodeVisitor):
    def __init__(self, source_lines, file_path: Path):
        self.logs_to_translate = []
        self.source_lines = source_lines
        self.file_path = file_path  # 需要文件路径来生成 key
        self.fstring_parser = FStringParser()

    def visit_Call(self, node):
        if self._is_logger_call(node):
            log_source = self._get_source_segment(node)

            if "t(" in log_source or "t (" in log_source:
                return

            if node.args and isinstance(node.args[0], ast.JoinedStr):
                fstring_node = node.args[0]
                template, _, static_text = self.fstring_parser.parse(fstring_node)
                # 传入文件路径以生成新的 key
                key = generate_ftl_key(static_text, self.file_path)

                self.logs_to_translate.append(
                    {"original_log": log_source, "key": key, "value": template}
                )

        self.generic_visit(node)

    def _is_logger_call(self, node):
        if not isinstance(node.func, ast.Attribute):
            return False
        if node.func.attr not in {"debug", "info", "warning", "error", "critical"}:
            return False
        target = node.func.value
        if isinstance(target, ast.Name) and target.id == "logger":
            return True
        if isinstance(target, ast.Attribute) and target.attr == "logger":
            return True
        return False

    def _get_source_segment(self, node):
        start = node.lineno - 1
        end = getattr(node, "end_lineno", node.lineno)
        return " ".join(line.strip() for line in self.source_lines[start:end])


def process_file(file_path: Path):
    try:
        source = file_path.read_text("utf-8")
        # 将文件路径传入 Visitor
        visitor = LogVisitor(source.splitlines(), file_path)
        visitor.visit(ast.parse(source))
        return visitor.logs_to_translate
    except Exception:
        return []


def main():
    py_files = [
        p
        for p in Path("astrbot").rglob("*.py")
        if p.is_file() and p.name != "__init__.py"
    ]
    preview_data = {}

    for f in py_files:
        logs = process_file(f)
        if not logs:
            continue

        # 假设路径是 "astrbot/core/main.py", head 是 "core"
        head = f.parts[1] if len(f.parts) > 2 else "main"
        ftl_name = f"{head}.ftl"

        if ftl_name not in preview_data:
            preview_data[ftl_name] = []

        for log in logs:
            log["source_file"] = str(f)
            preview_data[ftl_name].append(log)

    print("--- 预览模式：即将写入 FTL 的内容 (新 Key 格式) ---")
    if not preview_data:
        print("\n✅ 所有 f-string 格式的 log 似乎都已翻译，未发现可处理项。")
        return

    for ftl_file, entries in sorted(preview_data.items()):
        print(f"\n[即将写入 {ftl_file}]")
        print("---")
        for entry in entries:
            print(f"# 来源于: {entry['source_file']}")
            print(f"# 原始 log: {entry['original_log']}")
            print(f"{entry['key']} = {entry['value']}")
            print("---")


if __name__ == "__main__":
    main()
