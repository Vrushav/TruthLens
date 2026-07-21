import ast

from src.analysis.analyzer import Analyzer
from src.analysis.issue_factory import IssueFactory
from src.models.analysis.code_block import CodeBlock


class SecurityAnalyzer(Analyzer):

    def analyze(self, block: CodeBlock):

        if block.language != "python":
            return []

        try:
            tree = ast.parse(block.code)
        except SyntaxError:
            return []

        imports = self._collect_imports(tree)

        issues = []

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                issues.extend(self._check_name_calls(node, imports))

                issues.extend(self._check_attribute_calls(node))

            elif isinstance(node, ast.Assign):

                issues.extend(self._check_assignments(node))

        return issues

    # ---------------------------------------------------------

    def _collect_imports(self, tree):

        imports = {}

        for node in ast.walk(tree):

            if isinstance(node, ast.ImportFrom):

                if node.module:

                    for alias in node.names:

                        imports[alias.asname or alias.name] = node.module

        return imports

    # ---------------------------------------------------------

    def _check_name_calls(self, node, imports):

        issues = []

        if not isinstance(node.func, ast.Name):
            return issues

        if node.func.id == "eval":

            issues.append(IssueFactory.create("SEC001", line=node.lineno))

        elif node.func.id == "exec":

            issues.append(IssueFactory.create("SEC002", line=node.lineno))

        elif node.func.id == "loads" and imports.get("loads") == "pickle":

            issues.append(IssueFactory.create("SEC006", line=node.lineno))

        # -------- SEC007 --------

        elif node.func.id == "load" and imports.get("load") == "yaml":

            issues.append(IssueFactory.create("SEC007", line=node.lineno))

        return issues

    # ---------------------------------------------------------

    def _check_attribute_calls(self, node):

        issues = []

        if not isinstance(node.func, ast.Attribute):
            return issues

        # subprocess.run(..., shell=True)

        if node.func.attr == "run":

            for keyword in node.keywords:

                if (
                    keyword.arg == "shell"
                    and isinstance(keyword.value, ast.Constant)
                    and keyword.value.value is True
                ):

                    issues.append(IssueFactory.create("SEC003", line=node.lineno))

        # os.system()

        elif (
            isinstance(node.func.value, ast.Name)
            and node.func.value.id == "os"
            and node.func.attr == "system"
        ):

            issues.append(IssueFactory.create("SEC005", line=node.lineno))

        # pickle.loads()

        elif (
            isinstance(node.func.value, ast.Name)
            and node.func.value.id == "pickle"
            and node.func.attr == "loads"
        ):

            issues.append(IssueFactory.create("SEC006", line=node.lineno))

        # yaml.load()

        elif (
            isinstance(node.func.value, ast.Name)
            and node.func.value.id == "yaml"
            and node.func.attr == "load"
        ):

            issues.append(IssueFactory.create("SEC007", line=node.lineno))

        return issues

    # ---------------------------------------------------------

    def _check_assignments(self, node):

        issues = []

        suspicious_names = {
            "password",
            "passwd",
            "pwd",
            "secret",
            "token",
            "api_key",
            "apikey",
            "access_key",
            "auth_token",
            "jwt_secret",
        }

        for target in node.targets:

            if not isinstance(target, ast.Name):
                continue

            if (
                target.id.lower() in suspicious_names
                and isinstance(node.value, ast.Constant)
                and isinstance(node.value.value, str)
            ):

                issues.append(
                    IssueFactory.create(
                        "SEC004",
                        line=node.lineno,
                    )
                )

        return issues
