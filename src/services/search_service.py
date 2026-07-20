import os
from urllib.parse import urlparse

from dotenv import load_dotenv
from tavily import TavilyClient

from src.models.evidence import Evidence

load_dotenv()


class SearchService:
    def __init__(self):
        api_key = os.getenv("TAVILY_API_KEY")

        if not api_key:
            raise ValueError("TAVILY_API_KEY not found in .env")

        self.client = TavilyClient(api_key=api_key)

    def search(self, query: str, max_results: int = 5) -> list[Evidence]:
        response = self.client.search(
            query=query,
            max_results=max_results,
        )

        evidence_list = []

        for result in response.get("results", []):
            domain = urlparse(result["url"]).netloc

            evidence = Evidence(
                title=result["title"],
                url=result["url"],
                snippet=result["content"],
                source=domain,
            )

            evidence_list.append(evidence)

        return evidence_list