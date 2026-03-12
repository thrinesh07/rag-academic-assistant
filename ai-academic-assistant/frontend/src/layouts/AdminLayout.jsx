import { Outlet } from "react-router-dom";
import Navbar from "../components/navigation/Navbar";

export default function AdminLayout() {
  return (
    <div className="d-flex flex-column min-vh-100">
      <Navbar />

      <main className="flex-grow-1 bg-white">
        <div className="container py-4">
          <div className="mb-4">
            <h4 className="fw-bold">Admin Panel</h4>
            <hr />
          </div>

          <Outlet />
        </div>
      </main>
    </div>
  );
}