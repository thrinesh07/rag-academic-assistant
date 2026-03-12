import { Outlet } from "react-router-dom";

export default function AuthLayout() {
  return (
    <div className="min-vh-100 d-flex align-items-center justify-content-center bg-light">
      <div className="w-100" style={{ maxWidth: "420px" }}>
        <Outlet />
      </div>
    </div>
  );
}