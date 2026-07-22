from enum import Enum


class AnalyzerType(Enum):
    SYNTAX = "Syntax"
    RUNTIME = "Runtime"
    SECURITY = "Security"
    HALLUCINATION = "Hallucination"
    BEST_PRACTICES = "Best Practices"
    EXPLANATION = "Explanation"