from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from uuid import UUID


# -----------------------
# REQUEST MODELS
# -----------------------

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class RefreshResponse(BaseModel):
    access_token: str
    expires_in: int


# -----------------------
# RESPONSE MODELS
# -----------------------

class UserResponse(BaseModel):
    id: UUID
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


class AuthResponse(BaseModel):
    success: bool = True
    user: UserResponse