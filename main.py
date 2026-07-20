from src.pipeline.analysis_pipeline import AnalysisPipeline


def main():

    sample_response = '''
```python
name = input()

eval(name)
```
'''

    pipeline = AnalysisPipeline()

    report = pipeline.analyze(sample_response)

    print(report)


if __name__ == "__main__":
    main()