from src.models.enums.analyzer_type import AnalyzerType
from src.models.enums.category import Category
from src.models.enums.severity import Severity


RULES = {

    "RUN001": {
        "analyzer": AnalyzerType.RUNTIME,
        "category": Category.RUNTIME,
        "severity": Severity.CRITICAL,
        "title": "Division by Zero",
        "message": "Division by zero will raise ZeroDivisionError.",
        "recommendation": "Ensure the denominator is not zero before dividing.",
        "references": [
            "Python ZeroDivisionError"
        ]
    },

    "SYN001": {
        "analyzer": AnalyzerType.SYNTAX,
        "category": Category.SYNTAX,
        "severity": Severity.HIGH,
        "title": "Syntax Error",
        "message": "Python syntax is invalid.",
        "recommendation": "Fix the syntax before executing the code.",
        "references": [
            "Python Language Reference"
        ]
    },

    "API001": {
        "analyzer": AnalyzerType.HALLUCINATION,
        "category": Category.HALLUCINATION,
        "severity": Severity.HIGH,
        "title": "Hallucinated API",
        "message": "The referenced API does not exist.",
        "recommendation": "Verify the API against the official documentation.",
        "references": [
            "Official Python Documentation"
         ]
    },

    "SEC001": {
        "analyzer": AnalyzerType.SECURITY,
        "category": Category.SECURITY,
        "severity": Severity.CRITICAL,
        "title": "Use of eval()",
        "message": "eval() executes arbitrary code and can lead to code injection.",
        "recommendation": "Avoid eval(). Use safer parsing methods such as ast.literal_eval() when appropriate.",
        "references": ["Python Security Guidelines"]
    },

    "SEC002": {
        "analyzer": AnalyzerType.SECURITY,
        "category": Category.SECURITY,
        "severity": Severity.CRITICAL,
        "title": "Use of exec()",
        "message": "exec() executes arbitrary Python code.",
        "recommendation": "Avoid exec() unless absolutely necessary.",
        "references": ["Python Security Guidelines"]
    },

    "SEC003": {
        "analyzer": AnalyzerType.SECURITY,
        "category": Category.SECURITY,
        "severity": Severity.HIGH,
        "title": "shell=True detected",
        "message": "Using shell=True may lead to command injection.",
        "recommendation": "Use subprocess without shell=True whenever possible.",
        "references": ["Python subprocess documentation"]
    },
    
}