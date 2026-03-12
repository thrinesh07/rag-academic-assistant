# scripts/ingest_single.py

import sys
from rag.services import ingest_single_document
from rag.config import validate_config
from rag.constants import SUPPORTED_SUBJECTS


def main():
    if len(sys.argv) != 3:
        print("Usage: python ingest_single.py <file_path> <subject>")
        sys.exit(1)

    file_path = sys.argv[1]
    subject = sys.argv[2]

    if subject not in SUPPORTED_SUBJECTS:
        print("Invalid subject.")
        sys.exit(1)

    validate_config()

    ingest_single_document(file_path, subject)
    print("Single document ingestion complete.")


if __name__ == "__main__":
    main()