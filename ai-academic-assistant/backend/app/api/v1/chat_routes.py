from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

from rag.services import generate_answer
from rag.constants import SUPPORTED_SUBJECTS
from rag.utils.logger import get_logger


router = APIRouter()
logger = get_logger("chat")


class ChatRequest(BaseModel):
    subject: str
    question: str


@router.post("")
async def chat_endpoint(payload: ChatRequest):
    try:
        # ---------------------------------------------
        # Normalize subject
        # ---------------------------------------------

        subject = payload.subject.lower().strip()

        if subject not in SUPPORTED_SUBJECTS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid subject. Allowed: {list(SUPPORTED_SUBJECTS.keys())}"
            )

        # ---------------------------------------------
        # Generate RAG response
        # ---------------------------------------------

        rag_response = generate_answer(
            query=payload.question,
            subject=subject
        )

        return {
            "answer": rag_response["answer"],
            "retrieved_chunks": [
    {
        "chunk_id": chunk.get("chunk_id", f"chunk_{i}"),
        "content_preview": chunk.get("text", "")[:200]
    }
    for i, chunk in enumerate(rag_response["retrieved_chunks"])
],
            "subject": subject,
            "timestamp": datetime.utcnow().isoformat()
        }

    except HTTPException:
        raise

    except Exception as e:
        logger.exception("Chat generation failed")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to generate response from RAG: {str(e)}"
        )

