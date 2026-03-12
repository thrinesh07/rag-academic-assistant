# rag/llm/exceptions.py

class LLMError(Exception):
    pass


class RateLimitError(LLMError):
    pass


class InvalidResponseError(LLMError):
    pass