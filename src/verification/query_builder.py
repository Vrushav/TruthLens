from src.models.verification.claim import Claim


class QueryBuilder:
    """
    Builds optimized search queries from a claim.
    """

    KEYWORD_MAP = {
        "created": ["creator", "official"],
        "developed": ["official", "documentation"],
        "maintained": ["official", "documentation"],
        "invented": ["inventor"],
        "founded": ["founder", "history"],
        "ceo": ["leadership"],
    }

    def build(self, claim: Claim) -> str:

        text = claim.text.strip()
        lower = text.lower()

        # -------------------------------
        # Natural-language query patterns
        # -------------------------------

        if "created by" in lower:
            subject = text.split("was created by")[0].strip()
            return f"Who created {subject}"

        if "developed by" in lower:
            subject = text.split("was developed by")[0].strip()
            return f"Who developed {subject}"

        if "maintained by" in lower:
            subject = text.split("is maintained by")[0].strip()
            return f"Who maintains {subject}"

        if "founded by" in lower:
            subject = text.split("was founded by")[0].strip()
            return f"Who founded {subject}"

        if "released in" in lower:
            subject = text.split("was released")[0].strip()
            return f"When was {subject} released"

        # -------------------------------
        # Existing keyword-based logic
        # -------------------------------

        query_parts = []

        for entity in claim.entities:
            query_parts.append(entity.text)

        for word, keywords in self.KEYWORD_MAP.items():
            if word in lower:
                query_parts.extend(keywords)

        if len(query_parts) == len(claim.entities):
            query_parts.append("official")

        return " ".join(dict.fromkeys(query_parts))