from src.analysis.security_analyzer import SecurityAnalyzer
from src.models.analysis.code_block import CodeBlock
from src.models.enums.category import Category


def test_eval_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code='eval("2+2")',
        start_line=1,
        end_line=1,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC001"
    assert issues[0].category == Category.SECURITY
    assert issues[0].line == 1


def test_exec_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code='exec("print(1)")',
        start_line=1,
        end_line=1,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC002"
    assert issues[0].line == 1


def test_shell_true_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import subprocess
subprocess.run("ls", shell=True)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC003"
    assert issues[0].line == 3


def test_safe_subprocess():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import subprocess
subprocess.run(["ls"])
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0


def test_hardcoded_credentials_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code='password = "admin123"',
        start_line=1,
        end_line=1,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC004"
    assert issues[0].line == 1


def test_os_system_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import os
os.system("ls")
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC005"
    assert issues[0].line == 3


def test_pickle_loads_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import pickle
pickle.loads(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC006"
    assert issues[0].line == 3


def test_pickle_imported_loads_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
from pickle import loads
loads(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC006"
    assert issues[0].line == 3


def test_json_loads_not_detected():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import json
json.loads("{}")
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0


# ---------------------------------------------------------
# SEC007
# ---------------------------------------------------------


def test_yaml_load_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import yaml
yaml.load(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC007"
    assert issues[0].category == Category.SECURITY
    assert issues[0].line == 3


def test_yaml_imported_load_detection():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
from yaml import load
load(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC007"
    assert issues[0].line == 3


def test_yaml_safe_load_not_detected():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import yaml
yaml.safe_load(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0


def test_yaml_imported_safe_load_not_detected():
    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
from yaml import safe_load
safe_load(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0


def test_md5_detection():

    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import hashlib
hashlib.md5(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC008"


def test_imported_md5_detection():

    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
from hashlib import md5
md5(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC008"


def test_md5_alias_detection():

    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import hashlib as h
h.md5(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 1
    assert issues[0].id == "SEC008"


def test_sha256_not_detected():

    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import hashlib
hashlib.sha256(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0


def test_blake2b_not_detected():

    analyzer = SecurityAnalyzer()

    block = CodeBlock(
        language="python",
        code="""
import hashlib
hashlib.blake2b(data)
""",
        start_line=1,
        end_line=2,
    )

    issues = analyzer.analyze(block)

    assert len(issues) == 0
