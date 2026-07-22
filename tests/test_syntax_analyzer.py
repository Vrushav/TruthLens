from src.analysis.syntax_analyzer import SyntaxAnalyzer
from src.models.analysis.code_block import CodeBlock
from src.models.enums.category import Category

def test_valid_python():
    analyzer = SyntaxAnalyzer()

    block = CodeBlock(
        language="python",
        code='print("Hello")',
        start_line=1,
        end_line=1,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0


def test_invalid_python():
    analyzer = SyntaxAnalyzer()

    block = CodeBlock(
        language="python",
        code='print("Hello"',
        start_line=1,
        end_line=1,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1

    assert issues[0].category == Category.SYNTAX