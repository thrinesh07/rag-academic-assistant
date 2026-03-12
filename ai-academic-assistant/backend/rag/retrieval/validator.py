# rag/retrieval/validator.py

def validate_query(query: str):
    if not query or len(query.strip()) < 3:
        raise ValueError("Query too short.")