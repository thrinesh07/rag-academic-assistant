import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.database.base import Base


class Document(Base):
    __tablename__ = "documents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    subject = Column(String, nullable=False, index=True)

    file_name = Column(String, nullable=False)

    indexed_at = Column(DateTime, default=datetime.utcnow, nullable=False)