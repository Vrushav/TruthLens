import ast

from src.models.code_block import CodeBlock
from src.models.issue import Issue
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
              Issue(
                  id="SYN001",
                  analyzer=AnalyzerType.SYNTAX,
                  severity=Severity.HIGH,
                  category=Category.SYNTAX,
                  title="Syntax Error",
                  message=e.msg,
                  recommendation="Fix the syntax error before executing the code.",
                  line=e.lineno,
                  confidence=1.0,
                  references=[
                      "Python Language Reference",
                      "ast.parse"
                  ]
            )
)

        return issues