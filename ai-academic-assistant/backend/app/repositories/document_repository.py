from sqlalchemy.orm import Session
from app.models.document import Document


class DocumentRepository:

    @staticmethod
    def create(db: Session, subject: str, file_name: str):
        document = Document(
            subject=subject,
            file_name=file_name
        )

        db.add(document)
        db.commit()
        db.refresh(document)
        return document

    @staticmethod
    def get_by_subject(db: Session, subject: str):
        return db.query(Document).filter(Document.subject == subject).all()