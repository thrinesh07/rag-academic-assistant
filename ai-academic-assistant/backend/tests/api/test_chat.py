import pytest


def mock_generate_answer(question, subject):
    return {
        "answer": "Mocked answer",
        "chunks": [{"document_id": "123", "content_preview": "Sample"}]
    }


def test_chat_flow(client, monkeypatch):

    # Register user
    client.post(
        "/api/v1/auth/register",
        json={
            "email": "chat@example.com",
            "password": "strongpassword"
        }
    )

    # Mock RAG
    monkeypatch.setattr(
        "app.integrations.rag_adapter.generate_answer",
        mock_generate_answer
    )

    response = client.post(
        "/api/v1/chat",
        json={
            "subject": "OS",
            "question": "What is deadlock?"
        }
    )

    assert response.status_code == 200
    assert response.json()["answer"] == "Mocked answer"