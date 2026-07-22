from src.models.verification.claim import Claim
from src.models.verification.entity import Entity
from src.verification.query_builder import QueryBuilder


builder = QueryBuilder()

claim = Claim(
    text="Python was created by Guido van Rossum."
)

claim.entities = [
    Entity("Python", "TECHNOLOGY"),
    Entity("Guido van Rossum", "PERSON")
]

print(builder.build(claim))