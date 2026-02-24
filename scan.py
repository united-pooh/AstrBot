from pathlib import Path
import re


def get_py_files() -> list[str]:
    """获取 astrbot/ 目录下所有非 __init__.py 的 python 文件相对路径"""
    folder_path = Path("./astrbot")
    python_files = [
        p.relative_to(folder_path).as_posix()
        for p in folder_path.rglob("*.py")
        if p.is_file() and "__init__.py" not in p.name
    ]
    return sorted(python_files)


def get_file_head(file_path_str: str) -> str:
    """提取路径的第一级目录作为 Head"""
    path = Path(file_path_str)
    if len(path.parts) > 1:
        return path.parts[0]
    return "main"


def get_ftl_data() -> dict[str, set[str]]:
    """扫描 zh-cn 目录下的所有 ftl 文件，提取路径注释"""
    ftl_dir = Path("astrbot/i18n/locales/zh-cn")
    ftl_data = {}

    if not ftl_dir.exists():
        return ftl_data

    for ftl_file in ftl_dir.glob("*.ftl"):
        head = ftl_file.stem
        existing_paths = set()

        # 使用 utf-8-sig 以兼容各种编码可能
        content = ftl_file.read_text(encoding="utf-8-sig")

        # 通用匹配：寻找所有以 ### 开头的行
        matches = re.findall(r"^\s*###\s*(.+)$", content, re.MULTILINE)

        for m in matches:
            # 清洗逻辑：去除首尾空格，并统一移除 'astrbot/' 前缀以匹配 get_py_files 格式
            p_clean = m.strip().replace("astrbot/", "")
            existing_paths.add(p_clean)

        ftl_data[head] = existing_paths

    return ftl_data


def fill_ftl():
    """比对 Python 文件与 FTL 注释，找出缺失的标注"""
    py_files = get_py_files()
    ftl_data = get_ftl_data()

    missing_records = {}  # { head: [missing_paths] }

    for py_path in py_files:
        head = get_file_head(py_path)

        # 确定对应的 FTL 记录集
        existing_paths = ftl_data.get(head, set())

        # 如果当前路径不在 FTL 的已存在路径集合中
        # 匹配逻辑：直接匹配完整相对路径 (如 'core/log.py') 或 匹配去掉 head 的剩余路径
        # 这里采用更稳健的逻辑：只要 py_path 或 去掉 head 后的路径 不在 existing_paths 中

        # 获取去掉 head 后的剩余路径 (例如 'api/all.py' -> 'all.py')
        parts = Path(py_path).parts
        rem_path = "/".join(parts[1:]) if len(parts) > 1 else py_path

        if py_path not in existing_paths and rem_path not in existing_paths:
            if head not in missing_records:
                missing_records[head] = []
            missing_records[head].append(rem_path)

    return missing_records


def write_missing_to_ftl(missing_records: dict[str, list[str]]):
    """将缺失的路径注释追加到对应的 FTL 文件末尾"""
    ftl_dir = Path("astrbot/i18n/locales/zh-cn")

    for head, paths in missing_records.items():
        ftl_path = ftl_dir / f"{head}.ftl"

        if not ftl_path.exists():
            print(f"警告: 跳过 {head}.ftl，文件不存在。")
            continue

        # 准备追加的内容
        # 根据需求：追加“去掉了 get_file_head 的剩余文件路径”
        append_content = ""
        for p in paths:
            append_content += f"\n\n### {p}\n"

        try:
            # 以追加模式打开，确保编码一致
            with open(ftl_path, "a", encoding="utf-8") as f:
                f.write(append_content)
            print(f"成功: 已向 {head}.ftl 追加了 {len(paths)} 条新记录。")
        except Exception as e:
            print(f"失败: 写入 {head}.ftl 时出错: {e}")


if __name__ == "__main__":
    # 1. 扫描并比对
    missing = fill_ftl()

    total_missing = sum(len(paths) for paths in missing.values())

    if total_missing == 0:
        print("\n✨ 所有 Python 文件都已在 FTL 中标注，无需更新。")
    else:
        print(f"\n检测到 {total_missing} 个缺失记录，正在准备追加...")
        # 2. 执行写入
        write_missing_to_ftl(missing)
        print("\n✅ 更新完成！")
