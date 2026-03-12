# rag/services/health_service.py

from rag.vector_store.manager import VectorIndex


class HealthService:
    """
    Basic health diagnostics.
    """

    def __init__(self):
        self.vector_index = VectorIndex()

    def status(self):
        return {
            "vector_count": self.vector_index.size(),
            "status": "healthy"
        }