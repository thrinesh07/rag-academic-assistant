let isRefreshing = false;
let refreshSubscribers = [];

function subscribe(callback) {
  refreshSubscribers.push(callback);
}

function notifySubscribers() {
  refreshSubscribers.forEach((callback) => callback());
  refreshSubscribers = [];
}

export async function handleTokenRefresh(refreshCall) {
  if (isRefreshing) {
    return new Promise((resolve) => {
      subscribe(() => resolve());
    });
  }

  isRefreshing = true;

  try {
    await refreshCall();
    notifySubscribers();
  } finally {
    isRefreshing = false;
  }
}