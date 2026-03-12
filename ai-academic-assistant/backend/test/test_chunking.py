# tests/test_chunking.py

from rag.chunking.token_chunker import TokenChunker


def test_chunk_overlap():
    chunker = TokenChunker()

    text = "Deadlock occurs when processes compete for resources. " * 200

    base_metadata = {
        "subject": "os",
        "source": "test.pdf",
        "page": 1
    }

    chunks = chunker.chunk(text, base_metadata)

    assert len(chunks) > 1
    assert "chunk_id" in chunks[0]["metadata"]
    assert chunks[0]["metadata"]["subject"] == "os"