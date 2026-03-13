from fastapi import Request, HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.core.security import decode_token
from app.models.user import User
from app.core.constants import UserRole


# ==========================================================
# DATABASE DEPENDENCY
# ==========================================================

def get_db_session():
    """
    Wrapper dependency for database session.
    Allows injecting DB into authentication functions.
    """
    return Depends(get_db)


# ==========================================================
# GET CURRENT AUTHENTICATED USER
# ==========================================================

def get_current_user(
    request: Request,
    db: Session = Depends(get_db)
) -> User:
    """
    Extracts JWT token from HTTP-only cookies,
    validates the token,
    fetches the user from database,
    and returns the authenticated user.
    """

    token = request.cookies.get("access_token")

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required"
        )

    try:
        payload = decode_token(token, expected_type="access")
        user_id = payload.get("sub")

        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token"
            )

        user = db.query(User).filter(User.id == user_id).first()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )

        return user

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication failed"
        )


# ==========================================================
# ADMIN AUTHORIZATION
# ==========================================================

def get_admin_user(
    current_user: User = Depends(get_current_user)
) -> User:
    """
    Ensures the authenticated user has admin privileges.
    """

    if current_user.role != UserRole.ADMIN.value:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin privileges required"
        )

    return current_user