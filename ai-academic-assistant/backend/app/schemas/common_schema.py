from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class BaseResponse(BaseModel):
    success: bool = True


class ErrorResponse(BaseModel):
    success: bool = False
    detail: str


class TimestampMixin(BaseModel):
    timestamp: datetime


class PaginationParams(BaseModel):
    page: int = 1
    page_size: int = 10