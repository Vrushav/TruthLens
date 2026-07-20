from src.analysis.hallucination_analyzer import HallucinationAnalyzer
from src.models.code_block import CodeBlock
from src.models.enums.category import Category


def test_fake_requests_api():

    analyzer = HallucinationAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import requests

requests.fetch("https://example.com")
""",
        start_line=1,
        end_line=3
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].category == Category.HALLUCINATION


def test_real_requests_api():

    analyzer = HallucinationAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import requests

requests.get("https://example.com")
""",
        start_line=1,
        end_line=3
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0