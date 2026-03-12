import useAuth from "../../hooks/useAuth";

export default function ProfilePage() {
  const { user } = useAuth();

  return (
    <div className="card shadow-sm">
      <div className="card-header bg-white">
        <h6 className="mb-0 fw-semibold">Profile</h6>
      </div>

      <div className="card-body">
        <p>
          <strong>Email:</strong> {user?.email}
        </p>

        <p>
          <strong>Role:</strong> {user?.role}
        </p>
      </div>
    </div>
  );
}