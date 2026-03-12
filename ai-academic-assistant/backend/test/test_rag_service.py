# tests/test_rag_service.py

from rag.services.rag_service import RAGService


def test_rag_output_structure(monkeypatch):
    rag = RAGService()

    def fake_generate(prompt):
        return {
            "text": "Mock answer",
            "latency_ms": 10
        }

    monkeypatch.setattr(rag.llm, "generate", fake_generate)

    result = rag.generate_answer(
        query="Explain deadlock",
        subject="os",
        top_k=1
    )

    assert "answer" in result
    assert "latency_ms" in result