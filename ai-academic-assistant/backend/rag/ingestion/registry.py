# rag/ingestion/registry.py

import pickle
from pathlib import Path


class DocumentRegistry:
    """
    Maintains set of indexed document hashes.
    """

    def __init__(self, registry_path: Path):
        self.registry_path = registry_path
        self.registry_path.parent.mkdir(parents=True, exist_ok=True)
        self._registry = self._load()

    def _load(self):
        if self.registry_path.exists():
            with open(self.registry_path, "rb") as f:
                return pickle.load(f)
        return set()

    def save(self):
        with open(self.registry_path, "wb") as f:
            pickle.dump(self._registry, f)

    def exists(self, file_hash: str) -> bool:
        return file_hash in self._registry

    def add(self, file_hash: str):
        self._registry.add(file_hash)
        self.save()