import ast

from src.analysis.analyzer import Analyzer
from src.analysis.issue_factory import IssueFactory
from src.models.analysis.code_block import CodeBlock


class SecurityAnalyzer(Analyzer):

    def analyze(self, block: CodeBlock):

        issues = []

        if block.language != "python":
            return issues

        try:
            tree = ast.parse(block.code)
        except SyntaxError:
            return issues

        # -----------------------------------------
        # Track imported names
        # Example:
        # from pickle import loads
        # => imports["loads"] = "pickle"
        # -----------------------------------------

        imports = {}

        for node in ast.walk(tree):

            if isinstance(node, ast.ImportFrom):

                if node.module:

                    for alias in node.names:
                        imports[alias.asname or alias.name] = node.module

        # -----------------------------------------
        # Analyze AST
        # -----------------------------------------

        for node in ast.walk(tree):

            if isinstance(node, ast.Call):

                # -------------------------
                # Name-based calls
                # -------------------------

                if isinstance(node.func, ast.Name):

                    if node.func.id == "eval":

                        issues.append(IssueFactory.create("SEC001", line=node.lineno))

                    elif node.func.id == "exec":

                        issues.append(IssueFactory.create("SEC002", line=node.lineno))

                    elif node.func.id == "loads" and imports.get("loads") == "pickle":

                        issues.append(IssueFactory.create("SEC006", line=node.lineno))

                # -------------------------
                # Attribute-based calls
                # -------------------------

                elif isinstance(node.func, ast.Attribute):

                    # subprocess.run(..., shell=True)

                    if node.func.attr == "run":

                        for keyword in node.keywords:

                            if (
                                keyword.arg == "shell"
                                and isinstance(keyword.value, ast.Constant)
                                and keyword.value.value is True
                            ):

                                issues.append(
                                    IssueFactory.create("SEC003", line=node.lineno)
                                )

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

            # -------------------------
            # Hardcoded credentials
            # -------------------------

            elif isinstance(node, ast.Assign):

                for target in node.targets:

                    if isinstance(target, ast.Name):

                        variable_name = target.id.lower()

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

                        if (
                            variable_name in suspicious_names
                            and isinstance(node.value, ast.Constant)
                            and isinstance(node.value.value, str)
                        ):

                            issues.append(
                                IssueFactory.create("SEC004", line=node.lineno)
                            )

        return issues