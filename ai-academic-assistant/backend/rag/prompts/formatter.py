# rag/prompts/formatter.py

import re


def clean_context(text: str) -> str:

    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"#+\s*", "", text)
    text = re.sub(r"References.*", "", text, flags=re.DOTALL)
    text = re.sub(r"\[Source.*?\]", "", text)
    text = re.sub(r"\n\s*\n", "\n\n", text)

    return text.strip()


# rag/prompts/formatter.py

def format_context(chunks: list[dict]) -> str:

    context = []

    for i, chunk in enumerate(chunks):
        block = f"""
[Document {i+1}]
Source: {chunk.get("source")}
Page: {chunk.get("page")}

{chunk.get("text")}
"""
        context.append(block.strip())

    return "\n\n".join(context)