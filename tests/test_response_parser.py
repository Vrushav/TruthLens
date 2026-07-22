from src.parser.response_parser import ResponseParser


def test_parser():
    parser = ResponseParser()

    sample = """
Python is dynamically typed.

```python
print("Hello")
print(10/0)
```

pip install pandas

Git was created by Linus Torvalds.
"""

    result = parser.parse(sample)

    assert len(result.code_blocks) == 1
    assert result.code_blocks[0].language == "python"

    assert len(result.commands) == 1

    assert len(result.text_sections) == 2