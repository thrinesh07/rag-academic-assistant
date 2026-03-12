from pydantic import BaseModel
from uuid import UUID
from datetime import datetime


class UploadResponse(BaseModel):
    success: bool = True
    document_id: UUID
    subject: str
    indexed_at: datetime