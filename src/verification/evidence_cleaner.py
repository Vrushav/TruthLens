import re

from src.models.claim import Claim


class EvidenceCleaner:

    MAX_SNIPPET_LENGTH = 350

    def clean(self, claim: Claim) -> None:

        for evidence in claim.evidence:

            # ----------------------------
            # Clean title
            # ----------------------------

            title = evidence.title

            if title:
                title = re.sub(r"\s*\|\s*.*$", "", title)
                title = re.sub(r"\s*[-–]\s*.*$", "", title)

                evidence.title = title.strip()

            # ----------------------------
            # Clean snippet
            # ----------------------------

            snippet = evidence.snippet

            if not snippet:
                continue

            # Remove HTML tags
            snippet = re.sub(r"<[^>]+>", "", snippet)

            # Remove Markdown headings
            snippet = re.sub(r"#{1,6}\s*", "", snippet)

            # Remove Markdown links
            snippet = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", snippet)

            # Remove extra spaces/newlines
            snippet = re.sub(r"\s+", " ", snippet)

            snippet = snippet.strip()

            # Limit length
            if len(snippet) > self.MAX_SNIPPET_LENGTH:
                snippet = snippet[:self.MAX_SNIPPET_LENGTH] + "..."

            evidence.snippet = snippet