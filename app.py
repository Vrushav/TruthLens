from src.pipeline.validation_pipeline import ValidationPipeline


def main():

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

        if claim.trust_result is not None:

            print(f"Verdict: {claim.trust_result.verdict}")
            print(f"Trust Score: {claim.trust_result.trust_score:.2f}%")

        else:

            print("Verdict: Not Available")
            print("Trust Score: N/A")

        print("\nTop Evidence:")

        for evidence in claim.evidence:

            print(f"- {evidence.title}")
            print(f"  Source: {evidence.source}")
            print(f"  Similarity: {evidence.similarity_score:.2f}")


if __name__ == "__main__":
    main()
