import re


def _extract(text: str, section: str) -> str:
    pattern = rf"{section}:(.*?)(?=\n[A-Z][a-zA-Z ]+:|$)"
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else ""


def format_answer(text: str) -> dict:
    definition = _extract(text, "Definition")
    explanation = _extract(text, "Explanation")
    key_points = _extract(text, "Key Points")
    example = _extract(text, "Example")
    conclusion = _extract(text, "Conclusion")

    points = [
        p.strip("- ").strip()
        for p in key_points.split("\n")
        if p.strip()
    ]

    return {
        "definition": definition,
        "explanation": explanation,
        "key_points": points,
        "example": example,
        "conclusion": conclusion,
    }