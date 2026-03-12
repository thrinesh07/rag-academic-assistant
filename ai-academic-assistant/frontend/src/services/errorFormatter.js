export function formatApiError(error) {
  if (!error) {
    return "Unexpected error occurred.";
  }

  if (typeof error === "string") {
    return error;
  }

  if (error.message) {
    return error.message;
  }

  if (error.detail) {
    return error.detail;
  }

  return "Something went wrong. Please try again.";
}