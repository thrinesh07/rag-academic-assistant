import { useContext } from "react";
import { ChatContext } from "../../context/ChatContext";

import ChatWindow from "../../components/chat/ChatWindow";
import ChatInput from "../../components/chat/ChatInput";

export default function ChatPage() {

  const { messages, loading } = useContext(ChatContext);

  return (
    <div className="chatgpt-layout">

      <ChatWindow
        messages={messages}
        loading={loading}
      />

      <ChatInput />

    </div>
  );
}