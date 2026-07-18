from src.pipeline.validation_pipeline import ValidationPipeline


def main():
    pipeline = ValidationPipeline()

    response = """
    Python was created by Guido van Rossum.
    React is maintained by Meta.
    GitHub hosts millions of repositories.
    """

    claims = pipeline.validate(response)

    for i, claim in enumerate(claims, start=1):
        print(f"\nClaim {i}")
        print("-" * 40)
        print("Text:", claim.text)

        print("Entities:")
        for entity in claim.entities:
            print(f"  {entity}")


if __name__ == "__main__":
    main()