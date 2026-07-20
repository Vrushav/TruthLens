from src.models.issue import Issue
from src.rules.rule_registry import RULES


class IssueFactory:

    @staticmethod
    def create(rule_id: str, **kwargs) -> Issue:

        rule = RULES[rule_id]

        return Issue(

            id=rule_id,

            analyzer=rule["analyzer"],

            severity=rule["severity"],

            category=rule["category"],

            title=rule["title"],

            message=kwargs.get("message", rule["message"]),

            recommendation=kwargs.get(
                "recommendation",
                rule["recommendation"]
            ),

            line=kwargs.get("line"),

            confidence=kwargs.get("confidence", 1.0),

            references=rule["references"]

        )