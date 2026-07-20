from src.analysis.security_analyzer import SecurityAnalyzer
from src.models.analysis.code_block import CodeBlock
from src.models.enums.category import Category


def test_eval_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code='eval("2+2")',
        start_line=1,
        end_line=1
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].category == Category.SECURITY


def test_exec_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code='exec("print(1)")',
        start_line=1,
        end_line=1
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1


def test_shell_true_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import subprocess
subprocess.run("ls", shell=True)
""",
        start_line=1,
        end_line=2
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1


def test_safe_subprocess():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import subprocess
subprocess.run(["ls"])
""",
        start_line=1,
        end_line=2
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0