# scripts/ingest_all.py

from rag.services import ingest_all_documents
from rag.config import validate_config


def main():
    validate_config()
    print("Starting batch ingestion...")
    ingest_all_documents()
    print("Ingestion completed.")


if __name__ == "__main__":
    main()