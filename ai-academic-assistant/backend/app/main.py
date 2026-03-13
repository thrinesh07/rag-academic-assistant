from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.middleware.error_handler import register_exception_handlers
from app.middleware.rate_limiter import RateLimiterMiddleware
from app.middleware.request_logger import RequestLoggerMiddleware
from app.core.config import settings
from app.lifespan import lifespan


app = FastAPI(
    title=settings.APP_NAME,
    version="1.0.0",
    description="Production-grade AI Academic Assistant Backend",
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)


# --------------------------------------------------
# CORS (MUST BE FIRST)
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://rag-academic-assistant.vercel.app",
    ],
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# CUSTOM MIDDLEWARE
# --------------------------------------------------

app.add_middleware(RequestLoggerMiddleware)
app.add_middleware(RateLimiterMiddleware)


# --------------------------------------------------
# ROUTES
# --------------------------------------------------

app.include_router(api_router, prefix="/api/v1")


# --------------------------------------------------
# EXCEPTIONS
# --------------------------------------------------

register_exception_handlers(app)


@app.get("/")
def root():
    return {
        "service": settings.APP_NAME,
        "status": "running"
    }