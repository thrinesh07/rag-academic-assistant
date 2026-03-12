from sqlalchemy.orm import Session
from app.models.document import Document
from app.integrations.rag_adapter import ingest_document_to_rag
from app.core.logger import logger


def ingest_document(db: Session, subject: str, filename: str, file_bytes: bytes):

    # Call RAG ingestion pipeline
    ingest_document_to_rag(subject, filename, file_bytes)

    document = Document(
        subject=subject,
        file_name=filename,
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    logger.info(f"Document indexed: {filename}")

    return {
        "success": True,
        "document_id": document.id,
        "subject": subject,
        "indexed_at": document.indexed_at
    }