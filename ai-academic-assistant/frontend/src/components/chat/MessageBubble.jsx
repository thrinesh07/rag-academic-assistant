import ReactMarkdown from "react-markdown";

export default function MessageBubble({ message }) {

  const isUser = message.role === "user";

  if (isUser) {
    return (
      <div className="mb-3 d-flex justify-content-end">
        <div className="p-3 bg-dark text-white rounded">
          {message.content}
        </div>
      </div>
    );
  }

  return (
    <div className="mb-3 d-flex justify-content-start">

      <div
        className="p-3 bg-light rounded"
        style={{
          maxWidth: "70%",
          lineHeight: "1.7"
        }}
      >

        <ReactMarkdown>
          {message.content}
        </ReactMarkdown>

      </div>

    </div>
  );
}