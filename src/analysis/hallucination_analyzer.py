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

        print("===== ANALYZE STARTED =====")

        issues = []

        print("Language:", block.language)

        if block.language != "python":
            print("Not Python")
            return issues

        try:
            tree = ast.parse(block.code)
            print("AST parsed successfully")
        except SyntaxError:
            print("Syntax Error")
            return issues

        imports = self._collect_imports(tree)
        print("Imports:", imports)

        for node in ast.walk(tree):

            print("AST Node:", type(node).__name__)

            if not isinstance(node, ast.Call):
                continue

            print("FOUND CALL")

            issues.extend(self._check_attribute_calls(node, imports))

        print("Final Issues:", issues)

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

        print(">>> Entered _check_attribute_calls")

        issues = []

        if not isinstance(node.func, ast.Attribute):
            print("Not an attribute call")
            return issues

        if not isinstance(node.func.value, ast.Name):
            print("Attribute is not called on a Name")
            return issues

        module = imports.get(
            node.func.value.id,
            node.func.value.id,
        )

        print("Module:", module)

        valid = self.loader.load(module)
        print("Valid APIs:", valid)

        if not valid:
            print("No APIs loaded!")
            return issues

        method = node.func.attr

        print("Method Called:", method)
        print("Method Exists:", method in valid)

        if method not in valid:

            suggestion = self._get_suggestion(module, method)

            recommendation = (
                f"Did you mean '{module}.{suggestion}()'?"
                if suggestion
                else f"Check the official {module} documentation."
            )

            issue = IssueFactory.create(
                "API001",
                message=f"{module}.{method}() does not exist.",
                recommendation=recommendation,
                line=node.lineno,
            )

            print("Created Issue:", issue)

            issues.append(issue)

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