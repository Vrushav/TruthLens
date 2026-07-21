import ast

from src.analysis.analyzer import Analyzer
from src.analysis.issue_factory import IssueFactory
from src.models.analysis.code_block import CodeBlock

ATTRIBUTE_CALL_RULES = {
    ("pickle", "loads"): "SEC006",
    ("yaml", "load"): "SEC007",
    ("hashlib", "md5"): "SEC008",
    ("hashlib", "sha1"): "SEC009",
}

NAME_CALL_RULES = {
    ("pickle", "loads"): "SEC006",
    ("yaml", "load"): "SEC007",
    ("hashlib", "md5"): "SEC008",
    ("hashlib", "sha1"): "SEC009",
}

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

                issues.extend(self._check_attribute_calls(node, imports))

            elif isinstance(node, ast.Assign):

                issues.extend(self._check_assignments(node))

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

    def _check_name_calls(self, node, imports):

        issues = []

        if not isinstance(node.func, ast.Name):
            return issues

        if node.func.id == "eval":

            issues.append(
                IssueFactory.create(
                    "SEC001",
                   line=node.lineno,
                )
            )

            return issues

        if node.func.id == "exec":

            issues.append(
                IssueFactory.create(
                    "SEC002",
                   line=node.lineno,
                )
            )

            return issues

        module = imports.get(node.func.id)

        if module is None:
            return issues

        rule = NAME_CALL_RULES.get((module, node.func.id))

        if rule:

            issues.append(
                IssueFactory.create(
                    rule,
                  line=node.lineno,
                )
            )

        return issues

    # ---------------------------------------------------------

    def _check_attribute_calls(self, node, imports):

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

                    issues.append(
                        IssueFactory.create(
                            "SEC003",
                            line=node.lineno,
                        )
                    )

        if not isinstance(node.func.value, ast.Name):
            return issues

        module = imports.get(
            node.func.value.id,
            node.func.value.id,
        )

        rule = ATTRIBUTE_CALL_RULES.get((module, node.func.attr))

        if rule:

            issues.append(
                IssueFactory.create(
                    rule,
                    line=node.lineno,
                )
            )

        elif module == "os" and node.func.attr == "system":

            issues.append(
                IssueFactory.create(
                    "SEC005",
                    line=node.lineno,
                )
            )

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
