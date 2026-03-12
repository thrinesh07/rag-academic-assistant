import time
from collections import defaultdict
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import logger

RATE_LIMIT = 20
WINDOW = 60  # seconds

request_store = defaultdict(list)


class RateLimiterMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request: Request, call_next):

        identifier = self.get_identifier(request)
        current_time = time.time()

        timestamps = request_store[identifier]

        # Remove old timestamps
        request_store[identifier] = [
            ts for ts in timestamps if current_time - ts < WINDOW
        ]

        if len(request_store[identifier]) >= RATE_LIMIT:
            logger.warning(f"Rate limit exceeded: {identifier}")
            return JSONResponse(
                status_code=429,
                content={
                    "success": False,
                    "error": "Rate limit exceeded"
                }
            )

        request_store[identifier].append(current_time)

        response = await call_next(request)
        return response

    def get_identifier(self, request: Request):
        user_cookie = request.cookies.get("access_token")
        if user_cookie:
            return user_cookie
        return request.client.host