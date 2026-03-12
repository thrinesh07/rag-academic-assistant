from enum import Enum


class UserRole(str, Enum):
    USER = "user"
    ADMIN = "admin"


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"


class SupportedSubject(str, Enum):
    OS = "OS"
    DBMS = "DBMS"
    CN = "CN"
    DSA = "DSA"
    OOPS = "OOPS"


ALLOWED_SUBJECTS = {subject.value for subject in SupportedSubject}


ALLOWED_FILE_TYPES = {"application/pdf"}