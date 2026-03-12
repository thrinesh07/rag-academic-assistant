# scripts/reindex.py

import shutil
from rag.config import INDEX_DIR
from rag.services import ingest_all_documents


def main():
    print("Deleting existing index store...")

    shutil.rmtree(INDEX_DIR, ignore_errors=True)

    print("Rebuilding index from scratch...")
    ingest_all_documents()

    print("Reindex complete.")


if __name__ == "__main__":
    main()