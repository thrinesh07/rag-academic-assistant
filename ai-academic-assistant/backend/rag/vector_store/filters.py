# rag/vector_store/filters.py

def filter_by_subject(metadata_list: list[dict], subject: str):
    """
    Filters retrieved metadata by subject.
    """
    return [
        meta for meta in metadata_list
        if meta.get("subject") == subject
    ]