import useAuth from "../../hooks/useAuth";

export default function UserMenu() {
  const { user, logout } = useAuth();

  return (
    <div className="d-flex align-items-center gap-3 text-white">
      <span className="small">
        {user?.email}
      </span>

      <button
        className="btn btn-light btn-sm"
        onClick={logout}
      >
        Logout
      </button>
    </div>
  );
}