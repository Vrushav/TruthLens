from src.models.claim import Claim
from src.models.trust_result import TrustResult


class TrustEngine:
    """
    Calculates the final trust score for a claim.
    """

    DOMAIN_WEIGHT = 0.4
    SEMANTIC_WEIGHT = 0.6

    def evaluate(self, claim: Claim) -> Claim:

        if not claim.evidence:

            claim.trust_result = TrustResult(
                trust_score=0,
                verdict="NO EVIDENCE",
                explanation="No supporting evidence was found."
            )

            return claim

        avg_domain = sum(
            e.relevance_score for e in claim.evidence
        ) / len(claim.evidence)

        avg_similarity = sum(
            e.similarity_score for e in claim.evidence
        ) / len(claim.evidence)

        trust_score = (
            avg_domain * self.DOMAIN_WEIGHT +
            avg_similarity * self.SEMANTIC_WEIGHT
        ) * 100

        if trust_score >= 85:
            verdict = "SUPPORTED"

        elif trust_score >= 65:
            verdict = "LIKELY SUPPORTED"

        elif trust_score >= 45:
            verdict = "UNCERTAIN"

        else:
            verdict = "UNSUPPORTED"

        explanation = (
            f"Average domain score: {avg_domain:.2f}, "
            f"average semantic similarity: {avg_similarity:.2f}."
        )

        claim.trust_result = TrustResult(
            trust_score=round(trust_score, 2),
            verdict=verdict,
            explanation=explanation
        )

        return claim