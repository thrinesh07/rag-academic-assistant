import { useState } from "react";
import { SUBJECTS } from "../../config/constants";
import { UploadAPI } from "../../api/upload.api";

export default function UploadPage() {
  const [file, setFile] = useState(null);
  const [subject, setSubject] = useState("OS");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState(null);
  const [error, setError] = useState(null);

  const validateFile = (file) => {
    if (!file) return "Please select a file.";
    if (file.type !== "application/pdf")
      return "Only PDF files are allowed.";
    if (file.size > 10 * 1024 * 1024)
      return "File must be less than 10MB.";
    return null;
  };

  const handleUpload = async (e) => {
    e.preventDefault();

    setMessage(null);
    setError(null);

    const validationError = validateFile(file);
    if (validationError) {
      setError(validationError);
      return;
    }

    setLoading(true);

    try {
      await UploadAPI.uploadDocument(file, subject);
      setMessage("Document uploaded successfully. Processing started.");
      setFile(null);
      e.target.reset();
    } catch (err) {
      setError(err.message || "Upload failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card shadow-sm">
      <div className="card-header bg-white">
        <h6 className="mb-0 fw-semibold">Upload Academic Document</h6>
      </div>

      <div className="card-body">
        {message && (
          <div className="alert alert-success py-2">{message}</div>
        )}

        {error && (
          <div className="alert alert-danger py-2">{error}</div>
        )}

        <form onSubmit={handleUpload}>
          <div className="mb-3">
            <label className="form-label">Select Subject</label>
            <select
              className="form-select"
              value={subject}
              onChange={(e) => setSubject(e.target.value)}
            >
              {SUBJECTS.map((sub) => (
                <option key={sub.value} value={sub.value}>
                  {sub.label}
                </option>
              ))}
            </select>
          </div>

          <div className="mb-3">
            <label className="form-label">Upload PDF</label>
            <input
              type="file"
              className="form-control"
              accept="application/pdf"
              onChange={(e) => setFile(e.target.files[0])}
            />
          </div>

          <button
            type="submit"
            className="btn btn-dark"
            disabled={loading}
          >
            {loading ? "Uploading..." : "Upload"}
          </button>
        </form>
      </div>
    </div>
  );
}