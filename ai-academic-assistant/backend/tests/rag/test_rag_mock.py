from app.integrations.rag_adapter import generate_answer


def test_rag_wrapper(monkeypatch):

    def fake_rag(query, subject, top_k=3):
        return {
            "answer": "Fake answer",
            "retrieved_chunks": []
        }

    monkeypatch.setattr(
        "rag.services.rag_service.generate_answer",
        fake_rag
    )

    result = generate_answer("test", "OS")

    assert result["answer"] == "Fake answer"