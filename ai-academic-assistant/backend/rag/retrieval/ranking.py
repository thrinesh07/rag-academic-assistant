# rag/retrieval/ranking.py

def rank_by_score(scores: list[float], metadata: list[dict]):
    """
    Sorts results by similarity score descending.
    """

    combined = list(zip(scores, metadata))
    combined.sort(key=lambda x: x[0], reverse=True)

    sorted_scores = [item[0] for item in combined]
    sorted_metadata = [item[1] for item in combined]

    return sorted_scores, sorted_metadata