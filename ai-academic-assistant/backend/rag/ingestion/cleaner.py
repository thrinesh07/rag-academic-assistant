# rag/ingestion/cleaner.py

import re


class TextCleaner:
    """
    Cleans and normalizes extracted text.
    """

    @staticmethod
    def clean(text: str) -> str:
        if not text:
            return ""

        text = text.encode("utf-8", "ignore").decode("utf-8")
        text = re.sub(r'\s+', ' ', text)
        text = text.strip()

        return text