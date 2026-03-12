# tests/test_embeddings.py

import numpy as np
from rag.embeddings.model import EmbeddingModel


def test_embedding_dimension():
    model = EmbeddingModel()

    texts = ["Operating systems manage hardware."]
    vectors = model.embed(texts)

    assert vectors.shape == (1, 384)


def test_embedding_normalized():
    model = EmbeddingModel()

    texts = ["Test normalization."]
    vectors = model.embed(texts)

    norm = np.linalg.norm(vectors[0])
    assert abs(norm - 1.0) < 0.01