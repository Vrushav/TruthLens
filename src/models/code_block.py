from dataclasses import dataclass


@dataclass
class CodeBlock:
    language: str
    code: str

    start_line: int
    end_line: int