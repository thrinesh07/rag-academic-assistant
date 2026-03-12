# scripts/reset_index.py

import shutil
from rag.config import INDEX_DIR


def main():
    shutil.rmtree(INDEX_DIR, ignore_errors=True)
    print("Index store deleted.")


if __name__ == "__main__":
    main()