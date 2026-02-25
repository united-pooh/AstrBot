import ast
from pathlib import Path


class LogVisitor(ast.NodeVisitor):
    def __init__(self, source_lines):
        self.logs = []
        self.source_lines = source_lines

    def is_logger_call(self, node):
        """判断是否为 logger 相关调用"""
        if not isinstance(node.func, ast.Attribute):
            return False

        # 匹配方法名
        if node.func.attr not in {"debug", "info", "warning", "error", "critical"}:
            return False

        # 匹配调用者：logger 或 self.logger 等
        target = node.func.value
        # 情况 A: logger.info()
        if isinstance(target, ast.Name) and target.id == "logger":
            return True
        # 情况 B: self.logger.info()
        if isinstance(target, ast.Attribute) and target.attr == "logger":
            return True
        # 情况 C: logging.getLogger().info()
        if (
            isinstance(target, ast.Call)
            and isinstance(target.func, ast.Name)
            and target.func.id == "getLogger"
        ):
            return True

        return False

    def visit_Call(self, node):
        # 1. 识别 logger 调用
        if self.is_logger_call(node):
            # 2. 提取源代码片段
            start_line = node.lineno - 1
            end_line = getattr(node, "end_lineno", node.lineno)

            # 合并多行并清理多余空格，形成一个用于判断的完整字符串
            call_code = "".join(self.source_lines[start_line:end_line]).strip()

            # 3. 强力字符串过滤：排除任何包含调用 t(...) 迹象的 log
            # 检查特征：t(, t (, .t(
            if "t(" in call_code or "t (" in call_code:
                return  # 命中翻译标识，跳过

            # 4. 存储未翻译的 log (保持原始多行格式以便阅读)
            log_display = " ".join(
                line.strip() for line in self.source_lines[start_line:end_line]
            )
            self.logs.append(log_display)

        self.generic_visit(node)


def extract_logs_from_file(file_path: Path) -> list[str]:
    """解析单个文件并提取所有未翻译的 logger 调用"""
    try:
        source = file_path.read_text(encoding="utf-8")
        source_lines = source.splitlines()
        tree = ast.parse(source)

        visitor = LogVisitor(source_lines)
        visitor.visit(tree)
        return visitor.logs
    except Exception:
        return []


def get_py_files(target_dir: str = "astrbot") -> list[Path]:
    """递归获取目录下所有 python 文件"""
    root = Path(target_dir)
    if not root.exists():
        return []
    return [p for p in root.rglob("*.py") if p.is_file() and p.name != "__init__.py"]


def main():
    py_files = get_py_files()
    all_logs = {}

    for f in py_files:
        logs = extract_logs_from_file(f)
        if logs:
            rel_path = str(f.relative_to("."))
            all_logs[rel_path] = logs

    total_files = len(all_logs)
    total_logs = sum(len(l) for l in all_logs.values())

    print("✅ 扫描完成！")
    print(
        f"共发现 {total_logs} 条未翻译的 logger 记录，分布在 {total_files} 个文件中。\n"
    )

    for file_path in sorted(all_logs.keys()):
        print(f"[{file_path}]:")
        for log in all_logs[file_path]:
            print(f"  - {log}")


if __name__ == "__main__":
    main()
