import api from "./axios";

export const UploadAPI = {
  uploadDocument: (file, subject) => {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("subject", subject);

    return api.post("/upload", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  }
};