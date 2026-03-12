import { useState, useContext } from "react";
import { ChatContext } from "../../context/ChatContext";

export default function ChatInput() {

  const [text, setText] = useState("");
  const { sendMessage } = useContext(ChatContext);

  const handleSubmit = async (e) => {

    e.preventDefault();

    if (!text.trim()) return;

    const message = text;

    setText("");

    await sendMessage(message);
  };

  return (
    <form onSubmit={handleSubmit} className="chatgpt-input-wrapper">

      <div className="chatgpt-input-container">

        <input
          type="text"
          placeholder="Ask anything..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <button type="submit">
          Send
        </button>

      </div>

    </form>
  );
}