from src.models.claim import Claim
from src.modules.parser import ResponseParser
from src.modules.entity_extractor import EntityExtractor
from src.modules.technology_detector import TechnologyDetector

class ValidationPipeline:
    """
    Coordinates all validation modules.
    """

    def __init__(self) -> None:

        self.parser = ResponseParser()
        self.entity_extractor = EntityExtractor()
        self.technology_detector = TechnologyDetector()

    def validate(self, response: str) -> list[Claim]:
      """
      Run the complete validation pipeline.
      """

      claim_texts = self.parser.get_claims(response)

      claims = [Claim(text=text) for text in claim_texts]

      for claim in claims:
        self.entity_extractor.extract(claim)
        self.technology_detector.detect(claim)

      return claims