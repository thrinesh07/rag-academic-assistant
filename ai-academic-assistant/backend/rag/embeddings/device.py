# rag/embeddings/device.py

import torch


def get_device() -> str:
    """
    Returns 'cuda' if GPU available, else 'cpu'.
    """
    if torch.cuda.is_available():
        return "cuda"
    return "cpu"