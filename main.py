from src.pipeline.analysis_pipeline import AnalysisPipeline


def main():

    sample_response = '''
```python
import os

os.system("dir")
```
'''

    pipeline = AnalysisPipeline()

    report = pipeline.analyze(sample_response)

    print(report)


if __name__ == "__main__":
    main()