from collections import Counter
from pathlib import Path

from src.models.report import Report


class HTMLReportGenerator:
    """
    Generates an HTML report using an external HTML template.
    """

    TEMPLATE_FILE = Path("templates/report.html")

    def _severity_class(self, severity: str) -> str:
        return {
            "CRITICAL": "critical",
            "HIGH": "high",
            "MEDIUM": "medium",
            "LOW": "low",
        }.get(severity, "low")

    def generate(
        self,
        report: Report,
        output_file: str = "reports/truthlens_report.html",
    ) -> Path:

        template = self.TEMPLATE_FILE.read_text(encoding="utf-8")

        severity = Counter()

        for issue in report.issues:
            severity[issue.severity.name] += 1

        summary_table = f"""
<table>
<tr>
<th>Severity</th>
<th>Count</th>
</tr>

<tr>
<td>🔴 CRITICAL</td>
<td>{severity.get("CRITICAL", 0)}</td>
</tr>

<tr>
<td>🟠 HIGH</td>
<td>{severity.get("HIGH", 0)}</td>
</tr>

<tr>
<td>🟡 MEDIUM</td>
<td>{severity.get("MEDIUM", 0)}</td>
</tr>

<tr>
<td>🔵 LOW</td>
<td>{severity.get("LOW", 0)}</td>
</tr>
</table>
"""

        issue_cards = ""

        if report.issues:

            for issue in report.issues:

                severity_name = issue.severity.name
                severity_class = self._severity_class(severity_name)

                issue_cards += f"""
<div class="issue {severity_class}">

<h3>{severity_name} • {issue.title}</h3>

<p>
<strong>Analyzer:</strong>
{issue.analyzer.name}
</p>

<p>
<strong>Category:</strong>
{issue.category.name}
</p>

<p>
<strong>Line:</strong>
{issue.line if issue.line is not None else "-"}
</p>

<p>
<strong>Confidence:</strong>
{issue.confidence:.2f}
</p>

<p>
<strong>Description:</strong><br>
{issue.message}
</p>

<p>
<strong>Recommendation:</strong><br>
{issue.recommendation}
</p>

</div>
"""

        else:

            issue_cards = """
<div class="issue low">
<h3>✅ No Issues Detected</h3>
<p>The analysis completed successfully and no findings were reported.</p>
</div>
"""

        html = (
            template.replace(
                "{{TRUST_SCORE}}",
                f"{report.trust_score:.2f}/100",
            )
            .replace(
                "{{PRODUCTION_READY}}",
                "YES" if report.production_ready else "NO",
            )
            .replace(
                "{{READY_CLASS}}",
                "ready" if report.production_ready else "not-ready",
            )
            .replace(
                "{{TOTAL_ISSUES}}",
                str(len(report.issues)),
            )
            .replace(
                "{{SUMMARY_TABLE}}",
                summary_table,
            )
            .replace(
                "{{ISSUES}}",
                issue_cards,
            )
        )

        output_path = Path(output_file)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        output_path.write_text(
            html,
            encoding="utf-8",
        )

        return output_path