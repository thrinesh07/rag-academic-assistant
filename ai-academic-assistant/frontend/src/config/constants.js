// Subjects mirrored from backend constants.py

export const SUBJECTS = Object.freeze([
  { label: "Operating Systems", value: "OS" },
  { label: "Database Management Systems", value: "DBMS" },
  { label: "Computer Networks", value: "CN" },
  { label: "Data Structures & Algorithms", value: "DSA" },
  { label: "Object Oriented Programming", value: "OOPS" }
]);

// Roles mirrored from backend roles enum

export const ROLES = Object.freeze({
  ADMIN: "admin",
  STUDENT: "student"
});

// Default app settings

export const DEFAULTS = Object.freeze({
  DEFAULT_SUBJECT: "OS",
  CHAT_LIMIT: 50
});

// API version prefix (must match backend router prefix)

export const API_PREFIX = "/api/v1";