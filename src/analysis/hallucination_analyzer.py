import ast
import difflib

from src.analysis.analyzer import Analyzer
from src.analysis.issue_factory import IssueFactory
from src.models.analysis.code_block import CodeBlock
from src.services.knowledge_loader import KnowledgeLoader


class HallucinationAnalyzer(Analyzer):

    def __init__(self):
        super().__init__()
        self.loader = KnowledgeLoader()

    def analyze(self, block: CodeBlock):

        issues = []

        if block.language != "python":
            return issues

        try:
            tree = ast.parse(block.code)
        except SyntaxError:
            return issues

        imports = self._collect_imports(tree)

        for node in ast.walk(tree):

            if not isinstance(node, ast.Call):
                continue

            issues.extend(self._check_attribute_calls(node, imports))

        return issues

    # ---------------------------------------------------------

    def _collect_imports(self, tree):

        imports = {}

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:
                    imports[alias.asname or alias.name] = alias.name

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    for alias in node.names:
                        imports[alias.asname or alias.name] = node.module

        return imports

    # ---------------------------------------------------------

    def _check_attribute_calls(self, node, imports):

        issues = []

        if not isinstance(node.func, ast.Attribute):
            return issues

        if not isinstance(node.func.value, ast.Name):
            return issues

        module = imports.get(
            node.func.value.id,
            node.func.value.id,
        )

        valid = self.loader.load(module)

        if not valid:
            return issues

        method = node.func.attr

        if method not in valid:

            suggestion = self._get_suggestion(module, method)

            recommendation = (
                f"Did you mean '{module}.{suggestion}()'?"
                if suggestion
                else f"Check the official {module} documentation."
            )

            issues.append(
                IssueFactory.create(
                    "API001",
                    message=f"{module}.{method}() does not exist.",
                    recommendation=recommendation,
                    line=node.lineno,
                )
            )

        return issues

    # ---------------------------------------------------------

    def _get_suggestion(self, module, method):

        valid = list(self.loader.load(module))

        matches = difflib.get_close_matches(
            method,
            valid,
            n=1,
            cutoff=0.6,
        )

        if matches:
            return matches[0]

        return None
