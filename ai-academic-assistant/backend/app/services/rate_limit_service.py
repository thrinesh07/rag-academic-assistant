import time
from collections import defaultdict

RATE_LIMIT = 20
WINDOW = 60  # seconds

user_requests = defaultdict(list)


def check_rate_limit(user_id: str):

    current_time = time.time()

    requests = user_requests[user_id]

    # Remove old timestamps
    user_requests[user_id] = [
        ts for ts in requests if current_time - ts < WINDOW
    ]

    if len(user_requests[user_id]) >= RATE_LIMIT:
        return False

    user_requests[user_id].append(current_time)
    return True