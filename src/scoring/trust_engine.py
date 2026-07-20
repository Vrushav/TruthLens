from src.models.analysis.issue import Issue
from src.models.report import Report
from src.models.enums.severity import Severity


class TrustEngine:

    PENALTIES = {
        Severity.CRITICAL: 25,
        Severity.HIGH: 15,
        Severity.MEDIUM: 8,
        Severity.LOW: 3,
    }

    def calculate(self, issues: list[Issue]) -> Report:

        score = 100

        for issue in issues:
            score -= self.PENALTIES.get(issue.severity, 0)

        score = max(0, score)

        return Report(
            trust_score=score,
            production_ready=score >= 80,
            issues=issues
        )