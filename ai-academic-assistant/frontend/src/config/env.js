// Centralized environment configuration

const requiredEnv = (key) => {
  const value = import.meta.env[key];

  if (!value) {
    throw new Error(`Missing required environment variable: ${key}`);
  }

  return value;
};

export const ENV = {
  API_BASE_URL: requiredEnv("VITE_API_BASE_URL"),
  APP_ENV: import.meta.env.MODE || "development",
  IS_DEV: import.meta.env.DEV,
  IS_PROD: import.meta.env.PROD
};