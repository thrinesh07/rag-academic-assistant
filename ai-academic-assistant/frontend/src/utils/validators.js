export function isValidEmail(email) {
  const pattern =
    /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return pattern.test(email);
}

export function isStrongPassword(password) {
  return password.length >= 6;
}

export function validatePDF(file, maxSizeMB = 10) {
  if (!file) return "File is required.";

  if (file.type !== "application/pdf")
    return "Only PDF files are allowed.";

  if (file.size > maxSizeMB * 1024 * 1024)
    return `File must be under ${maxSizeMB}MB.`;

  return null;
}