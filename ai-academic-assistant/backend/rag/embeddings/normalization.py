# rag/embeddings/normalization.py

import numpy as np


def normalize_vectors(vectors: np.ndarray) -> np.ndarray:
    """
    Normalize embeddings to unit length.
    Required for cosine similarity using inner product.
    """

    norms = np.linalg.norm(vectors, axis=1, keepdims=True)

    # Avoid division by zero
    norms[norms == 0] = 1e-10

    return vectors / norms