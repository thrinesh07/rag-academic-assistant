import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./pages/auth/Login";
import Register from "./pages/auth/Register";

import ChatPage from "./pages/dashboard/ChatPage";
import HistoryPage from "./pages/dashboard/HistoryPage";
import ProfilePage from "./pages/dashboard/ProfilePage";

import UploadPage from "./pages/admin/UploadPage";
import IndexStatusPage from "./pages/admin/IndexStatusPage";

import NotFound from "./pages/NotFound";

import AuthLayout from "./layouts/AuthLayout";
import DashboardLayout from "./layouts/DashboardLayout";
import AdminLayout from "./layouts/AdminLayout";

import ProtectedRoute from "./router/ProtectedRoute";
import RoleProtectedRoute from "./router/RoleProtectedRoute";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* ================= PUBLIC ROUTES ================= */}
        <Route element={<AuthLayout />}>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Route>

        {/* ================= STUDENT PROTECTED ROUTES ================= */}
        <Route element={<ProtectedRoute />}>
          <Route element={<DashboardLayout />}>

            <Route path="/" element={<ChatPage />} />
            <Route path="/history" element={<HistoryPage />} />
            <Route path="/profile" element={<ProfilePage />} />

          </Route>
        </Route>

        {/* ================= ADMIN PROTECTED ROUTES ================= */}
        <Route element={<ProtectedRoute />}>
          <Route element={<RoleProtectedRoute role="admin" />}>
            <Route element={<AdminLayout />}>

              <Route path="/admin/upload" element={<UploadPage />} />
              <Route path="/admin/status" element={<IndexStatusPage />} />

            </Route>
          </Route>
        </Route>

        {/* ================= FALLBACK ================= */}
        <Route path="*" element={<NotFound />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;