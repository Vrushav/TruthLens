from src.models.code_block import CodeBlock
from src.models.issue import Issue
from src.analysis.analyzer import Analyzer

class AnalysisEngine:
    """
    Runs all registered analyzers on a code block.
    """

    def __init__(self):
        self.analyzers: list[Analyzer] = []

    def register(self, analyzer: Analyzer):
        self.analyzers.append(analyzer)

    def analyze(self, block: CodeBlock) -> list[Issue]:
        issues = []

        for analyzer in self.analyzers:
            issues.extend(analyzer.analyze(block))

        return issues