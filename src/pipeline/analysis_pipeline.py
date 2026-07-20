from src.parser.response_parser import ResponseParser
from src.analysis.analysis_engine import AnalysisEngine
from src.scoring.trust_engine import TrustEngine
from src.report.report_generator import ReportGenerator
from src.analysis.syntax_analyzer import SyntaxAnalyzer
from src.analysis.runtime_analyzer import RuntimeAnalyzer
from src.analysis.security_analyzer import SecurityAnalyzer
from src.analysis.hallucination_analyzer import HallucinationAnalyzer

class AnalysisPipeline:
    """
    Coordinates the AI Code Trust Validator pipeline.
    """

    def __init__(self) -> None:

        self.parser = ResponseParser()
        self.analysis_engine = AnalysisEngine()
        self.trust_engine = TrustEngine()
        self.report_generator = ReportGenerator()
        
         # Register analyzers
        self.analysis_engine.register(SyntaxAnalyzer())
        self.analysis_engine.register(RuntimeAnalyzer())
        self.analysis_engine.register(SecurityAnalyzer())
        self.analysis_engine.register(HallucinationAnalyzer())
        
    def analyze(self, response: str):
        """
        Analyze an AI response containing code.
        """

        # Step 1: Parse the response
        parsed_response = self.parser.parse(response)

        # Step 2: Analyze every code block
        issues = []

        for block in parsed_response.code_blocks:
            issues.extend(
                self.analysis_engine.analyze(block)
        )

        # Step 3: Calculate trust score
        report = self.trust_engine.calculate(issues)

        # Step 4: Generate human-readable report
        return self.report_generator.generate(report)
    
    