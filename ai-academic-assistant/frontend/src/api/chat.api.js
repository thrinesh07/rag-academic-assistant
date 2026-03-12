import api from "./axios";

export const ChatAPI = {
  sendMessage: (payload) =>
    api.post("/chat", {
      subject: payload.subject,
      question: payload.question
    })
};



// // chat.api.js

// export const ChatAPI = {
//   sendMessage: (payload) => api.post("/chat", payload),

//   getHistory: () => api.get("/chat/history"),

//   getChatById: (id) => api.get(`/chat/${id}`)
// };