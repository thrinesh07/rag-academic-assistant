# rag/chunking/validation.py

def validate_text(text: str) -> bool:
    """
    Filters invalid or meaningless text before chunking.
    """

    if not text:
        return False

    if len(text.strip()) < 20:
        return False

    return True