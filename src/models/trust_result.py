from dataclasses import dataclass


@dataclass(slots=True)
class TrustResult:
    """
    Final verification result for a claim.
    """

    trust_score: float
    verdict: str
    explanation: str