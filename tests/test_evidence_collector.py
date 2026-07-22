from src.models.verification.claim import Claim
from src.models.verification.entity import Entity
from src.verification.evidence_collector import EvidenceCollector


collector = EvidenceCollector()

claim = Claim(
    text="Python was created by Guido van Rossum."
)

claim.entities = [
    Entity("Python", "TECHNOLOGY"),
    Entity("Guido van Rossum", "PERSON")
]

claim = collector.collect(claim)

print(f"\nClaim: {claim.text}\n")

for evidence in claim.evidence:
    print("=" * 60)
    print(evidence.title)
    print(evidence.source)
    print(evidence.url)