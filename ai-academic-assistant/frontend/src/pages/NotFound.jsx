import { Link } from "react-router-dom";
import useAuth from "../hooks/useAuth";

export default function NotFound() {
  const { isAuthenticated } = useAuth();

  return (
    <div className="d-flex flex-column justify-content-center align-items-center text-center py-5">
      <h1 className="display-4 fw-bold">404</h1>
      <p className="text-muted mb-3">
        The page you’re looking for doesn’t exist.
      </p>

      <Link
        to={isAuthenticated ? "/" : "/login"}
        className="btn btn-dark"
      >
        Go Back Home
      </Link>
    </div>
  );
}