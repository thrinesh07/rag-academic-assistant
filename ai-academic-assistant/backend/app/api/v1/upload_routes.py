# api/v1/upload.py

from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from pathlib import Path
import shutil
import uuid

from rag.services import ingest_single_document
from rag.constants import SUPPORTED_SUBJECTS
from rag.config import MAX_FILE_SIZE_MB
from rag.utils.file_utils import validate_pdf
from rag.utils.logger import get_logger


router = APIRouter()
logger = get_logger("upload")

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

MAX_FILE_SIZE_BYTES = MAX_FILE_SIZE_MB * 1024 * 1024


@router.post("/")
async def upload_document(
    subject: str = Query(..., description="Subject key (os, dbms, cn, dsa, oops)"),
    file: UploadFile = File(...)
):
    try:
        # --------------------------------------------------
        # Normalize Subject
        # --------------------------------------------------

        subject = subject.lower().strip()

        if subject not in SUPPORTED_SUBJECTS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid subject. Allowed: {list(SUPPORTED_SUBJECTS.keys())}"
            )

        # --------------------------------------------------
        # Validate File Extension
        # --------------------------------------------------

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(
                status_code=400,
                detail="Only PDF files are allowed"
            )

        # --------------------------------------------------
        # Validate File Size (Before Saving)
        # --------------------------------------------------

        contents = await file.read()

        if len(contents) > MAX_FILE_SIZE_BYTES:
            raise HTTPException(
                status_code=400,
                detail=f"File exceeds maximum size of {MAX_FILE_SIZE_MB} MB"
            )

        # --------------------------------------------------
        # Save File Safely
        # --------------------------------------------------

        unique_name = f"{uuid.uuid4().hex}_{file.filename}"
        temp_path = UPLOAD_DIR / unique_name

        with temp_path.open("wb") as buffer:
            buffer.write(contents)

        # --------------------------------------------------
        # Validate PDF Structure (Extra Safety)
        # --------------------------------------------------

        validate_pdf(str(temp_path))

        # --------------------------------------------------
        # Move File Into Subject Folder
        # --------------------------------------------------

        subject_dir = Path("data") / subject
        subject_dir.mkdir(parents=True, exist_ok=True)

        final_path = subject_dir / unique_name
        temp_path.replace(final_path)

        # --------------------------------------------------
        # Ingest Into RAG
        # --------------------------------------------------

        ingest_single_document(str(final_path), subject)

        logger.info(f"Uploaded and ingested file: {final_path}")

        return {
            "message": "Document uploaded and indexed successfully",
            "subject": subject,
            "filename": unique_name,
            "size_mb": round(len(contents) / (1024 * 1024), 2)
        }

    except HTTPException:
        raise

    except Exception as e:
        logger.exception("Document ingestion failed")
        raise HTTPException(
            status_code=500,
            detail=f"Document ingestion failed: {str(e)}"
        )