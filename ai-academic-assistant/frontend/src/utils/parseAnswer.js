export default function parseAnswer(text) {

  const result = {
    definition: "",
    explanation: "",
    key_points: [],
    example: "",
    conclusion: ""
  };

  if (!text || typeof text !== "string") {
    return result;
  }

  // Normalize headings so each starts on a new line
  const headings = [
    "Definition",
    "Explanation",
    "Key Points",
    "Example",
    "Conclusion"
  ];

  let normalized = text;

  headings.forEach(h => {
    const regex = new RegExp(`\\s*${h}:`, "gi");
    normalized = normalized.replace(regex, `\n${h}:\n`);
  });

  // Extract section text
  const extract = (name) => {
    const regex = new RegExp(
      `${name}:\\s*([\\s\\S]*?)(?=\\n(?:Definition|Explanation|Key Points|Example|Conclusion):|$)`,
      "i"
    );

    const match = normalized.match(regex);
    return match ? match[1].trim() : "";
  };

  result.definition = extract("Definition");
  result.explanation = extract("Explanation");

  const points = extract("Key Points");

  result.key_points = points
    .split("\n")
    .map(p => p.replace(/^[-•]/, "").trim())
    .filter(Boolean);

  result.example = extract("Example");
  result.conclusion = extract("Conclusion");

  return result;
}