import { createContext, useState, useCallback } from "react";
import { ChatAPI } from "../api/chat.api";

export const ChatContext = createContext(null);

export function ChatProvider({ children }) {

  const [messages, setMessages] = useState([]);
  const [subject, setSubject] = useState("OS");
  const [loading, setLoading] = useState(false);

  const sendMessage = useCallback(async (question) => {

    setLoading(true);

    const userMessage = {
      id: Date.now(),
      role: "user",
      content: question
    };

    setMessages(prev => [...prev, userMessage]);

    try {

      const res = await ChatAPI.sendMessage({
        subject,
        question
      });

      const aiMessage = {
        id: Date.now() + 1,
        role: "assistant",
        content: res.data.answer,  // IMPORTANT: raw backend text
        retrieved: res.data.retrieved_chunks || []
      };

      setMessages(prev => [...prev, aiMessage]);

    } catch (error) {

      const errorMessage = {
        id: Date.now() + 2,
        role: "assistant",
        content: "Something went wrong while generating the answer."
      };

      setMessages(prev => [...prev, errorMessage]);

    } finally {
      setLoading(false);
    }

  }, [subject]);

  return (
    <ChatContext.Provider
      value={{
        messages,
        subject,
        setSubject,
        sendMessage,
        loading
      }}
    >
      {children}
    </ChatContext.Provider>
  );
}