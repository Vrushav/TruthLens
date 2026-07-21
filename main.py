from src.pipeline.analysis_pipeline import AnalysisPipeline


def main():

    sample_response = '''
```python
password = "admin123"

print(password)
```
'''

    pipeline = AnalysisPipeline()

    report = pipeline.analyze(sample_response)

    print(report)


if __name__ == "__main__":
    main()