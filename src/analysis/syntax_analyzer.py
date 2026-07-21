import ast

from src.analysis.issue_factory import IssueFactory
from src.models.analysis.code_block import CodeBlock
from src.models.analysis.issue import Issue
from src.models.enums.analyzer_type import AnalyzerType
from src.models.enums.category import Category
from src.models.enums.severity import Severity
from src.analysis.analyzer import Analyzer

class SyntaxAnalyzer(Analyzer):
    """
    Checks Python code for syntax errors.
    """

    def analyze(self, block: CodeBlock) -> list[Issue]:
        issues = []

        # Only analyze Python code
        if block.language != "python":
            return issues

        try:
            ast.parse(block.code)

        except SyntaxError as e:
            issues.append(
              IssueFactory.create(
                    "SYN001",
                    message=e.msg,
                  line=e.lineno
             )
        )

        
        return issues