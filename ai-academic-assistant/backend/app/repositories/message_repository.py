from sqlalchemy.orm import Session
from app.models.message import Message


class MessageRepository:

    @staticmethod
    def create(
        db: Session,
        chat_id: str,
        role: str,
        question: str,
        retrieved_context: str,
        response: str
    ):
        message = Message(
            chat_id=chat_id,
            role=role,
            question=question,
            retrieved_context=retrieved_context,
            response=response
        )

        db.add(message)
        db.commit()
        db.refresh(message)
        return message

    @staticmethod
    def get_by_chat(db: Session, chat_id: str):
        return (
            db.query(Message)
            .filter(Message.chat_id == chat_id)
            .order_by(Message.timestamp.asc())
            .all()
        )