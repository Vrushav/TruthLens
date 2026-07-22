import json
from pathlib import Path


class KnowledgeLoader:
    """
    Loads API knowledge from JSON files.

    Example:
        loader = KnowledgeLoader()
        pandas = loader.load("pandas")
    """

    def __init__(self):

        self.base_path = Path(__file__).resolve().parent.parent / "knowledge"
        self._cache = {}

    def load(self, library: str):

        if library in self._cache:
            return self._cache[library]

        path = self.base_path / f"{library}.json"

        if not path.exists():
            self._cache[library] = set()
            return self._cache[library]

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self._cache[library] = set(data.get("valid", []))

        return self._cache[library]

    def exists(self, library: str, api: str) -> bool:

        return api in self.load(library)
