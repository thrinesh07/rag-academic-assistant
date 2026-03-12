# rag/constants.py

# --------------------------------------------------
# Supported Subjects
# --------------------------------------------------

SUPPORTED_SUBJECTS = {
    "os": "Operating Systems",
    "dbms": "Database Management Systems",
    "cn": "Computer Networks",
    "dsa": "Data Structures and Algorithms",
    "oops": "Object Oriented Programming"
}

# --------------------------------------------------
# Default Responses
# --------------------------------------------------

NOT_ENOUGH_INFO_RESPONSE = \
    "Not enough information in provided material"

# --------------------------------------------------
# Logging Formats
# --------------------------------------------------

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"

# --------------------------------------------------
# Similarity Score Bounds
# --------------------------------------------------

SIMILARITY_MIN = -1.0
SIMILARITY_MAX = 1.0

# --------------------------------------------------
# Metadata Keys
# --------------------------------------------------

METADATA_KEYS = [
    "subject",
    "source",
    "page",
    "chunk_id",
    "token_count"
]