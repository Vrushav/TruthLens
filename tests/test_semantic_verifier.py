from src.models.verification.claim import Claim
from src.models.verification.entity import Entity
from src.verification.evidence_collector import EvidenceCollector
from src.verification.evidence_ranker import EvidenceRanker
from src.verification.semantic_verifier import SemanticVerifier

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

claim = collector.collect(claim)
claim = ranker.rank(claim)
claim = verifier.verify(claim)

for evidence in claim.evidence:
    print(f"{evidence.similarity_score:.3f} | {evidence.source}")