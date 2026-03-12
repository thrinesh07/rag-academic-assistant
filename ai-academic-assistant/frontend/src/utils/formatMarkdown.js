// export function formatMarkdown(data) {
//   if (!data) return "";

//   let md = "";

//   if (data.definition) {
//     md += `## Definition\n\n${data.definition}\n\n`;
//   }

//   if (data.explanation) {
//     md += `## Explanation\n\n${data.explanation}\n\n`;
//   }

//   if (data.key_points && data.key_points.length > 0) {
//     md += `## Key Points\n\n`;
//     data.key_points.forEach(point => {
//       md += `- ${point}\n`;
//     });
//     md += `\n`;
//   }

//   if (data.example) {
//     md += `## Example\n\n${data.example}\n\n`;
//   }

//   if (data.conclusion) {
//     md += `## Conclusion\n\n${data.conclusion}\n\n`;
//   }

//   return md.trim();
// }