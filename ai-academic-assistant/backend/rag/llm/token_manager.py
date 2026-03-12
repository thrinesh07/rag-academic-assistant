# rag/llm/token_manager.py

MAX_INPUT_CHAR_LIMIT = 15000  # soft cap


def trim_prompt(prompt: str) -> str:
    """
    Prevent excessive token usage.
    Character-based soft trimming.
    """

    if len(prompt) > MAX_INPUT_CHAR_LIMIT:
        return prompt[:MAX_INPUT_CHAR_LIMIT]

    return prompt