from src.parser.language_detector import LanguageDetector


def test_language_aliases():
    detector = LanguageDetector()

    assert detector.detect("py") == "python"
    assert detector.detect("js") == "javascript"
    assert detector.detect("yml") == "yaml"


def test_language_heuristics():
    detector = LanguageDetector()

    assert detector.detect("", 'print("Hello")') == "python"
    assert detector.detect("", "console.log('Hi')") == "javascript"
    assert detector.detect("", "SELECT * FROM users") == "sql"