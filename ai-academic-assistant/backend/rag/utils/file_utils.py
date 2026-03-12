# rag/utils/file_utils.py

from pathlib import Path
import hashlib


MAX_FILE_SIZE_MB = 10


def validate_pdf(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("File not found")

    if path.suffix.lower() != ".pdf":
        raise ValueError("Only PDF files are allowed")

    size_mb = path.stat().st_size / (1024 * 1024)

    if size_mb > MAX_FILE_SIZE_MB:
        raise ValueError("File exceeds size limit")


def compute_sha256(file_path: str) -> str:
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            sha256.update(chunk)

    return sha256.hexdigest()