from enum import Enum


class Category(Enum):
    SYNTAX = "Syntax"
    RUNTIME = "Runtime"
    SECURITY = "Security"
    HALLUCINATION = "Hallucination"
    BEST_PRACTICES = "Best Practices"
    EXPLANATION = "Explanation"