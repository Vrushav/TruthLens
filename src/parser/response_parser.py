import re

from src.models.response import Response
from src.models.code_block import CodeBlock
from src.parser.language_detector import LanguageDetector


class ResponseParser:
    """
    Parses an AI response into:
    - Text sections
    - Code blocks
    - Shell commands
    - Config snippets (future)
    """

    CODE_BLOCK_PATTERN = re.compile(
        r"```(\w+)?\n(.*?)```",
        re.DOTALL
    )

    COMMAND_PATTERN = re.compile(
        r"^(pip|npm|yarn|git|python|node|docker)\b.*",
        re.MULTILINE
    )

    def parse(self, response: str) -> Response:

        parsed = Response()
        detector = LanguageDetector()

        # -------------------------
        # Extract code blocks
        # -------------------------

        for match in self.CODE_BLOCK_PATTERN.finditer(response):

            language = match.group(1) or "text"

            code = match.group(2).strip()

            start_line = response[:match.start()].count("\n") + 1

            end_line = start_line + code.count("\n") + 1

            parsed.code_blocks.append(

                CodeBlock(

                    language=detector.detect(language, code),

                    code=code,

                    start_line=start_line,

                    end_line=end_line

                )

            )

        # -------------------------
        # Remove code blocks
        # -------------------------

        text_only = self.CODE_BLOCK_PATTERN.sub("", response)

        # -------------------------
        # Commands
        # -------------------------

        for command in self.COMMAND_PATTERN.findall(text_only):
            pass

        for line in text_only.splitlines():

            line = line.strip()

            if not line:
                continue

            if self.COMMAND_PATTERN.match(line):

                parsed.commands.append(line)

            else:

                parsed.text_sections.append(line)

        return parsed