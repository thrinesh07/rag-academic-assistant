from fastapi import UploadFile, HTTPException
from sqlalchemy.orm import Session
from app.services.upload_service import process_upload
from app.core.constants import ALLOWED_FILE_TYPES, MAX_UPLOAD_SIZE_MB
from app.core.logger import logger


def handle_upload(db: Session, user_id: str, subject: str, file: UploadFile):

    if file.content_type not in ALLOWED_FILE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid file type")

    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)

    if file_size > MAX_UPLOAD_SIZE_MB * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    result = process_upload(
        db=db,
        user_id=user_id,
        subject=subject,
        file=file
    )

    logger.info(f"Document uploaded | user={user_id} | file={file.filename}")

    return result