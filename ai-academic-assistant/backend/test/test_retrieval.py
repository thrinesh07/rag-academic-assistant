# tests/test_retrieval.py

from rag.retrieval.retriever import RetrievalService


def test_retrieval_structure():
    retriever = RetrievalService()

    result = retriever.retrieve_context(
        query="Explain scheduling",
        subject="os",
        top_k=2
    )

    assert "chunks" in result
    assert "scores" in result
    assert "latency_ms" in result