from src.models.verification.claim import Claim
from src.verification.technology_detector import TechnologyDetector


def run_claim(text: str):
    detector = TechnologyDetector()

    claim = Claim(text=text)

    detector.detect(claim)

    print(f"\nClaim: {text}")
    print("-" * 50)

    for entity in claim.entities:
        print(entity)


def main():
    run_claim("Python and React were developed using Git.")
    run_claim("GitHub uses PostgreSQL with Node.js.")
    run_claim("Google developed Gemini.")

if __name__ == "__main__":
    main()