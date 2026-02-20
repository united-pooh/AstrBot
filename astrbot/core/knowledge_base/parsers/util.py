from .base import BaseParser
from astrbot.core.lang import t


async def select_parser(ext: str) -> BaseParser:
    if ext in {".md", ".txt", ".markdown", ".xlsx", ".docx", ".xls"}:
        from .markitdown_parser import MarkitdownParser

        return MarkitdownParser()
    if ext == ".pdf":
        from .pdf_parser import PDFParser

        return PDFParser()
    raise ValueError(t('knowledge_base-parsers-util-unsupported_format', ext=ext))
