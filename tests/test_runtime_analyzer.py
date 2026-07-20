from src.analysis.runtime_analyzer import RuntimeAnalyzer
from src.models.code_block import CodeBlock
from src.models.enums.category import Category


def test_division_by_zero():
    analyzer = RuntimeAnalyzer()

    block = CodeBlock(
        language="python",
        code="print(10 / 0)",
        start_line=1,
        end_line=1,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].category == Category.RUNTIME


def test_safe_division():
    analyzer = RuntimeAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
a = 10
b = 5
print(a / b)
""",
        start_line=1,
        end_line=3,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0