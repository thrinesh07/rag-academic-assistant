# rag/services/ingestion_service.py

from rag.ingestion.pipeline import IngestionPipeline


class IngestionService:
    """
    Public ingestion interface.
    """

    def __init__(self):
        self.pipeline = IngestionPipeline()

    def ingest_all_documents(self):
        self.pipeline.ingest_all_documents()

    def ingest_single_document(self, file_path: str, subject: str):
        self.pipeline.ingest_single_document(file_path, subject)