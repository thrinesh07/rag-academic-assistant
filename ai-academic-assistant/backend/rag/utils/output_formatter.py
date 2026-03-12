import re


HEADINGS = [
    "Definition",
    "Explanation",
    "Key Points",
    "Example",
    "Conclusion"
]


def format_output(text: str) -> str:
    """
    Normalize LLM output into structured sections.
    """

    if not text:
        return ""

    # remove markdown artifacts
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"#", "", text)

    # ensure headings start on new line
    for heading in HEADINGS:
        text = re.sub(rf"\s*{heading}\s*", f"\n\n{heading}:\n", text)

    # replace comma separators with new lines
    text = text.replace(".,", ".\n")
    text = text.replace(",", "\n")

    # normalize bullet points
    text = text.replace("•", "\n•")

    lines = []

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue

        # keep headings
        if any(line.startswith(h) for h in HEADINGS):
            lines.append(line)
            continue

        # keep bullets
        if line.startswith("•"):
            lines.append(line)
            continue

        # convert sentence into bullet
        lines.append(f"• {line}")

    return "\n".join(lines)