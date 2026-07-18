# TruthLens API Contract

## ResponseParser

Input:
- Raw AI response (str)

Output:
- List[Claim]

---

## EntityExtractor

Input:
- Claim

Output:
- Claim (with entities)

---

## TechnologyDetector

Input:
- Claim

Output:
- Claim (with technology entities)

---

## EvidenceCollector

Input:
- Claim

Output:
- Claim (with evidence)

---

## SemanticVerifier

Input:
- Claim

Output:
- Claim (with similarity scores)

---

## TrustEngine

Input:
- Claim

Output:
- Claim (with TrustResult)