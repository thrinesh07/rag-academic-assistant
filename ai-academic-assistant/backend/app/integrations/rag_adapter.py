import time
from typing import Dict, Any

from app.core.logger import logger
from app.core.exceptions import RAGProcessingError

# Import only public RAG services
from rag.services.rag_service import generate_answer as rag_generate_answer
from rag.services.ingestion_service import IngestionService


# ==========================================================
# GENERATE ANSWER WRAPPER
# ==========================================================

def generate_answer(question: str, subject: str) -> Dict[str, Any]:
    """
    Wrapper around RAG engine.
    Handles:
    - Latency tracking
    - Exception normalization
    - Response standardization
    """

    start_time = time.time()

    try:
        result = rag_generate_answer(
            query=question,
            subject=subject,
            top_k=3
        )

        latency = time.time() - start_time

        logger.info(
            f"RAG success | subject={subject} | latency={latency:.3f}s"
        )

        return {
            "answer": result.get("answer"),
            "chunks": result.get("retrieved_chunks", []),
            "latency": latency
        }

    except Exception as e:
        logger.error(f"RAG failure | subject={subject} | error={str(e)}")
        raise RAGProcessingError("Failed to generate response from RAG")


# ==========================================================
# DOCUMENT INGESTION WRAPPER
# ==========================================================

def ingest_document_to_rag(subject: str, filename: str, file_bytes: bytes):
    """
    Calls RAG ingestion pipeline.
    Backend does not handle embedding logic.
    """

    start_time = time.time()

    try:
        # RAG ingestion logic assumed to accept raw bytes
        IngestionService(
            subject=subject,
            filename=filename,
            file_bytes=file_bytes
        )

        latency = time.time() - start_time

        logger.info(
            f"Ingestion success | file={filename} | latency={latency:.3f}s"
        )

    except Exception as e:
        logger.error(f"Ingestion failure | file={filename} | error={str(e)}")
        raise RAGProcessingError("Document ingestion failed")

# ==========================================================
# HEALTH CHECK WRAPPER (LIGHTWEIGHT & CORRECT)
# ==========================================================

def check_rag_health() -> Dict[str, Any]:
    """
    Lightweight RAG availability check.
    Does NOT call LLM.
    Only verifies FAISS index loads correctly.
    """

    try:
        from rag.vector_store.manager import VectorIndex

        index = VectorIndex()
        index_size = index.size()

        return {
            "status": "healthy",
            "rag_loaded": True,
            "index_size": index_size
        }

    except Exception as e:
        logger.error(f"RAG health failure: {str(e)}")

        return {
            "status": "unhealthy",
            "rag_loaded": False
        }