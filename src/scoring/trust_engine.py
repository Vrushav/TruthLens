from src.models.analysis.issue import Issue
from src.models.enums.severity import Severity
from src.models.report import Report


class TrustEngine:
    """
    Calculates the overall trust score and determines whether
    the analyzed code is suitable for production.
    """

    MAX_SCORE = 100
    MIN_PRODUCTION_SCORE = 70

    PENALTIES = {
        Severity.CRITICAL: 25,
        Severity.HIGH: 15,
        Severity.MEDIUM: 8,
        Severity.LOW: 3,
    }

    def calculate(self, issues: list[Issue]) -> Report:

        score = self.MAX_SCORE

        has_critical = False

        for issue in issues:

            score -= self.PENALTIES.get(issue.severity, 0)

            if issue.severity == Severity.CRITICAL:
                has_critical = True

        score = max(0, score)

        production_ready = not has_critical and score >= self.MIN_PRODUCTION_SCORE

        return Report(
            trust_score=score,
            production_ready=production_ready,
            issues=issues,
        )
