# rag/chunking/metadata_builder.py

def build_metadata(base_metadata: dict, chunk_id: int, token_count: int) -> dict:
    """
    Ensures consistent metadata schema for every chunk.
    """

    metadata = base_metadata.copy()

    metadata.update({
        "chunk_id": chunk_id,
        "token_count": token_count
    })

    return metadata