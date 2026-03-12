from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import List

from app.core.constants import ALLOWED_SUBJECTS


# ==========================================================
# REQUEST
# ==========================================================

class ChatRequest(BaseModel):
    subject: str
    question: str = Field(min_length=5, max_length=2000)

    @field_validator("subject")
    @classmethod
    def validate_subject(cls, value: str):
        if value not in ALLOWED_SUBJECTS:
            raise ValueError("Unsupported subject")
        return value


# ==========================================================
# RESPONSE
# ==========================================================

class RetrievedChunk(BaseModel):
    chunk_id: str   # NOT UUID — matches your RAG engine
    content_preview: str


class ChatResponse(BaseModel):
    answer: str
    retrieved_chunks: List[RetrievedChunk]
    subject: str
    timestamp: datetime