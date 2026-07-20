"""
Response Parser Module

This module is responsible for converting AI-generated responses
into clean, individual textual claims that can later be verified.
"""

import re
import spacy


class ResponseParser:
    """
    Parses AI-generated responses into individual claims.
    """

    def __init__(self):
        """
        Load the spaCy English language model.
        """
        self.nlp = spacy.load("en_core_web_sm")

    def clean_text(self, text: str) -> str:
        """
        Clean and normalize the input text.

        Args:
            text: Raw AI-generated response.

        Returns:
            Cleaned string.
        """

        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    def split_into_claims(self, text: str) -> list[str]:
        """
        Split cleaned text into individual sentences.

        Args:
            text: Cleaned text.

        Returns:
            List of claims.
        """

        if not text:
            return []

        doc = self.nlp(text)

        return [
            sentence.text.strip()
            for sentence in doc.sents
            if sentence.text.strip()
        ]

    def get_claims(self, response: str) -> list[str]:
        """
        Public method used by the application.

        Args:
            response: AI-generated response.

        Returns:
            List of extracted claims.
        """

        cleaned = self.clean_text(response)

        return self.split_into_claims(cleaned)