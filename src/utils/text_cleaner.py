import re


def clean_snippet(text: str) -> str:
    if not text:
        return ""

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove Markdown headings
    text = re.sub(r"#{1,6}\s*", "", text)

    # Collapse whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()