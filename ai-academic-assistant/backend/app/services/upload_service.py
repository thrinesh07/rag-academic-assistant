# from sqlalchemy.orm import Session
# from datetime import datetime
# from app.models.document import Document
# from app.core.constants import SUPPORTED_SUBJECTS
# from app.core.exceptions import ValidationError
# from rag_module import ingest_document  # external ingestion function


# def process_upload(db: Session, user_id: str, subject: str, file):

#     if subject not in SUPPORTED_SUBJECTS:
#         raise ValidationError("Invalid subject")

#     # Call RAG ingestion pipeline
#     ingest_document(file=file.file, subject=subject)

#     document = Document(
#         subject=subject,
#         file_name=file.filename,
#         indexed_at=datetime.utcnow()
#     )

#     db.add(document)
#     db.commit()
#     db.refresh(document)

#     return {
#         "document_id": str(document.id),
#         "subject": subject,
#         "file_name": document.file_name,
#         "indexed_at": document.indexed_at,
#         "status": "indexed"
#     }