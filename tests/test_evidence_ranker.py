from src.models.verification.claim import Claim
from src.models.verification.entity import Entity
from src.verification.evidence_collector import EvidenceCollector
from src.verification.evidence_ranker import EvidenceRanker

claim = Claim(
    text="Python was created by Guido van Rossum."
)

claim.entities = [
    Entity("Python", "TECHNOLOGY"),
    Entity("Guido van Rossum", "PERSON")
]

collector = EvidenceCollector()
ranker = EvidenceRanker()

claim = collector.collect(claim)
claim = ranker.rank(claim)

for evidence in claim.evidence:
    print(f"{evidence.relevance_score:.2f} | {evidence.source}")