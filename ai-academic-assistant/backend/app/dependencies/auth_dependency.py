from fastapi import Request, HTTPException, Depends
from sqlalchemy.orm import Session
from app.dependencies.db_dependency import get_db
from app.core.security import decode_token
from app.repositories.user_repository import UserRepository


def get_current_user_id(request: Request) -> str:
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = decode_token(token, expected_type="access")
    return payload["sub"]


def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
):
    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")

    payload = decode_token(token, expected_type="access")
    user_id = payload["sub"]

    user = UserRepository.get_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user