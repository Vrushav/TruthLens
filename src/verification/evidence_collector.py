from src.models.claim import Claim
from src.verification.query_builder import QueryBuilder
from src.services.search_service import SearchService


class EvidenceCollector:
    """
    Collects supporting evidence for a claim.
    """

    def __init__(self):
        self.query_builder = QueryBuilder()
        self.search_service = SearchService()

    def collect(self, claim: Claim) -> Claim:
        """
        Search for evidence and attach it to the claim.
        """

        query = self.query_builder.build(claim)

        evidence = self.search_service.search(query)

        claim.evidence = evidence

        return claim