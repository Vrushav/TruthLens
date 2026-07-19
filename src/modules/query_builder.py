from src.models.claim import Claim


class QueryBuilder:
    """
    Builds optimized search queries from a claim.
    """

    # Mapping from common claim words to search-friendly keywords
    KEYWORD_MAP = {
        "created": ["creator", "official"],
        "developed": ["official", "documentation"],
        "maintained": ["official", "documentation"],
        "invented": ["inventor"],
        "founded": ["founder", "history"],
        "ceo": ["leadership"],
    }

    def build(self, claim: Claim) -> str:
        query_parts = []

        # Add extracted entities
        for entity in claim.entities:
            query_parts.append(entity.text)

        # Add context-specific keywords
        claim_text = claim.text.lower()

        for word, keywords in self.KEYWORD_MAP.items():
            if word in claim_text:
                query_parts.extend(keywords)

        # Fallback if nothing matched
        if len(query_parts) == len(claim.entities):
            query_parts.append("official")

        # Remove duplicates while preserving order
        return " ".join(dict.fromkeys(query_parts))