from sqlalchemy.orm import Session
from app.models.chat import Chat


class ChatRepository:

    @staticmethod
    def create(db: Session, user_id: str, subject: str):
        chat = Chat(
            user_id=user_id,
            subject=subject
        )
        db.add(chat)
        db.commit()
        db.refresh(chat)
        return chat

    @staticmethod
    def get_by_user(db: Session, user_id: str):
        return db.query(Chat).filter(Chat.user_id == user_id).all()

    @staticmethod
    def get_by_id(db: Session, chat_id: str):
        return db.query(Chat).filter(Chat.id == chat_id).first()