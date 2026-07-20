from dataclasses import dataclass, field
from typing import Optional

from src.models.enums.analyzer_type import AnalyzerType
from src.models.enums.category import Category
from src.models.enums.severity import Severity


@dataclass
class Issue:
    id: str

    analyzer: AnalyzerType
    severity: Severity
    category: Category

    title: str
    message: str
    recommendation: str

    line: Optional[int] = None
    confidence: float = 1.0

    references: list[str] = field(default_factory=list)