import re

SECTIONS = [
    "Definition",
    "Explanation",
    "Key Points",
    "Example",
    "Conclusion"
]


def normalize_headings(text: str) -> str:
    """
    Convert many heading styles into a consistent 'Section:' form.
    Handles:
    - 'Definition ...'
    - '## Definition'
    - '**Definition**'
    - 'Definition -'
    """
    for section in SECTIONS:
        # Markdown heading
        text = re.sub(rf"#+\s*{section}", f"{section}:", text, flags=re.IGNORECASE)

        # Bold heading
        text = re.sub(rf"\*\*{section}\*\*", f"{section}:", text, flags=re.IGNORECASE)

        # Dash heading
        text = re.sub(rf"{section}\s*-", f"{section}:", text, flags=re.IGNORECASE)

        # Plain heading without colon
        text = re.sub(rf"\b{section}\b\s+", f"{section}: ", text, flags=re.IGNORECASE)

    return text


def extract_section(text: str, section: str, next_section: str | None):
    if next_section:
        pattern = rf"{section}:(.*?)(?={next_section}:)"
    else:
        pattern = rf"{section}:(.*)"

    match = re.search(pattern, text, re.S | re.IGNORECASE)
    if not match:
        return ""

    return match.group(1).strip()


def format_keypoints(text: str):
    """
    Ensure bullet formatting is consistent.
    """
    lines = re.split(r'\n|- ', text)

    points = []
    for line in lines:
        line = line.strip()
        if not line:
            continue

        # remove any existing bullets
        line = re.sub(r'^[•\-\*\s]+', '', line)

        points.append(f"• {line}")

    return "\n".join(points)


def build_block(title: str, content: str):
    if not content:
        return ""

    return f"{title}\n\n{content}\n\n"


def format_structured_answer(raw_text: str):

    text = normalize_headings(raw_text)

    sections = {}

    for i, section in enumerate(SECTIONS):
        next_section = SECTIONS[i + 1] if i + 1 < len(SECTIONS) else None
        sections[section] = extract_section(text, section, next_section)

    output = ""

    output += build_block("Definition", sections["Definition"])
    output += build_block("Explanation", sections["Explanation"])

    if sections["Key Points"]:
        points = format_keypoints(sections["Key Points"])
        output += build_block("Key Points", points)

    output += build_block("Example", sections["Example"])
    output += build_block("Conclusion", sections["Conclusion"])

    return output.strip()