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
    Production-safe embedding wrapper.

    - Uses local all-MiniLM-L6-v2 model
    - 384 dimensional output
    - Normalized vectors for cosine similarity
    - Singleton pattern to prevent multiple loads
    """

    _instance = None
    _model = None  # Shared model object

    # --------------------------------------------------
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EmbeddingModel, cls).__new__(cls)
        return cls._instance

    # --------------------------------------------------
    def __init__(self):
        if hasattr(self, "_initialized"):
            return

        self.device = get_device()

        # Load model only once
        if EmbeddingModel._model is None:
            EmbeddingModel._model = self._load_local_model()

        self.model = EmbeddingModel._model

        self.batch_size = 32 if self.device == "cuda" else 16

        self._initialized = True

    # --------------------------------------------------
    def _load_local_model(self):
        """
        Force load model from local path only.
        Prevents runtime HuggingFace downloads.
        """

        local_path = os.path.join(
            os.getcwd(),
            "models",
            "all-MiniLM-L6-v2"
        )

        if not os.path.exists(local_path):
            raise RuntimeError(
                f"Local embedding model not found at: {local_path}"
            )

        print(f"[EmbeddingModel] Loading from: {local_path}")

        return SentenceTransformer(
            local_path,
            device=self.device
        )

    # --------------------------------------------------
    def embed(self, texts: list[str]):
        """
        Generates normalized embeddings.
        """

        if not texts:
            return np.array([], dtype="float32")

        all_embeddings = []

        for batch in batch_iterator(texts, self.batch_size):
            embeddings = self.model.encode(
                batch,
                convert_to_numpy=True,
                show_progress_bar=False
            )

            all_embeddings.append(embeddings)

        embeddings = np.vstack(all_embeddings)

        # Dimension safety check
        if embeddings.shape[1] != EMBEDDING_DIM:
            raise ValueError(
                f"Unexpected embedding dimension: {embeddings.shape[1]}"
            )

        embeddings = normalize_vectors(embeddings)

        return embeddings.astype("float32")