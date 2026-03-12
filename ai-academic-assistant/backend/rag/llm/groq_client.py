# rag/llm/groq_client.py

import time
from typing import Dict, Any
from groq import Groq

from rag.config import GROQ_API_KEY, GROQ_MODEL
from rag.utils.logger import get_logger


logger = get_logger(__name__)


class GroqLLM:

    def __init__(self):
        if not GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not configured")

        self.client = Groq(api_key=GROQ_API_KEY)
        self.model = GROQ_MODEL

    def generate(self, prompt: str) -> Dict[str, Any]:

        start_time = time.time()

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )

        latency = int((time.time() - start_time) * 1000)

        return {
            "text": response.choices[0].message.content,
            "latency_ms": latency
        }