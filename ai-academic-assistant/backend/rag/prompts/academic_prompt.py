# rag/prompts/academic_prompt.py


from rag.prompts.guardrails import SYSTEM_INSTRUCTION
from rag.constants import NOT_ENOUGH_INFO_RESPONSE


class AcademicPromptBuilder:
    """
    Builds structured academic prompts for the LLM.
    """

    def build(self, query: str, retrieved_chunks: list[dict]) -> str:

        context_blocks = []

        for i, chunk in enumerate(retrieved_chunks, start=1):

            context_blocks.append(
                f"[Context {i}]\n{chunk['text']}\n"
            )

        context_text = "\n".join(context_blocks)

        prompt = f"""
{SYSTEM_INSTRUCTION}

You are a university-level academic assistant.

Write a structured answer.

Use EXACT format:

Definition:
(2–3 sentences)

Explanation:
(clear technical explanation)

Key Points:
- bullet points only
- concise and exam oriented

Example:
(simple real world example)

Conclusion:
(short conceptual summary)

STRICT RULES:
- Use the exact headings:
Definition:
Explanation:
Key Points:
Example:
Conclusion:
- Do NOT use markdown
- Do NOT invent information
- If context is insufficient return exactly:
{NOT_ENOUGH_INFO_RESPONSE}

CONTEXT:
{context_text}

QUESTION:
{query}
"""

        return prompt.strip()