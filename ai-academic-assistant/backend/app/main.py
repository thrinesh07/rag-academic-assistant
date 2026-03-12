from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.middleware.error_handler import register_exception_handlers
from app.middleware.rate_limiter import RateLimiterMiddleware
from app.middleware.request_logger import RequestLoggerMiddleware
from app.core.config import settings
from app.lifespan import lifespan


# ==========================================================
# APPLICATION INSTANCE
# ==========================================================

app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Production-grade AI Academic Assistant Backend",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)


# ==========================================================
# CORS CONFIGURATION
# ==========================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_URL],
    allow_credentials=True,     # Required for HTTPOnly cookies
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==========================================================
# MIDDLEWARE REGISTRATION
# ==========================================================

# Order matters.
# Request logger first → rate limiter → route handlers.

app.add_middleware(RequestLoggerMiddleware)
app.add_middleware(RateLimiterMiddleware)


# ==========================================================
# ROUTES
# ==========================================================

app.include_router(api_router, prefix="/api/v1")


# ==========================================================
# EXCEPTION HANDLERS
# ==========================================================

register_exception_handlers(app)


# ==========================================================
# ROOT ENDPOINT
# ==========================================================

@app.get("/", tags=["Root"])
def root():
    return {
        "service": settings.APP_NAME,
        "version": "1.0.0",
        "status": "running"
    }