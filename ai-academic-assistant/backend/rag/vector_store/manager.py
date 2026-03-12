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

    Stores:
    - FAISS index
    - metadata_store (parallel list to vectors)
    """

    def __init__(self):
        self.index = None
        self.metadata_store = []
        self._load_or_initialize()

    # --------------------------------------------
    # LOAD OR CREATE
    # --------------------------------------------

    def _load_or_initialize(self):

        if os.path.exists(FAISS_INDEX_PATH) and os.path.exists(METADATA_PATH):

            logger.info("Loading existing FAISS index and metadata")

            self.index = faiss.read_index(str(FAISS_INDEX_PATH))

            with open(METADATA_PATH, "rb") as f:
                self.metadata_store = pickle.load(f)

        else:
            logger.info("Creating new FAISS index")

            self.index = faiss.IndexFlatIP(EMBEDDING_DIM)
            self.metadata_store = []

    # --------------------------------------------
    # ADD VECTORS
    # --------------------------------------------

    # rag/vector_store/manager.py

    def add(self, embeddings: np.ndarray, metadata_list: list):

        if embeddings.shape[1] != EMBEDDING_DIM:
            raise ValueError("Embedding dimension mismatch")

        embeddings = embeddings.astype("float32")

        self.index.add(embeddings)

        self.metadata_store.extend(metadata_list)

        self._persist()

    # --------------------------------------------
    # SAVE
    # --------------------------------------------

    def _persist(self):

        faiss.write_index(self.index, str(FAISS_INDEX_PATH))

        with open(METADATA_PATH, "wb") as f:
            pickle.dump(self.metadata_store, f)

    # --------------------------------------------
    # RECONSTRUCT
    # --------------------------------------------

    def reconstruct(self, idx: int):
        return self.index.reconstruct(idx)

    # --------------------------------------------
    # SIZE
    # --------------------------------------------

    def size(self):
        return self.index.ntotal


