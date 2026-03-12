# from fastapi import Request, HTTPException
# from app.core.security import decode_token
# from app.core.exceptions import AuthenticationError


# def get_current_user(request: Request) -> str:
#     token = request.cookies.get("access_token")

#     if not token:
#         raise HTTPException(status_code=401, detail="Not authenticated")

#     try:
#         payload = decode_token(token, expected_type="access")
#         return payload["sub"]

#     except AuthenticationError:
#         raise HTTPException(status_code=401, detail="Authentication failed")