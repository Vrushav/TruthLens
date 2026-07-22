from collections import Counter

from src.models.report import Report


class ReportGenerator:
    """
    Generates a human-readable report.
    """

    def generate(self, report: Report) -> str:

        lines = []

        lines.append("=" * 60)
        lines.append("               TruthLens Analysis Report")
        lines.append("=" * 60)

        lines.append(f"Trust Score       : {report.trust_score:.2f}/100")
        lines.append(
            f"Production Ready  : {'YES' if report.production_ready else 'NO'}"
        )
        lines.append(f"Total Issues      : {len(report.issues)}")

        lines.append("")

        severity = Counter()

        for issue in report.issues:
            severity[issue.severity.name] += 1

        if severity:

            lines.append("Issue Summary")
            lines.append("-" * 60)

            for level in [
                "CRITICAL",
                "HIGH",
                "MEDIUM",
                "LOW",
                "INFO",
            ]:
                if level in severity:
                    lines.append(f"{level:<10}: {severity[level]}")

            lines.append("")

        lines.append("-" * 60)

        if not report.issues:

            lines.append("No issues detected.")

        else:

            for issue in report.issues:

                lines.append(f"[{issue.severity.name}] {issue.title}")

                if issue.line is not None:
                    lines.append(f"Line: {issue.line}")

                lines.append(issue.message)
                lines.append(f"Recommendation: {issue.recommendation}")

                lines.append("-" * 60)

        lines.append("Summary")
        lines.append("-" * 60)

        if report.production_ready:
            lines.append("The analyzed code is suitable for production use.")
        else:
            lines.append(
                "The analyzed code requires improvements before production deployment."
            )

        lines.append("=" * 60)

        return "\n".join(lines)
