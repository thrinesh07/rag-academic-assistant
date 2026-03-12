# rag/embeddings/batching.py

from typing import List


def batch_iterator(items: List[str], batch_size: int):
    """
    Yields batches to control memory usage.
    """

    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]