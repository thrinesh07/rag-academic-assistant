# rag/ingestion/document_hash.py

import hashlib


def compute_file_hash(file_path: str) -> str:
    """
    Computes SHA256 hash of file.
    Used to prevent duplicate indexing.
    """
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()