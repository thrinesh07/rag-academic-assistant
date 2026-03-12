import api from "./axios";

export const HealthAPI = {
  check: () => api.get("/health")
};