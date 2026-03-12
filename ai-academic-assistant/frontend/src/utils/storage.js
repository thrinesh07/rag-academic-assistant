export const storage = {
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch {
      // silently fail
    }
  },

  get(key) {
    try {
      const value = localStorage.getItem(key);
      return value ? JSON.parse(value) : null;
    } catch {
      return null;
    }
  },

  remove(key) {
    try {
      localStorage.removeItem(key);
    } catch {
      // ignore
    }
  }
};