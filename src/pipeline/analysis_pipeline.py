from src.parser.response_parser import ResponseParser
from src.analysis.analysis_engine import AnalysisEngine
from src.analysis.syntax_analyzer import SyntaxAnalyzer
from src.analysis.runtime_analyzer import RuntimeAnalyzer
from src.analysis.security_analyzer import SecurityAnalyzer
from src.analysis.hallucination_analyzer import HallucinationAnalyzer

from src.scoring.trust_engine import TrustEngine

from src.report.report_generator import ReportGenerator
from src.report.html_report_generator import HTMLReportGenerator


class AnalysisPipeline:
    """
    Coordinates the AI Code Trust Validator pipeline.
    """

    def __init__(self) -> None:

        self.parser = ResponseParser()

        self.analysis_engine = AnalysisEngine()

        self.trust_engine = TrustEngine()

        self.report_generator = ReportGenerator()
        self.html_report_generator = HTMLReportGenerator()

        # Register analyzers

        self.analysis_engine.register(SyntaxAnalyzer())

        self.analysis_engine.register(RuntimeAnalyzer())

        self.analysis_engine.register(SecurityAnalyzer())

        self.analysis_engine.register(HallucinationAnalyzer())

    def analyze(self, response: str):
        """
        Analyze an AI response containing code.
        """

        parsed_response = self.parser.parse(response)

        issues = []

        for block in parsed_response.code_blocks:

            issues.extend(self.analysis_engine.analyze(block))

        report = self.trust_engine.calculate(issues)

        # Generate HTML report
        self.html_report_generator.generate(report)

        # Generate console report
        return self.report_generator.generate(report)
