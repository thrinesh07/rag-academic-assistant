# app/database/session.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


# Production-ready engine config
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,              # max persistent connections
    max_overflow=20,           # extra connections beyond pool_size
    pool_pre_ping=True,        # prevents stale connections
    pool_recycle=1800,         # recycle connections every 30 min
    echo=False                 # set True only for debugging
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


# FastAPI dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()