from src.models.claim import Claim
from src.models.entity import Entity

from src.verification.evidence_collector import EvidenceCollector
from src.verification.evidence_ranker import EvidenceRanker
from src.verification.semantic_verifier import SemanticVerifier
from src.verification.trust_engine import TrustEngine

claim = Claim(
    text="Python was created by Guido van Rossum."
)

claim.entities = [
    Entity("Python", "TECHNOLOGY"),
    Entity("Guido van Rossum", "PERSON")
]

collector = EvidenceCollector()
ranker = EvidenceRanker()
verifier = SemanticVerifier()
engine = TrustEngine()

claim = collector.collect(claim)
claim = ranker.rank(claim)
claim = verifier.verify(claim)
claim = engine.evaluate(claim)

print("\nClaim:")
print(claim.text)

print("\nTrust Result")
print("-" * 50)
print(f"Score      : {claim.trust_result.trust_score}")
print(f"Verdict    : {claim.trust_result.verdict}")
print(f"Explanation: {claim.trust_result.explanation}")