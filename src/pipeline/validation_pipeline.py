from src.models.verification.claim import Claim
from src.verification.parser import ResponseParser
from src.verification.entity_extractor import EntityExtractor
from src.verification.technology_detector import TechnologyDetector
from src.verification.evidence_collector import EvidenceCollector
from src.verification.evidence_ranker import EvidenceRanker
from src.verification.semantic_verifier import SemanticVerifier
from src.verification.trust_engine import TrustEngine
from src.verification.evidence_cleaner import EvidenceCleaner

class ValidationPipeline:
    """
    Coordinates all validation modules.
    """

    def __init__(self) -> None:

        self.parser = ResponseParser()
        self.entity_extractor = EntityExtractor()
        self.technology_detector = TechnologyDetector()
        self.evidence_collector = EvidenceCollector()
        self.evidence_cleaner = EvidenceCleaner()
        self.evidence_ranker = EvidenceRanker()
        self.semantic_verifier = SemanticVerifier()
        self.trust_engine = TrustEngine()

    def validate(self, response: str) -> list[Claim]:
      """
      Run the complete validation pipeline.
      """

      claim_texts = self.parser.get_claims(response)

      claims = [Claim(text=text) for text in claim_texts]

      for claim in claims:
        self.entity_extractor.extract(claim)
        self.technology_detector.detect(claim)
        self.evidence_collector.collect(claim)
        self.evidence_ranker.rank(claim)
        self.semantic_verifier.verify(claim)
        self.trust_engine.evaluate(claim)

      return claims