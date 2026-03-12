import { createContext, useEffect, useState, useCallback } from "react";
import { AuthAPI } from "../api/auth.api";

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fetch logged-in user on app startup
  const fetchUser = useCallback(async () => {
    try {
      const res = await AuthAPI.getCurrentUser();
      setUser(res.data.user);
    } catch {
      setUser(null);
    } finally {
      setLoading(false);
    }
  }, []);

  useEffect(() => {
    fetchUser();
  }, [fetchUser]);

  const login = async (credentials) => {
    const res = await AuthAPI.login(credentials);
    setUser(res.data.user);
  };

  const register = async (data) => {
    const res = await AuthAPI.register(data);
    setUser(res.data.user);
  };

  const logout = async () => {
    await AuthAPI.logout();
    setUser(null);
  };

  const value = {
    user,
    loading,
    login,
    register,
    logout,
    isAuthenticated: !!user,
    isAdmin: user?.role === "admin"
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}