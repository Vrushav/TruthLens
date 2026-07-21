import sys
from pathlib import Path

from src.pipeline.analysis_pipeline import AnalysisPipeline


def main():
    if len(sys.argv) != 2:
        print("Usage:")
        print("    python -m truthlens <python_file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    if file_path.suffix != ".py":
        print("Error: Only Python (.py) files are supported.")
        sys.exit(1)

    try:
        code = file_path.read_text(encoding="utf-8")
    except Exception as exc:
        print(f"Unable to read file: {exc}")
        sys.exit(1)

    response = f"""```python
{code}
```"""

    print("=" * 60)
    print("TruthLens AI Code Trust Validator")
    print("=" * 60)
    print(f"Analyzing: {file_path}")
    print()

    pipeline = AnalysisPipeline()
    report = pipeline.analyze(response)

    print(report)


if __name__ == "__main__":
    main()
