# rag/llm/response_parser.py
import markdown
from rag.llm.exceptions import InvalidResponseError


def parse_groq_response(response) -> str:
    """
    Extracts content safely from Groq API response.
    """

    try:
        content = response.choices[0].message.content
        if not content:
            raise InvalidResponseError("Empty response from LLM")

        return content.strip()

    except Exception as e:
        raise InvalidResponseError(f"Invalid LLM response format: {str(e)}")