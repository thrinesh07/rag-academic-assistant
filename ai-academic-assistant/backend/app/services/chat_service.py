from sqlalchemy.orm import Session
from app.models.chat import Chat
from app.models.message import Message
from app.models.user import User
from app.integrations.rag_adapter import generate_answer
from app.core.logger import logger


def generate_chat_response(
    db: Session,
    user: User,
    subject: str,
    question: str
):

    # -----------------------------------------
    # Create chat session
    # -----------------------------------------
    chat = Chat(user_id=user.id, subject=subject)
    db.add(chat)
    db.commit()
    db.refresh(chat)

    # -----------------------------------------
    # Call RAG
    # -----------------------------------------
    rag_result = generate_answer(
        question=question,
        subject=subject
    )

    raw_chunks = rag_result.get("chunks", [])

    # -----------------------------------------
    # Transform RAG chunks to API schema format
    # -----------------------------------------
    formatted_chunks = []

    for chunk in raw_chunks:
        formatted_chunks.append({
            "chunk_id": str(chunk.get("chunk_id", "")),
            "content_preview": chunk.get("text", "")[:300]
        })

    # -----------------------------------------
    # Store message in DB
    # -----------------------------------------
    message = Message(
        chat_id=chat.id,
        role="assistant",
        question=question,
        retrieved_context=str(raw_chunks),
        response=rag_result.get("answer")
    )

    db.add(message)
    db.commit()
    db.refresh(message)

    logger.info(f"Chat generated | user={user.email} | subject={subject}")

    # -----------------------------------------
    # Return structured response
    # -----------------------------------------
    return {
        "answer": rag_result.get("answer"),
        "retrieved_chunks": formatted_chunks,
        "subject": subject,
        "timestamp": message.timestamp,
    }