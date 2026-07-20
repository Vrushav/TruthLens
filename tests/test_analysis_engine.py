from src.analysis.analysis_engine import AnalysisEngine
from src.analysis.syntax_analyzer import SyntaxAnalyzer
from src.models.analysis.code_block import CodeBlock
from src.models.enums.category import Category
from src.analysis.runtime_analyzer import RuntimeAnalyzer
from src.analysis.security_analyzer import SecurityAnalyzer

def test_analysis_engine():
    engine = AnalysisEngine()

    engine.register(SyntaxAnalyzer())
    engine.register(RuntimeAnalyzer())
    engine.register(SecurityAnalyzer())

    block = CodeBlock(
        language="python",
        code='print("Hello"',
        start_line=1,
        end_line=1,
    )

    issues = engine.analyze(block)

    assert len(issues) == 1
    assert issues[0].category == Category.SYNTAX