import { Link, useLocation } from "react-router-dom";
import useAuth from "../../hooks/useAuth";

export default function Sidebar() {
  const { isAdmin } = useAuth();
  const location = useLocation();

  const isActive = (path) =>
    location.pathname === path ? "fw-semibold text-dark" : "text-muted";

  return (
    <div className="bg-light p-3 border-end" style={{ width: "220px" }}>
      <h6 className="mb-3">Dashboard</h6>

      <ul className="list-unstyled">

        <li className="mb-2">
          <Link className={isActive("/")} to="/">
            Chat
          </Link>
        </li>

        {isAdmin && (
          <li className="mb-2">
            <Link
              className={isActive("/admin/upload")}
              to="/admin/upload"
            >
              Admin Upload
            </Link>
          </li>
        )}
      </ul>
    </div>
  );
}