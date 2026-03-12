import { useEffect, useState } from "react";
import { HealthAPI } from "../../api/health.api";

export default function IndexStatusPage() {
  const [status, setStatus] = useState(null);
  const [error, setError] = useState(null);

  const fetchStatus = async () => {
    try {
      const res = await HealthAPI.check();
      setStatus(res.data);
    } catch (err) {
      setError(err.message || "Unable to fetch status.");
    }
  };

  useEffect(() => {
    fetchStatus();
  }, []);

  return (
    <div className="card shadow-sm">
      <div className="card-header bg-white">
        <h6 className="mb-0 fw-semibold">System Status</h6>
      </div>

      <div className="card-body">
        {error && (
          <div className="alert alert-danger py-2">{error}</div>
        )}

        {!status && !error && (
          <div className="text-muted">Loading status...</div>
        )}

        {status && (
          <ul className="list-group">
            <li className="list-group-item">
              API Status: {status.api_status}
            </li>
            <li className="list-group-item">
              RAG Engine: {status.rag_status}
            </li>
            <li className="list-group-item">
              Vector Index Loaded:{" "}
              {status.index_loaded ? "Yes" : "No"}
            </li>
          </ul>
        )}
      </div>
    </div>
  );
}