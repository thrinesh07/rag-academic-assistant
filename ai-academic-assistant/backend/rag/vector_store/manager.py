# rag/vector_store/manager.py

import os
import faiss
import pickle
import numpy as np

from rag.config import FAISS_INDEX_PATH, METADATA_PATH, EMBEDDING_DIM
from rag.utils.logger import get_logger


logger = get_logger(__name__)


class VectorIndex:
    """
    FAISS vector index manager.

    Lazy initialization to prevent heavy startup on
    low-memory environments (Render free tier).
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(VectorIndex, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        self.index = None
        self.metadata_store = []

        self._initialized = True

    # ------------------------------------------------
    # LAZY LOAD
    # ------------------------------------------------

    def _ensure_loaded(self):

        if self.index is not None:
            return

        if os.path.exists(FAISS_INDEX_PATH) and os.path.exists(METADATA_PATH):

            logger.info("Loading existing FAISS index")

            self.index = faiss.read_index(str(FAISS_INDEX_PATH))

            with open(METADATA_PATH, "rb") as f:
                self.metadata_store = pickle.load(f)

        else:

            logger.info("Creating new FAISS index")

            self.index = faiss.IndexFlatIP(EMBEDDING_DIM)
            self.metadata_store = []

    # ------------------------------------------------
    # ADD
    # ------------------------------------------------

    def add(self, embeddings: np.ndarray, metadata_list: list):

        self._ensure_loaded()

        if embeddings.shape[1] != EMBEDDING_DIM:
            raise ValueError("Embedding dimension mismatch")

        embeddings = embeddings.astype("float32")

        self.index.add(embeddings)

        self.metadata_store.extend(metadata_list)

        self._persist()

    # ------------------------------------------------
    # SEARCH
    # ------------------------------------------------

    def search(self, query_embedding: np.ndarray, k: int):

        self._ensure_loaded()

        query_embedding = query_embedding.astype("float32")

        scores, indices = self.index.search(query_embedding, k)

        results = []

        for idx in indices[0]:
            if idx < len(self.metadata_store):
                results.append(self.metadata_store[idx])

        return results

    # ------------------------------------------------
    # RECONSTRUCT VECTOR (FIX FOR RETRIEVER)
    # ------------------------------------------------

    def reconstruct(self, idx: int):
        """
        Returns embedding vector from FAISS index.
        Required for subject-filtered retrieval.
        """

        self._ensure_loaded()

        if idx >= self.index.ntotal:
            raise IndexError("Vector index out of range")

        return self.index.reconstruct(idx)

    # ------------------------------------------------
    # SAVE
    # ------------------------------------------------

    def _persist(self):

        faiss.write_index(self.index, str(FAISS_INDEX_PATH))

        with open(METADATA_PATH, "wb") as f:
            pickle.dump(self.metadata_store, f)

    # ------------------------------------------------
    # SIZE
    # ------------------------------------------------

    def size(self):

        self._ensure_loaded()

        return self.index.ntotal