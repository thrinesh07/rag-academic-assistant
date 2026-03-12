import re


SECTIONS = [
    "Definition",
    "Explanation",
    "Key Points",
    "Example",
    "Conclusion"
]


def format_answer(text: str) -> str:
    """
    Normalize LLM output so sections and bullets render correctly
    in the frontend.
    """

    if not text:
        return ""

    # remove markdown symbols
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"#+", "", text)

    # force section breaks
    for sec in SECTIONS:
        text = re.sub(rf"\s*{sec}\s*", f"\n\n{sec}\n", text)

    # normalize bullet points
    text = text.replace("•", "\n•")

    # split sentences separated by commas
    text = re.sub(r",\s*", "\n", text)

    lines = []
    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue

        # keep section titles
        if line in SECTIONS:
            lines.append(f"\n{line}")
            continue

        # keep bullets
        if line.startswith("•"):
            lines.append(line)
            continue

        # convert sentences to bullets
        lines.append(f"• {line}")

    return "\n".join(lines)