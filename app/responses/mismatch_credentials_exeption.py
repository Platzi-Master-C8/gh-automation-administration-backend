from fastapi import HTTPException, status


class MismatchCredentialsExeption(HTTPException):
    """
    Class reperesenting a `mismatch credentials` custom exception.
    Throw this exception when a login request receives a wrong `email` or
    `password`.
    """
    def __init__(self):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        self.detail = {
            "status": status.HTTP_401_UNAUTHORIZED,
            "code": "CERBERUS",
            "title": "Mismatch credentials",
            "description":
                "Email or password entered are incorrect. Please try again.",
        }
        headers = {"WWW-Authenticate": "Bearer"}
        self.headers = headers
