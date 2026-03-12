import { Outlet } from "react-router-dom";
import Navbar from "../components/navigation/Navbar";

export default function DashboardLayout() {
  return (
    <div className="d-flex flex-column min-vh-100">
      <Navbar />

      <main className="flex-grow-1 bg-light">
        <div className="container py-4">
          <Outlet />
        </div>
      </main>
    </div>
  );
}