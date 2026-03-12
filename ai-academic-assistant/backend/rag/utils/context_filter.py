# rag/utils/context_filter.py

def compress_chunks(chunks, max_chars=1500):

    context = ""
    selected = []

    for chunk in chunks:

        text = chunk["text"]

        if len(context) + len(text) > max_chars:
            break

        context += text
        selected.append(chunk)

    return selected