from abc import ABC, abstractmethod

from src.models.code_block import CodeBlock
from src.models.issue import Issue


class Analyzer(ABC):
    """
    Base class for all analyzers.
    """

    @abstractmethod
    def analyze(self, block: CodeBlock) -> list[Issue]:
        """
        Analyze a code block and return detected issues.
        """
        pass