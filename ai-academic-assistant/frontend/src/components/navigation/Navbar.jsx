import { Link, useLocation } from "react-router-dom";
import useAuth from "../../hooks/useAuth";
import UserMenu from "./UserMenu";

export default function Navbar() {
  const { isAuthenticated, isAdmin } = useAuth();
  const location = useLocation();

  if (!isAuthenticated) return null;

  const isActive = (path) =>
    location.pathname === path ? "active fw-semibold" : "";

  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark px-4">
      <Link className="navbar-brand fw-semibold" to="/">
        AI Academic Assistant
      </Link>

      <div className="collapse navbar-collapse show">
        <ul className="navbar-nav me-auto mb-2 mb-lg-0">

          <li className="nav-item">
            <Link
              className={`nav-link ${isActive("/")}`}
              to="/"
            >
              Chat
            </Link>
          </li>

          {isAdmin && (
            <li className="nav-item">
              <Link
                className={`nav-link ${isActive("/admin/upload")}`}
                to="/admin/upload"
              >
                Admin
              </Link>
            </li>
          )}
        </ul>

        <UserMenu />
      </div>
    </nav>
  );
}