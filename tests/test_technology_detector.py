from src.models.claim import Claim
from src.modules.technology_detector import TechnologyDetector


def test_claim(text: str):
    detector = TechnologyDetector()

    claim = Claim(text=text)

    detector.detect(claim)

    print(f"\nClaim: {text}")
    print("-" * 50)

    for entity in claim.entities:
        print(entity)


def main():
    test_claim("Python and React were developed using Git.")

    test_claim("GitHub uses PostgreSQL with Node.js.")

    test_claim("Google developed Gemini.")


if __name__ == "__main__":
    main()