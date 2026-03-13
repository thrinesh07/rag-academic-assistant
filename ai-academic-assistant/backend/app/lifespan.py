import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database.session import engine
from app.core.logger import configure_logger, logger
from app.integrations.rag_adapter import check_rag_health

# RAG imports
from rag.vector_store.manager import VectorIndex
from rag.embeddings.model import EmbeddingModel


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle manager.

    Handles:
    - Logger initialization
    - Database connectivity check
    - RAG system preload
    - RAG health verification
    - Graceful shutdown
    """

    # ------------------------------------------------
    # STARTUP
    # ------------------------------------------------

    configure_logger()
    logger.info("Starting AI Academic Assistant API...")

    # -----------------------------
    # Database health check
    # -----------------------------

    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        logger.info("Database connection established.")
    except SQLAlchemyError as e:
        logger.critical(f"Database connection failed: {str(e)}")
        raise RuntimeError("Database initialization failed")

    # -----------------------------
    # Preload RAG components
    # -----------------------------

    try:
        logger.info("Preloading RAG components...")

        # Load FAISS index
        vector_store = VectorIndex()
        vector_store._ensure_loaded()

        # Load embedding model
        embedding_model = EmbeddingModel()

        logger.info("Embedding model loaded.")
        logger.info(f"FAISS vectors loaded: {vector_store.size()}")

    except Exception as e:
        logger.warning(f"RAG preload failed: {str(e)}")

    # -----------------------------
    # RAG Health Check
    # -----------------------------

    try:
        rag_status = check_rag_health()

        if rag_status["status"] != "healthy":
            logger.warning("RAG system not fully healthy at startup.")
        else:
            logger.info("RAG system ready.")

    except Exception as e:
        logger.warning(f"RAG health check failed: {str(e)}")

    yield

    # ------------------------------------------------
    # SHUTDOWN
    # ------------------------------------------------

    logger.info("Shutting down AI Academic Assistant API...")

    try:
        engine.dispose()
        logger.info("Database connections closed.")
    except Exception:
        logger.warning("Database cleanup encountered an issue.")