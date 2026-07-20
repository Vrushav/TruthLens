import re
from src.models.verification.claim import Claim


class EvidenceRanker:
    """
    Ranks collected evidence based on simple heuristics.
    """

    TRUSTED_DOMAINS = {
        "python.org": 1.0,
        "docs.python.org": 1.0,
        "github.com": 0.95,
        "developer.mozilla.org": 0.95,
        "react.dev": 1.0,
        "wikipedia.org": 0.80,
    }

    def rank(self, claim: Claim) -> Claim:
        """
        Assign a relevance score to each evidence object
        and sort them from best to worst.
        """

        claim_words = {
        word.lower()
        for word in re.findall(r"\b\w+\b", claim.text)
        if len(word) > 2
}

        for evidence in claim.evidence:

        # ----------------------------
        # Domain score
        # ----------------------------

          domain_score = 0.5

        domain = evidence.source.lower()

        for trusted_domain, trusted_score in self.TRUSTED_DOMAINS.items():
          if trusted_domain in domain:
            domain_score = trusted_score
            break

        # ----------------------------
        # Keyword overlap
        # ----------------------------

        evidence_text = (
          f"{evidence.title} {evidence.snippet}"
        ).lower()

        overlap = sum(
          word in evidence_text
            for word in claim_words
        )

        keyword_score = overlap / max(len(claim_words), 1)

        # ----------------------------
        # Final score
        # ----------------------------

        evidence.relevance_score = (
          0.8 * domain_score
          + 0.2 * keyword_score
        )

        claim.evidence = sorted(
          claim.evidence,
          key=lambda e: e.relevance_score,
        reverse=True
        )[:3]

        return claim