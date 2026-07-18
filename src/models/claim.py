from dataclasses import dataclass, field

from .entity import Entity
from .evidence import Evidence
from .trust_result import TrustResult


@dataclass(slots=True)
class Claim:
    """
    Represents a single factual claim extracted from an AI response.
    """

    text: str

    entities: list[Entity] = field(default_factory=list)

    evidence: list[Evidence] = field(default_factory=list)

    trust_result: TrustResult | None = None