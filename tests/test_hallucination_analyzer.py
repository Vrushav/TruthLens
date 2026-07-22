from src.analysis.hallucination_analyzer import HallucinationAnalyzer
from src.models.analysis.code_block import CodeBlock
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


def test_requests_alias_detection():

    analyzer = HallucinationAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import requests as r
r.fetch("https://example.com")
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "API001"


def test_pandas_alias_detection():

    analyzer = HallucinationAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import pandas as pd
pd.load_excel("file.xlsx")
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "API001"


def test_numpy_alias_detection():

    analyzer = HallucinationAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import numpy as np
np.average_value(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "API001"


def test_pandas_suggestion():

    analyzer = HallucinationAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import pandas
pandas.load_excel("file.xlsx")
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert "read_excel" in issues[0].recommendation


def test_requests_suggestion():

    analyzer = HallucinationAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import requests
requests.fetch("https://example.com")
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert "Did you mean" in issues[0].recommendation
