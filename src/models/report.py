from dataclasses import dataclass, field
from typing import List

from .issue import Issue


@dataclass
class Report:

    trust_score: float

    production_ready: bool

    issues: List[Issue] = field(default_factory=list)