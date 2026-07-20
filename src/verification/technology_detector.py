import json
import re
from pathlib import Path

from src.models.claim import Claim
from src.models.entity import Entity


class TechnologyDetector:
    """
    Detects technology-related entities that spaCy may miss.
    """

    def __init__(self) -> None:
        self.technology_terms = self._load_terms()

    def _load_terms(self) -> dict[str, str]:
        data_path = Path("data") / "technology_terms.json"

        try:
            with data_path.open("r", encoding="utf-8") as file:
                technology_list = json.load(file)

            return {
                term.lower(): term
                for term in technology_list
            }

        except FileNotFoundError:
            raise FileNotFoundError(
                f"Technology terms file not found: {data_path}"
            )

        except json.JSONDecodeError:
            raise ValueError(
                f"Invalid JSON format in {data_path}"
            )

    def detect(self, claim: Claim) -> Claim:
        """
        Detect technology entities in a claim.
        """

        for normalized_term, original_term in self.technology_terms.items():

            pattern = rf"(?<!\w){re.escape(original_term)}(?!\w)"

            if re.search(pattern, claim.text, re.IGNORECASE):

                exists = any(
                    entity.text.lower() == normalized_term
                    and entity.label == "TECHNOLOGY"
                    for entity in claim.entities
                )

                if not exists:
                    claim.entities.append(
                        Entity(
                            text=original_term,
                            label="TECHNOLOGY",
                            confidence=0.95,
                        )
                    )

        return claim