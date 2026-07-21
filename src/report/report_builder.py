from collections import Counter

from src.models.report import Report


class ReportBuilder:
    """
    Builds a Report object and provides helper methods
    for report statistics.
    """

    def build(
        self,
        trust_score: float,
        issues: list,
        production_ready: bool,
    ) -> Report:

        return Report(
            trust_score=trust_score,
            production_ready=production_ready,
            issues=issues,
        )

    def severity_summary(self, report: Report) -> dict:

        counter = Counter()

        for issue in report.issues:
            counter[issue.severity.name] += 1

        return dict(counter)

    def total_issues(self, report: Report) -> int:

        return len(report.issues)
