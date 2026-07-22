from src.models import report
from src.parser.response_parser import ResponseParser
from src.analysis.analysis_engine import AnalysisEngine
from src.analysis.syntax_analyzer import SyntaxAnalyzer
from src.analysis.runtime_analyzer import RuntimeAnalyzer
from src.analysis.security_analyzer import SecurityAnalyzer
from src.analysis.hallucination_analyzer import HallucinationAnalyzer

from src.scoring.trust_engine import TrustEngine

from src.report.report_generator import ReportGenerator
from src.report.html_report_generator import HTMLReportGenerator
from src.report.json_report_generator import JSONReportGenerator


class AnalysisPipeline:
    """
    Coordinates the TruthLens AI Code Trust Validator pipeline.
    """

    def __init__(self) -> None:

        self.parser = ResponseParser()

        self.analysis_engine = AnalysisEngine()

        self.trust_engine = TrustEngine()

        self.report_generator = ReportGenerator()
        self.html_report_generator = HTMLReportGenerator()
        self.json_report_generator = JSONReportGenerator()

        # Register analyzers
        self.analysis_engine.register(SyntaxAnalyzer())
        self.analysis_engine.register(RuntimeAnalyzer())
        self.analysis_engine.register(SecurityAnalyzer())
        self.analysis_engine.register(HallucinationAnalyzer())

    def analyze(self, response: str) -> str:
        """
        Analyze an AI response containing Python code.

        Returns:
            str: Human-readable console report.
        """

        # Step 1: Parse the AI response
        parsed_response = self.parser.parse(response)

        # Step 2: Analyze every extracted code block
        issues = []

        for block in parsed_response.code_blocks:
            issues.extend(self.analysis_engine.analyze(block))

        # Step 3: Calculate trust score
        report = self.trust_engine.calculate(issues)

        # Step 4: Generate all report formats
        html_path = self.html_report_generator.generate(report)
        self.json_report_generator.generate(report)

        # Step 5: Return console report and HTML report path
        return self.report_generator.generate(report), html_path
