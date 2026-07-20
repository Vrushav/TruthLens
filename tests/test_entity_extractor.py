from src.models import Claim
from src.verification.entity_extractor import EntityExtractor

extractor = EntityExtractor()

claim = Claim(
    text="Python was created by Guido van Rossum in 1991."
)

result = extractor.extract(claim)

print("\nEntities Found:\n")

for entity in result.entities:
    print(entity)