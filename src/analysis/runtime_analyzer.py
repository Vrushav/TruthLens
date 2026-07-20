import ast

from src.analysis.analyzer import Analyzer
from src.models.code_block import CodeBlock
from src.models.issue import Issue
from src.models.enums.analyzer_type import AnalyzerType
from src.models.enums.category import Category
from src.models.enums.severity import Severity
from src.analysis.issue_factory import IssueFactory


class RuntimeAnalyzer(Analyzer):
    """
    Detects common runtime risks in Python code.
    """

    def analyze(self, block: CodeBlock) -> list[Issue]:
        issues = []

        if block.language != "python":
            return issues

        try:
            tree = ast.parse(block.code)
        except SyntaxError:
            # Syntax errors are handled by SyntaxAnalyzer
            return issues

        for node in ast.walk(tree):

            # Detect division by zero
            if isinstance(node, ast.BinOp):

                if isinstance(node.op, ast.Div):

                    if isinstance(node.right, ast.Constant):

                        if node.right.value == 0:

                            issues.append(
                                IssueFactory.create(
                                      "RUN001",
                                      line=node.lineno
                                  )
                              )

        return issues