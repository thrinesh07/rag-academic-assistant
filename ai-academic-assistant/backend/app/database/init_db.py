from app.database.session import engine
from app.database.base import Base
from app.models import user, chat, message, document  # Ensure models load


def init_db():
    Base.metadata.create_all(bind=engine)