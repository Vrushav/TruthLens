from dataclasses import dataclass


@dataclass(slots=True)
class Evidence:
    """
    Represents evidence collected from an external source.
    """

    title: str
    url: str
    snippet: str
    source: str
    relevance_score: float = 0.0      # ranking score
    similarity_score: float = 0.0     # semantic similarity