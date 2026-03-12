# tests/test_ingestion.py

from rag.ingestion.pipeline import IngestionPipeline


def test_ingestion_init():
    pipeline = IngestionPipeline()
    assert pipeline is not None