from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, Response, status, Request
import hashlib

from app.models.user import User
from app.models.refresh_token import RefreshToken
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    create_refresh_token,
    set_auth_cookies,
    clear_auth_cookies,
)
from app.core.config import settings
from app.core.logger import logger


# ==========================================================
# REGISTER
# ==========================================================

def register_user(request: RegisterRequest, response: Response, db: Session):

    existing = db.query(User).filter(User.email == request.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=request.email,
        hashed_password=hash_password(request.password),
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))

    # Remove any existing refresh tokens for safety
    invalidate_user_refresh_tokens(db, user.id)

    store_refresh_token(db, user.id, refresh_token)

    set_auth_cookies(response, access_token, refresh_token)

    logger.info(f"User registered: {user.email}")

    return {"success": True, "user": user}


# ==========================================================
# LOGIN
# ==========================================================

def login_user(request: LoginRequest, response: Response, db: Session):

    user = db.query(User).filter(User.email == request.email).first()

    if not user or not verify_password(request.password, user.hashed_password):
        logger.warning(f"Failed login attempt: {request.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(str(user.id))
    refresh_token = create_refresh_token(str(user.id))

    # Invalidate old refresh tokens
    invalidate_user_refresh_tokens(db, user.id)

    store_refresh_token(db, user.id, refresh_token)

    set_auth_cookies(response, access_token, refresh_token)

    logger.info(f"User login: {user.email}")

    return {"success": True, "user": user}


# ==========================================================
# REFRESH TOKEN ROTATION
# ==========================================================

def refresh_access_token(request: Request, response: Response, db: Session):

    refresh_token = request.cookies.get("refresh_token")

    if not refresh_token:
        raise HTTPException(status_code=401, detail="Missing refresh token")

    hashed = hash_refresh_token(refresh_token)

    stored = db.query(RefreshToken).filter(
        RefreshToken.token_hash == hashed
    ).first()

    if not stored or stored.expires_at < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    user_id = stored.user_id

    # ROTATION: remove old token
    db.delete(stored)
    db.commit()

    # Issue new tokens
    new_access = create_access_token(str(user_id))
    new_refresh = create_refresh_token(str(user_id))

    store_refresh_token(db, user_id, new_refresh)

    set_auth_cookies(response, new_access, new_refresh)

    logger.info(f"Refresh token rotated for user {user_id}")

    return {"success": True}


# ==========================================================
# LOGOUT
# ==========================================================

def logout_user(request: Request, response: Response, db: Session):

    refresh_token = request.cookies.get("refresh_token")

    if refresh_token:
        hashed = hash_refresh_token(refresh_token)
        db.query(RefreshToken).filter(
            RefreshToken.token_hash == hashed
        ).delete()
        db.commit()

    clear_auth_cookies(response)

    logger.info("User logged out")

    return {"success": True}


# ==========================================================
# HELPER METHODS
# ==========================================================

def store_refresh_token(db: Session, user_id, refresh_token: str):

    hashed = hash_refresh_token(refresh_token)

    expires_at = datetime.utcnow() + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    token_entry = RefreshToken(
        user_id=user_id,
        token_hash=hashed,
        expires_at=expires_at
    )

    db.add(token_entry)
    db.commit()


def invalidate_user_refresh_tokens(db: Session, user_id):
    """
    Ensures only one active refresh token per user.
    """
    db.query(RefreshToken).filter(
        RefreshToken.user_id == user_id
    ).delete()
    db.commit()


def hash_refresh_token(token: str) -> str:
    """
    Refresh tokens are already high-entropy JWTs.
    We hash them with SHA256 for safe storage.
    """
    return hashlib.sha256(token.encode()).hexdigest()