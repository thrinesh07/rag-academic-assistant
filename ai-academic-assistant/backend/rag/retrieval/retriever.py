# rag/retrieval/retriever.py

import time
import numpy as np
from typing import Dict, Any

from rag.vector_store.manager import VectorIndex
from rag.embeddings.model import EmbeddingModel
from rag.config import MIN_SIMILARITY_THRESHOLD
from rag.utils.logger import get_logger


logger = get_logger(__name__)


class RetrievalService:

    def __init__(self):
        self.vector_store = VectorIndex()
        self.embedding_model = EmbeddingModel()

    def retrieve_context(self, query: str, subject: str, top_k: int = 3):

        start_time = time.time()

        query_embedding = self.embedding_model.embed([query])
        query_embedding = np.array(query_embedding).astype("float32")

        metadata_store = self.vector_store.metadata_store

        # STRICT subject filtering
        subject_indices = []

        for idx, meta in enumerate(metadata_store):

            if meta.get("subject", "").lower() == subject.lower():
                subject_indices.append(idx)

        if not subject_indices:
            return {
                "chunks": [],
                "scores": [],
                "latency_ms": int((time.time() - start_time) * 1000)
            }

        filtered_vectors = np.vstack([
            self.vector_store.reconstruct(i)
            for i in subject_indices
        ]).astype("float32")

        scores = np.dot(filtered_vectors, query_embedding.T).flatten()

        ranked = np.argsort(scores)[::-1]

        chunks = []
        similarities = []

        for r in ranked:

            idx = subject_indices[r]

            meta = metadata_store[idx]

            chunks.append({
                "text": meta["text"],
                "source": meta["source"],
                "page": meta["page"],
                "subject": meta["subject"]
            })

            similarities.append(float(scores[r]))

            if len(chunks) >= top_k:
                break

        latency = int((time.time() - start_time) * 1000)

        return {
            "chunks": chunks,
            "scores": similarities,
            "latency_ms": latency
        }