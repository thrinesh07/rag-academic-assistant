import api from "./axios";

export const AuthAPI = {
  register: (data) => api.post("/auth/register", data),

  login: (data) => api.post("/auth/login", data),

  refresh: () => api.post("/auth/refresh"),

  logout: () => api.post("/auth/logout"),

  getCurrentUser: () => api.get("/auth/me")
};