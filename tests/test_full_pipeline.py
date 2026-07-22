from src.pipeline.validation_pipeline import ValidationPipeline

pipeline = ValidationPipeline()

response = """
Python was created by Guido van Rossum.

React is maintained by Meta.

GitHub hosts millions of repositories.
"""

claims = pipeline.validate(response)

for i, claim in enumerate(claims, start=1):
    print("=" * 80)
    print(f"Claim {i}: {claim.text}")

    print("\nEntities:")
    for entity in claim.entities:
        print(f"  - {entity.text} ({entity.label})")

    print("\nEvidence:")
    for evidence in claim.evidence[:3]:
        print(f"• {evidence.title}")
        print(f"  Source : {evidence.source}")
        print(f"  URL    : {evidence.url}")