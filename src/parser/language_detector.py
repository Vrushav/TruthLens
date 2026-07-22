import re


class LanguageDetector:
    """
    Detects and normalizes programming language names.
    """

    LANGUAGE_ALIASES = {
        "py": "python",
        "python": "python",

        "js": "javascript",
        "javascript": "javascript",

        "ts": "typescript",
        "typescript": "typescript",

        "java": "java",

        "cpp": "cpp",
        "c++": "cpp",

        "c": "c",

        "cs": "csharp",
        "c#": "csharp",

        "go": "go",
        "golang": "go",

        "rs": "rust",
        "rust": "rust",

        "php": "php",

        "rb": "ruby",
        "ruby": "ruby",

        "swift": "swift",

        "kt": "kotlin",
        "kotlin": "kotlin",

        "sql": "sql",

        "json": "json",
        "yaml": "yaml",
        "yml": "yaml",
        "xml": "xml",

        "bash": "bash",
        "shell": "bash",
        "sh": "bash",

        "dockerfile": "dockerfile"
    }

    def detect(self, language: str, code: str = "") -> str:
        """
        Returns a normalized language name.
        """

        if language:
            language = language.strip().lower()

            if language in self.LANGUAGE_ALIASES:
                return self.LANGUAGE_ALIASES[language]

        # ---------- Heuristics ----------

        code = code.lower()

        if re.search(r"\bprint\s*\(", code):
            return "python"

        if "console.log" in code:
            return "javascript"

        if "system.out.println" in code:
            return "java"

        if re.search(r"\bselect\b.*\bfrom\b", code):
            return "sql"

        return "text"