import argparse
import sys
from pathlib import Path

from truthlens import __version__
from src.pipeline.analysis_pipeline import AnalysisPipeline


def analyze_command(file_path: str) -> int:
    """
    Analyze a Python source file using TruthLens.
    """

    path = Path(file_path)

    if not path.exists():
        print(f"❌ Error: File '{path}' not found.")
        return 1

    if path.suffix != ".py":
        print("❌ Error: Only Python (.py) files are supported.")
        return 1

    try:
        code = path.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"❌ Unable to read file: {exc}")
        return 1

    response = f"""```python
{code}
```"""

    print("=" * 60)
    print(f"TruthLens AI Code Trust Validator v{__version__}")
    print("=" * 60)
    print()

    print(f"📄 Reading: {path}")
    print("✓ File loaded successfully")

    print()
    print("🔍 Running analysis...")
    print()

    pipeline = AnalysisPipeline()

    report = pipeline.analyze(response)

    print("✓ Analysis completed")
    print("✓ HTML report generated")
    print("✓ JSON report generated")

    print()
    print(report)

    return 0


def main() -> None:

    parser = argparse.ArgumentParser(
        prog="truthlens", description="TruthLens AI Code Trust Validator"
    )

    subparsers = parser.add_subparsers(dest="command")

    analyze_parser = subparsers.add_parser(
        "analyze", help="Analyze a Python source file"
    )

    analyze_parser.add_argument("file", help="Path to a Python (.py) file")

    args = parser.parse_args()

    if args.command == "analyze":
        sys.exit(analyze_command(args.file))

    parser.print_help()


if __name__ == "__main__":
    main()
