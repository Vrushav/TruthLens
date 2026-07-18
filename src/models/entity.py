from dataclasses import dataclass


@dataclass(slots=True)
class Entity:
    """
    Represents an extracted entity.
    """

    text: str

    label: str

    confidence: float = 1.0