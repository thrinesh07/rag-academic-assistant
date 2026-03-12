from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.models.user import User
from app.core.security import hash_password
from app.core.constants import UserRole


def create_admin():
    db: Session = SessionLocal()

    admin_email = "admin@aiassistant.com"

    existing = db.query(User).filter(User.email == admin_email).first()
    if existing:
        print("Admin already exists")
        return

    admin = User(
        email=admin_email,
        hashed_password=hash_password("admin123"),
        role=UserRole.ADMIN
    )

    db.add(admin)
    db.commit()
    print("Admin created successfully")