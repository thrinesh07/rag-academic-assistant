# import time
# from app.core.logger import logger
# from app.core.exceptions import RAGServiceError
# from rag.services.rag_service import generate_answer  # External module


# def call_rag(question: str, subject: str):

#     start = time.time()

#     try:
#         result = generate_answer(question, subject)
#         latency = time.time() - start

#         logger.info(f"RAG latency: {latency:.2f}s")

#         return {
#             "answer": result.get("answer"),
#             "retrieved_chunks": result.get("chunks", []),
#             "latency": latency
#         }

#     except Exception as e:
#         logger.error(f"RAG failure: {str(e)}")
#         raise RAGServiceError("Failed to generate response")