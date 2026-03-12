export function hasRole(user, role) {
  return user?.role === role;
}

export function isAdmin(user) {
  return user?.role === "admin";
}