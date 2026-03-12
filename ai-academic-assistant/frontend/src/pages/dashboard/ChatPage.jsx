import useChat from "../../hooks/useChat";
import useAutoScroll from "../../hooks/useAutoScroll";
import { SUBJECTS } from "../../config/constants";

export default function ChatPage() {
  const {
    messages,
    subject,
    setSubject,
    sendMessage,
    loading
  } = useChat();

  const containerRef = useAutoScroll(messages);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const form = e.target;
    const question = form.question.value.trim();

    if (!question) return;

    await sendMessage(question);
    form.reset();
  };

  return (
    <div className="card shadow-sm">
      {/* Header */}
      <div className="card-header bg-white d-flex justify-content-between align-items-center">
        <h6 className="mb-0 fw-semibold">Ask a Question</h6>

        <select
          className="form-select w-auto"
          value={subject}
          onChange={(e) => setSubject(e.target.value)}
        >
          {SUBJECTS.map((sub) => (
            <option key={sub.value} value={sub.value}>
              {sub.label}
            </option>
          ))}
        </select>
      </div>

      {/* Chat Window */}
      <div
        ref={containerRef}
        className="card-body"
        style={{ height: "60vh", overflowY: "auto" }}
      >
        {messages.length === 0 && (
          <div className="text-center text-muted mt-5">
            Start by asking a question.
          </div>
        )}

        {messages.map((msg, index) => (
          <div
            key={index}
            className={`mb-3 d-flex ${
              msg.role === "user"
                ? "justify-content-end"
                : "justify-content-start"
            }`}
          >
            <div
              className={`p-3 rounded ${
                msg.role === "user"
                  ? "bg-dark text-white"
                  : "bg-light"
              }`}
              style={{ maxWidth: "70%" }}
            >
              <div>{msg.content}</div>

              {/* Retrieved context section */}
              {msg.role === "assistant" &&
                msg.retrieved &&
                msg.retrieved.length > 0 && (
                  <details className="mt-2">
                    <summary className="small text-muted">
                      View retrieved context
                    </summary>
                    <ul className="small mt-2">
                      {msg.retrieved.map((chunk, i) => (
                        <li key={i}>
                          {chunk.text?.slice(0, 120)}...
                        </li>
                      ))}
                    </ul>
                  </details>
                )}
            </div>
          </div>
        ))}

        {loading && (
          <div className="text-muted small">
            AI is thinking...
          </div>
        )}
      </div>

      {/* Input */}
      <div className="card-footer bg-white">
        <form onSubmit={handleSubmit} className="input-group">
          <input
            type="text"
            name="question"
            className="form-control"
            placeholder="Ask something..."
            autoComplete="off"
          />
          <button className="btn btn-dark" disabled={loading}>
            Send
          </button>
        </form>
      </div>
    </div>
  );
}