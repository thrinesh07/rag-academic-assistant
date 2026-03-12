import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database.session import engine
from app.core.logger import configure_logger, logger
from app.integrations.rag_adapter import check_rag_health


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle manager.

    Handles:
    - Logger initialization
    - Database connectivity check
    - RAG health verification
    - Graceful shutdown logging
    """

    # ----------------------------
    # STARTUP PHASE
    # ----------------------------

    configure_logger()
    logger.info("Starting AI Academic Assistant API...")

    # DB Health Check
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection established.")
    except SQLAlchemyError as e:
        logger.critical(f"Database connection failed: {str(e)}")
        raise RuntimeError("Database initialization failed")

    # RAG Health Check (non-blocking safe check)
    try:
        rag_status = check_rag_health()
        if rag_status["status"] != "healthy":
            logger.warning("RAG system not fully healthy at startup.")
        else:
            logger.info("RAG system ready.")
    except Exception as e:
        logger.warning(f"RAG health check failed: {str(e)}")

    yield

    # ----------------------------
    # SHUTDOWN PHASE
    # ----------------------------

    logger.info("Shutting down AI Academic Assistant API...")

    try:
        engine.dispose()
        logger.info("Database connections closed.")
    except Exception:
        logger.warning("Database cleanup encountered an issue.")