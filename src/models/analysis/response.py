from dataclasses import dataclass, field
from typing import List

from .code_block import CodeBlock


@dataclass
class Response:

    text_sections: List[str] = field(default_factory=list)

    code_blocks: List[CodeBlock] = field(default_factory=list)

    commands: List[str] = field(default_factory=list)

    configs: List[str] = field(default_factory=list)