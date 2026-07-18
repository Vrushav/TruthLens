"""
Entity Extraction Module

Extracts named entities from claims using spaCy.
"""

import spacy

from src.models import Claim, Entity


class EntityExtractor:
    """
    Extract named entities from claims.
    """

    def __init__(self):
        """
        Load spaCy English model.
        """
        self.nlp = spacy.load("en_core_web_sm")

    def extract(self, claim: Claim) -> Claim:
        """
        Extract entities from a claim.

        Args:
            claim: Claim object.

        Returns:
            Updated Claim with extracted entities.
        """

        doc = self.nlp(claim.text)

        claim.entities = [
            Entity(
                text=entity.text,
                label=entity.label_
            )
            for entity in doc.ents
        ]

        return claim