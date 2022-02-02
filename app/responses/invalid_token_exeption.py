from fastapi import HTTPException, status


class InvalidTokenException(HTTPException):
    """
    Class reperesenting a `invalid token` custom exception.
    Throw this exception when token verification fails.
    """
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = {
            "status": status.HTTP_401_UNAUTHORIZED,
            "code": "CHAMELEON",
            "title": "Invalid token",
            "description":
                "Token could be invalid or expired. Please try again.",
        }
        headers = {"WWW-Authenticate": "Bearer"}
        self.headers = headers
