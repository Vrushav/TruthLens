import ast

from src.analysis.analyzer import Analyzer
from src.analysis.issue_factory import IssueFactory
from src.models.analysis.code_block import CodeBlock
from src.rules.python_api_rules import PYTHON_API_RULES


class HallucinationAnalyzer(Analyzer):

    def analyze(self, block: CodeBlock):

        issues = []

        if block.language != "python":
            return issues

        try:
            tree = ast.parse(block.code)
        except SyntaxError:
            return issues

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                func = node.func

                if isinstance(func, ast.Attribute):

                    if isinstance(func.value, ast.Name):

                        module = func.value.id

                        method = func.attr

                        if module in PYTHON_API_RULES:

                            valid = PYTHON_API_RULES[module]["valid"]

                            if method not in valid:

                                issues.append(

                                    IssueFactory.create(

                                        "API001",

                                        message=f"{module}.{method}() does not exist.",

                                        recommendation=f"Check the official {module} documentation.",

                                        line=node.lineno

                                    )

                                )

        return issues