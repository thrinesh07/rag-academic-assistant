from fastapi import APIRouter, Depends, Response, Request
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth_schema import RegisterRequest, LoginRequest, AuthResponse
from app.services.auth_service import (
    register_user,
    login_user,
    refresh_access_token,
    logout_user
)

from app.middleware.auth_middleware import get_current_user
from app.models.user import User


router = APIRouter(prefix="/auth", tags=["Auth"])


# ----------------------------------------
# REGISTER
# ----------------------------------------

@router.post("/register", response_model=AuthResponse)
def register(
    request: RegisterRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    return register_user(request, response, db)


# ----------------------------------------
# LOGIN
# ----------------------------------------

@router.post("/login", response_model=AuthResponse)
def login(
    request: LoginRequest,
    response: Response,
    db: Session = Depends(get_db)
):
    return login_user(request, response, db)


# ----------------------------------------
# REFRESH TOKEN
# ----------------------------------------

@router.post("/refresh")
def refresh(
    request: Request,
    response: Response,
    db: Session = Depends(get_db)
):
    return refresh_access_token(request, response, db)


# ----------------------------------------
# LOGOUT
# ----------------------------------------

@router.post("/logout")
def logout(
    request: Request,
    response: Response,
    db: Session = Depends(get_db)
):
    return logout_user(request, response, db)


# ----------------------------------------
# CURRENT USER
# ----------------------------------------

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):

    return {
        "id": current_user.id,
        "email": current_user.email,
        "created_at": current_user.created_at
    }