# rag/vector_store/storage.py

import pickle
from pathlib import Path


class MetadataStorage:
    """
    Maintains mapping between FAISS vector ID and metadata.
    """

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.metadata = self._load()

    def _load(self):
        if self.path.exists():
            with open(self.path, "rb") as f:
                return pickle.load(f)
        return []

    def save(self):
        with open(self.path, "wb") as f:
            pickle.dump(self.metadata, f)

    def append(self, items: list[dict]):
        self.metadata.extend(items)
        self.save()

    def get_by_indices(self, indices: list[int]):
        return [self.metadata[i] for i in indices if i < len(self.metadata)]