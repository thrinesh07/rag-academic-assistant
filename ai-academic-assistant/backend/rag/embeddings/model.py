# rag/embeddings/model.py

import os
import numpy as np
from sentence_transformers import SentenceTransformer
from transformers import logging

from rag.config import EMBEDDING_DIM
from rag.embeddings.device import get_device
from rag.embeddings.batching import batch_iterator
from rag.embeddings.normalization import normalize_vectors


logging.set_verbosity_error()


class EmbeddingModel:
    """
    Memory-safe embedding wrapper.

    Lazy loads the model only when embeddings
    are first requested.
    """

    _instance = None
    _model = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EmbeddingModel, cls).__new__(cls)
        return cls._instance

    def __init__(self):

        if hasattr(self, "_initialized"):
            return

        self.device = get_device()
        self.batch_size = 32 if self.device == "cuda" else 16

        self._initialized = True

    # ------------------------------------------------
    # LAZY LOAD MODEL
    # ------------------------------------------------

    def _load_model(self):

        if EmbeddingModel._model is not None:
            return

        local_path = os.path.join(
            os.getcwd(),
            "models",
            "all-MiniLM-L6-v2"
        )

        if not os.path.exists(local_path):
            raise RuntimeError(
                f"Embedding model not found at {local_path}"
            )

        print(f"[EmbeddingModel] Loading from: {local_path}")

        EmbeddingModel._model = SentenceTransformer(
            local_path,
            device=self.device
        )

    # ------------------------------------------------
    # EMBEDDINGS
    # ------------------------------------------------

    def embed(self, texts: list[str]):

        if not texts:
            return np.array([], dtype="float32")

        self._load_model()

        all_embeddings = []

        for batch in batch_iterator(texts, self.batch_size):

            embeddings = EmbeddingModel._model.encode(
                batch,
                convert_to_numpy=True,
                show_progress_bar=False
            )

            all_embeddings.append(embeddings)

        embeddings = np.vstack(all_embeddings)

        if embeddings.shape[1] != EMBEDDING_DIM:
            raise ValueError(
                f"Unexpected embedding dimension: {embeddings.shape[1]}"
            )

        embeddings = normalize_vectors(embeddings)

        return embeddings.astype("float32")