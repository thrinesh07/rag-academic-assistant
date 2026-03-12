import MessageBubble from "./MessageBubble";
import Loader from "../ui/Loader";
import useAutoScroll from "../../hooks/useAutoScroll";

export default function ChatWindow({ messages = [], loading = false }) {

  const containerRef = useAutoScroll(messages);

  return (
    <div
      ref={containerRef}
      className="chat-window"
      style={{
        flex: 1,
        overflowY: "auto",
        padding: "20px"
      }}
    >

      {messages.length === 0 && (
        <div style={{ textAlign: "center", color: "#888", marginTop: "80px" }}>
          Ask a question to start the conversation.
        </div>
      )}

      {messages.map(msg => (
        <MessageBubble
          key={msg.id}
          message={msg}
        />
      ))}

      {loading && (
        <div style={{ display: "flex", justifyContent: "flex-start" }}>
          <div className="p-3 bg-light rounded">
            <Loader />
          </div>
        </div>
      )}

    </div>
  );
}

