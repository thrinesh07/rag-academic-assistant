import json
import re


def default_schema():
    return {
        "definition": [],
        "explanation": [],
        "key_points": [],
        "example": "",
        "conclusion": ""
    }


def extract_json(text: str):

    if not text:
        return default_schema()

    # try parsing normal JSON
    try:
        return json.loads(text)
    except Exception:
        pass

    sections = default_schema()

    # split using headings
    parts = re.split(
        r"(Definition|Explanation|Key Points|Example|Conclusion)",
        text
    )

    for i in range(1, len(parts), 2):

        name = parts[i].lower().replace(" ", "_")
        content = parts[i + 1]

        items = [
            x.strip(" ,•")
            for x in re.split(r",|\n|•", content)
            if x.strip()
        ]

        if name in ["definition", "explanation", "key_points"]:
            sections[name] = items

        elif name == "example":
            sections["example"] = " ".join(items)

        elif name == "conclusion":
            sections["conclusion"] = " ".join(items)

    return sections