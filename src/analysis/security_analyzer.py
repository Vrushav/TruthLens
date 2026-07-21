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

        for node in ast.walk(tree):

            # Detect eval()
            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Name):

                    if node.func.id == "eval":

                        issues.append(
                            IssueFactory.create(
                                "SEC001",
                                line=node.lineno
                            )
                        )

                    elif node.func.id == "exec":

                        issues.append(
                            IssueFactory.create(
                                "SEC002",
                                line=node.lineno
                            )
                        )

            # Detect subprocess(..., shell=True)
            if isinstance(node, ast.Call):

                if isinstance(node.func, ast.Attribute):

                    if node.func.attr == "run":

                        for keyword in node.keywords:

                            if keyword.arg == "shell":

                                if (
                                    isinstance(keyword.value, ast.Constant)
                                    and keyword.value.value is True
                                ):

                                    issues.append(
                                        IssueFactory.create(
                                            "SEC003",
                                            line=node.lineno
                                        )
                                    )

            # Detect hardcoded credentials
            if isinstance(node, ast.Assign):

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

                        if variable_name in suspicious_names:

                            if isinstance(node.value, ast.Constant):

                                if isinstance(node.value.value, str):

                                    issues.append(
                                        IssueFactory.create(
                                            "SEC004",
                                          line=node.lineno
                            )
                        )
        return issues