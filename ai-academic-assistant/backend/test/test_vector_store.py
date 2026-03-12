# tests/test_vector_store.py

import numpy as np
from rag.vector_store.manager import VectorIndex


def test_vector_add_and_search():
    vector_store = VectorIndex()

    embeddings = np.random.rand(5, 384).astype("float32")

    metadata = [
        {"subject": "os", "text": f"text {i}", "source": "test.pdf", "page": 1}
        for i in range(5)
    ]

    vector_store.add(embeddings, metadata)

    query = embeddings[0].reshape(1, -1)

    scores, results = vector_store.search(query, top_k=1)

    assert len(results) == 1