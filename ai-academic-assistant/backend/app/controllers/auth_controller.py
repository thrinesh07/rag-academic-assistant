from fastapi import Response, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth_schema import RegisterRequest, LoginRequest
from app.services.auth_service import (
    create_user,
    authenticate_user,
    generate_tokens_from_refresh
)
from app.core.security import set_auth_cookies, clear_auth_cookies
from app.core.logger import logger


def register_user(payload: RegisterRequest, db: Session):
    user = create_user(db, payload.email, payload.password)

    logger.info(f"New user registered: {user.email}")

    return {
        "message": "User registered successfully",
        "user": user
    }


def login_user(payload: LoginRequest, response: Response, db: Session):
    user = authenticate_user(db, payload.email, payload.password)

    if not user:
        logger.warning(f"Failed login attempt: {payload.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token, refresh_token = user["tokens"]

    set_auth_cookies(response, access_token, refresh_token)

    logger.info(f"User logged in: {payload.email}")

    return {
        "message": "Login successful",
        "user": user["user"]
    }


def refresh_access_token(response: Response, db: Session):
    access_token = generate_tokens_from_refresh(db, response)

    logger.info("Access token refreshed")

    return {
        "message": "Token refreshed"
    }


def logout_user(response: Response):
    clear_auth_cookies(response)

    logger.info("User logged out")

    return {
        "message": "Logged out successfully"
    }