# rag/services/rag_service.py

import time
from typing import Dict, Any, List

from rag.retrieval.retriever import RetrievalService
from rag.prompts.academic_prompt import AcademicPromptBuilder
from rag.llm.groq_client import GroqLLM
from rag.utils.structured_formatter import format_structured_answer
from rag.constants import NOT_ENOUGH_INFO_RESPONSE
from rag.utils.logger import get_logger


logger = get_logger(__name__)


class RAGService:
    """
    Main orchestration service for the RAG pipeline.

    Pipeline steps:
    1. Retrieve relevant context chunks
    2. Build structured prompt
    3. Call LLM
    4. Format response
    5. Return structured output
    """

    def __init__(self):

        self.retriever = RetrievalService()
        self.prompt_builder = AcademicPromptBuilder()
        self.llm = GroqLLM()

    # ---------------------------------------------------------

    def _compress_context(self, chunks: List[dict], max_chars: int = 2000):
        """
        Prevent extremely long prompts.
        Keeps most relevant chunks until limit reached.
        """

        total = 0
        filtered = []

        for chunk in chunks:

            text = chunk.get("text", "")

            if not text:
                continue

            length = len(text)

            if total + length > max_chars:
                break

            filtered.append(chunk)
            total += length

        return filtered

    # ---------------------------------------------------------

    def generate_answer(
        self,
        query: str,
        subject: str,
        top_k: int = 3
    ) -> Dict[str, Any]:

        total_start = time.time()

        try:

            # -------------------------------------------------
            # RETRIEVAL
            # -------------------------------------------------

            retrieval_result = self.retriever.retrieve_context(
                query=query,
                subject=subject,
                top_k=top_k
            )

            chunks = retrieval_result.get("chunks", [])
            similarity_scores = retrieval_result.get("scores", [])
            retrieval_latency = retrieval_result.get("latency_ms", 0)

            logger.info(
                f"Retrieval | subject={subject} | chunks={len(chunks)} | latency={retrieval_latency}ms"
            )

            if not chunks:

                return {
                    "answer": NOT_ENOUGH_INFO_RESPONSE,
                    "retrieved_chunks": [],
                    "similarity_scores": [],
                    "subject": subject,
                    "retrieval_latency_ms": retrieval_latency,
                    "llm_latency_ms": 0,
                    "latency_ms": int((time.time() - total_start) * 1000)
                }

            # -------------------------------------------------
            # CONTEXT COMPRESSION
            # -------------------------------------------------

            chunks = self._compress_context(chunks)

            # -------------------------------------------------
            # PROMPT BUILDING
            # -------------------------------------------------

            prompt = self.prompt_builder.build(
                query=query,
                retrieved_chunks=chunks
            )

            # -------------------------------------------------
            # LLM GENERATION
            # -------------------------------------------------

            llm_result = self.llm.generate(prompt)

            raw_output = llm_result.get("text", "")
            llm_latency = llm_result.get("latency_ms", 0)

            logger.debug(f"LLM RAW OUTPUT:\n{raw_output}")


            if not raw_output:
                raw_output = NOT_ENOUGH_INFO_RESPONSE

            # -------------------------------------------------
            # STRUCTURED FORMATTING
            # -------------------------------------------------

            formatted_answer = format_structured_answer(raw_output)

            total_latency = int((time.time() - total_start) * 1000)

            # -------------------------------------------------
            # FINAL RESPONSE
            # -------------------------------------------------

            return {
                "answer": formatted_answer,
                "retrieved_chunks": chunks,
                "similarity_scores": similarity_scores,
                "subject": subject,
                "retrieval_latency_ms": retrieval_latency,
                "llm_latency_ms": llm_latency,
                "latency_ms": total_latency
            }

        except Exception as e:

            logger.exception("RAG generation failed")

            return {
                "answer": "Internal system error.",
                "retrieved_chunks": [],
                "similarity_scores": [],
                "subject": subject,
                "retrieval_latency_ms": 0,
                "llm_latency_ms": 0,
                "latency_ms": int((time.time() - total_start) * 1000),
                "error": str(e)
            }


# ---------------------------------------------------------
# SINGLETON INSTANCE
# ---------------------------------------------------------

_rag_service_instance = RAGService()


def generate_answer(
    query: str,
    subject: str,
    top_k: int = 3
) -> Dict[str, Any]:

    return _rag_service_instance.generate_answer(query, subject, top_k)