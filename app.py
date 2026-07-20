from src.pipeline.validation_pipeline import ValidationPipeline

pipeline = ValidationPipeline()

print("Enter an AI response (press Enter twice to finish):")

lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

response = "\n".join(lines)

claims = pipeline.validate(response)

for claim in claims:
    print("\n" + "=" * 80)
    print(f"Claim: {claim.text}")
    print(f"Verdict: {claim.trust_result.verdict}")
    print(f"Trust Score: {claim.trust_result.trust_score:.2f}%")

    print("\nTop Evidence:")
    for evidence in claim.evidence:
        print(f"- {evidence.title}")
        print(f"  Source: {evidence.source}")
        print(f"  Similarity: {evidence.similarity_score:.2f}")