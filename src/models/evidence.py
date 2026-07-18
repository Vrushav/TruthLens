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