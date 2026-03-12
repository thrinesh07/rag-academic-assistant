# rag/vector_store/index.py

import faiss
from pathlib import Path
from rag.config import FAISS_INDEX_PATH, EMBEDDING_DIM


class FaissIndex:
    """
    Manages FAISS index lifecycle.
    """

    def __init__(self):
        FAISS_INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        self.index = self._load_or_create()

    def _load_or_create(self):
        if FAISS_INDEX_PATH.exists():
            return faiss.read_index(str(FAISS_INDEX_PATH))

        # Inner Product index (for cosine similarity with normalized vectors)
        return faiss.IndexFlatIP(EMBEDDING_DIM)

    def save(self):
        faiss.write_index(self.index, str(FAISS_INDEX_PATH))

    def add(self, embeddings):
        self.index.add(embeddings)
        self.save()

    def search(self, query_embedding, top_k: int):
        return self.index.search(query_embedding, top_k)

    def size(self):
        return self.index.ntotal