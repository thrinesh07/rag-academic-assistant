# rag/utils/timers.py

import time
from contextlib import contextmanager


@contextmanager
def timer():
    start = time.time()
    yield lambda: int((time.time() - start) * 1000)