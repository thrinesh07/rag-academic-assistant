# rag/services/__init__.py

from rag.services.rag_service import RAGService
from rag.services.ingestion_service import IngestionService


# Create service instances
rag_service = RAGService()
ingestion_service = IngestionService()


# Public API
generate_answer = rag_service.generate_answer

ingest_all_documents = ingestion_service.ingest_all_documents
ingest_single_document = ingestion_service.ingest_single_document