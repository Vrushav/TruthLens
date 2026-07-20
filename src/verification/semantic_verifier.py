from sentence_transformers import SentenceTransformer, util
from src.models.claim import Claim


class SemanticVerifier:
    """
    Compares a claim with its evidence using semantic similarity.
    """

    def __init__(self):
        # Loads once when the verifier is created
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def verify(self, claim: Claim) -> Claim:
        """
        Computes semantic similarity between the claim
        and each evidence snippet.
        """

        claim_embedding = self.model.encode(
        claim.text,
        convert_to_tensor=True
)

        snippets = [e.snippet for e in claim.evidence]

        evidence_embeddings = self.model.encode(
        snippets,
        convert_to_tensor=True
)

        similarities = util.cos_sim(
        claim_embedding,
        evidence_embeddings
)[0]

        for evidence, score in zip(claim.evidence, similarities):
          evidence.similarity_score = score.item()

        # Highest similarity first
        claim.evidence.sort(
            key=lambda e: e.relevance_score,
            reverse=True
        )

        return claim