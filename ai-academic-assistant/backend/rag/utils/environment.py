# rag/utils/environment.py

import os


REQUIRED_ENV_VARS = [
    "GROQ_API_KEY"
]


def validate_environment():
    missing = []

    for var in REQUIRED_ENV_VARS:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        raise EnvironmentError(
            f"Missing required environment variables: {missing}"
        )