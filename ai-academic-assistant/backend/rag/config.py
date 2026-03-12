# rag/config.py

import os
from pathlib import Path
from dotenv import load_dotenv

# --------------------------------------------------
# Load environment variables
# --------------------------------------------------

load_dotenv()

# --------------------------------------------------
# Project Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INDEX_DIR = BASE_DIR / "rag" / "index_store"

INDEX_DIR.mkdir(parents=True, exist_ok=True)

# --------------------------------------------------
# Environment
# --------------------------------------------------

ENV = os.getenv("ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# --------------------------------------------------
# LLM Configuration
# --------------------------------------------------

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama3-70b-8192")

MAX_TOKENS_LLM = int(os.getenv("MAX_TOKENS_LLM", 1500))
LLM_TEMPERATURE = float(os.getenv("LLM_TEMPERATURE", 0.2))

# --------------------------------------------------
# Embedding Configuration
# --------------------------------------------------

EMBEDDING_MODEL_NAME = os.getenv(
    "EMBEDDING_MODEL_NAME",
    "sentence-transformers/all-MiniLM-L6-v2"
)

EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", 384))
EMBEDDING_BATCH_SIZE = int(os.getenv("EMBEDDING_BATCH_SIZE", 16))

# --------------------------------------------------
# Chunking Configuration
# --------------------------------------------------

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 450))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))

# --------------------------------------------------
# Retrieval Configuration
# --------------------------------------------------

TOP_K_DEFAULT = int(os.getenv("TOP_K_DEFAULT", 3))
MIN_SIMILARITY_THRESHOLD = float(
    os.getenv("MIN_SIMILARITY_THRESHOLD", 0.25)
)

# --------------------------------------------------
# Vector Store Paths
# --------------------------------------------------

FAISS_INDEX_PATH = Path(
    os.getenv(
        "FAISS_INDEX_PATH",
        INDEX_DIR / "faiss.index"
    )
)

METADATA_PATH = Path(
    os.getenv(
        "METADATA_PATH",
        INDEX_DIR / "metadata.pkl"
    )
)

DOC_REGISTRY_PATH = Path(
    os.getenv(
        "DOC_REGISTRY_PATH",
        INDEX_DIR / "document_registry.pkl"
    )
)

# --------------------------------------------------
# File Limits
# --------------------------------------------------

MAX_FILE_SIZE_MB = int(os.getenv("MAX_FILE_SIZE_MB", 10))
ALLOWED_EXTENSIONS = os.getenv("ALLOWED_EXTENSIONS", ".pdf").split(",")

# --------------------------------------------------
# Validation
# --------------------------------------------------

def validate_config():
    """
    Validates critical runtime configuration.
    """

    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is not set")

    if CHUNK_OVERLAP >= CHUNK_SIZE:
        raise ValueError("CHUNK_OVERLAP must be smaller than CHUNK_SIZE")

    if EMBEDDING_DIM <= 0:
        raise ValueError("Invalid EMBEDDING_DIM")

    return True