from src.models.report import Report


class ReportGenerator:
    """
    Generates a human-readable report from the analysis result.
    """

    def generate(self, report: Report) -> str:

        lines = []

        lines.append("=" * 60)
        lines.append("TruthLens Analysis Report")
        lines.append("=" * 60)

        lines.append(f"Trust Score       : {report.trust_score}")
        lines.append(
            f"Production Ready  : {'YES' if report.production_ready else 'NO'}"
        )

        lines.append("")
        lines.append(f"Issues Found      : {len(report.issues)}")
        lines.append("-" * 60)

        if not report.issues:
            lines.append("No issues detected.")

        for issue in report.issues:

            lines.append(
                f"[{issue.severity.name}] {issue.title}"
            )

            if issue.line is not None:
                lines.append(f"Line: {issue.line}")

            lines.append(issue.message)
            lines.append(
                f"Recommendation: {issue.recommendation}"
            )

            lines.append("-" * 60)

        return "\n".join(lines)