# rag/retrieval/scorer.py

from rag.config import MIN_SIMILARITY_THRESHOLD


def filter_by_score(scores: list[float], metadata: list[dict], top_k: int):
    """
    Adaptive filtering strategy.

    - Keep items above threshold
    - If none pass threshold, fallback to top_k highest
    """

    if not scores:
        return [], []

    filtered_scores = []
    filtered_metadata = []

    for score, meta in zip(scores, metadata):
        if score >= MIN_SIMILARITY_THRESHOLD:
            filtered_scores.append(score)
            filtered_metadata.append(meta)

    # If everything filtered out → fallback to best top_k
    if not filtered_metadata:
        return scores[:top_k], metadata[:top_k]

    return filtered_scores[:top_k], filtered_metadata[:top_k]