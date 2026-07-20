from src.services.search_service import SearchService


def main():
    service = SearchService()

    evidence_list = service.search(
        "Python Guido van Rossum creator official"
    )

    for evidence in evidence_list:
        print("=" * 60)
        print(f"Title   : {evidence.title}")
        print(f"Source  : {evidence.source}")
        print(f"URL     : {evidence.url}")
        print(f"Snippet : {evidence.snippet[:200]}...")


if __name__ == "__main__":
    main()