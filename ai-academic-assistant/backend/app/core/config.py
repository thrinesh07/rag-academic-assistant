from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    APP_NAME: str = "AI Academic Assistant"
    APP_ENV: str = "development"

    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 15
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    JWT_ALGORITHM: str = "HS256"

    DATABASE_URL: str
    FRONTEND_URL: str

    MAX_UPLOAD_SIZE_MB: int = 10
    LOG_LEVEL: str = "INFO"

    model_config = {
        "env_file": ".env",
        "case_sensitive": True,
        "extra": "ignore"  # ← critical fix
    }


settings = Settings()