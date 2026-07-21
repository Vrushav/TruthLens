import json
from pathlib import Path

from src.models.report import Report


class JSONReportGenerator:
    """
    Generates a JSON report from a Report object.
    """

    OUTPUT_DIR = Path("reports")
    OUTPUT_FILE = OUTPUT_DIR / "truthlens_report.json"

    def generate(self, report: Report) -> Path:
        """
        Generate a JSON report and save it to the reports directory.
        """

        self.OUTPUT_DIR.mkdir(exist_ok=True)

        data = {
            "tool": "TruthLens",
            "version": "1.0.0",
            "trust_score": report.trust_score,
            "production_ready": report.production_ready,
            "total_issues": len(report.issues),
            "issues": [],
        }

        for issue in report.issues:
            data["issues"].append(
                {
                    "id": issue.id,
                    "analyzer": issue.analyzer.name,
                    "category": issue.category.name,
                    "severity": issue.severity.name,
                    "title": issue.title,
                    "message": issue.message,
                    "recommendation": issue.recommendation,
                    "line": issue.line,
                    "confidence": issue.confidence,
                    "references": issue.references,
                }
            )

        with open(self.OUTPUT_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return self.OUTPUT_FILE