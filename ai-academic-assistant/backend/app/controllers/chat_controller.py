from sqlalchemy.orm import Session
from app.services.chat_service import process_chat_request
from app.core.logger import logger


def handle_chat(db: Session, user_id: str, subject: str, question: str):
    result = process_chat_request(
        db=db,
        user_id=user_id,
        subject=subject,
        question=question
    )

    logger.info(f"Chat processed | user={user_id} | subject={subject}")

    return result