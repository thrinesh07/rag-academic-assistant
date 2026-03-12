import axios from "axios";
import { ENV } from "../config/env";
import { API_PREFIX } from "../config/constants";

const api = axios.create({
  baseURL: `${ENV.API_BASE_URL}${API_PREFIX}`,
  withCredentials: true,
  headers: {
    "Content-Type": "application/json"
  }
});
// import axios from "axios";

// const api = axios.create({
//   baseURL: import.meta.env.VITE_API_BASE_URL,
//   withCredentials: true
// });


// ---- Response Interceptor ----
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Auto refresh token on 401
    if (
      error.response?.status === 401 &&
      !originalRequest._retry &&
      !originalRequest.url.includes("/auth/login")
    ) {
      originalRequest._retry = true;

      try {
        await axios.post(
          `${ENV.API_BASE_URL}${API_PREFIX}/auth/refresh`,
          {},
          { withCredentials: true }
        );

        return api(originalRequest);
      } catch (refreshError) {
        window.location.href = "/login";
      }
    }

    return Promise.reject(formatError(error));
  }
);

// ---- Error Formatter ----
function formatError(error) {
  if (error.response) {
    return {
      status: error.response.status,
      message: error.response.data?.detail || "Request failed"
    };
  }

  if (error.request) {
    return {
      status: 0,
      message: "Network error. Please check your connection."
    };
  }

  return {
    status: 500,
    message: "Unexpected error occurred."
  };
}

export default api;