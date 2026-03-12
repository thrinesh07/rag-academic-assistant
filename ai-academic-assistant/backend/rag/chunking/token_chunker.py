# rag/chunking/token_chunker.py

from transformers import AutoTokenizer
from rag.config import (
    EMBEDDING_MODEL_NAME,
    CHUNK_SIZE,
    CHUNK_OVERLAP
)
from rag.chunking.metadata_builder import build_metadata
from rag.chunking.validation import validate_text


class TokenChunker:
    """
    Token-aware chunking using the embedding model tokenizer.

    Why token-based?
    - LLMs and embedding models operate on tokens.
    - Character slicing breaks semantic boundaries.
    - Ensures chunk fits model context window.
    """

    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(
            EMBEDDING_MODEL_NAME,
            use_fast=True
        )

    def chunk(self, text: str, base_metadata: dict) -> list[dict]:
        """
        Splits text into overlapping token chunks.

        Returns:
        [
            {
                "text": "...",
                "metadata": {...}
            }
        ]
        """

        if not validate_text(text):
            return []

        tokens = self.tokenizer.encode(
            text,
            add_special_tokens=False
        )

        if not tokens:
            return []

        chunks = []
        start = 0
        chunk_id = 0
        total_tokens = len(tokens)

        while start < total_tokens:
            end = start + CHUNK_SIZE
            chunk_tokens = tokens[start:end]

            chunk_text = self.tokenizer.decode(
                chunk_tokens,
                skip_special_tokens=True
            ).strip()

            if chunk_text:
                metadata = build_metadata(
                    base_metadata,
                    chunk_id=chunk_id,
                    token_count=len(chunk_tokens)
                )

                chunks.append({
                    "text": chunk_text,
                    "metadata": metadata
                })

            start += CHUNK_SIZE - CHUNK_OVERLAP
            chunk_id += 1

        return chunks