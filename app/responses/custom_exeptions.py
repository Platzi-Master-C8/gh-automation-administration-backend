from fastapi import HTTPException, status


class NotFoundExeption(HTTPException):
    """
    Class reperesenting a `not found` custom exception.
    Throw this exception when a router receives `None` from resources at `id`
    dependant requests.
    """
    def __init__(self, resource: str, id: int):
        self.status_code = status.HTTP_404_NOT_FOUND
        self.detail = {
            "status": status.HTTP_404_NOT_FOUND,
            "code": "EAGLE",
            "title": "Resource not found",
            "description": f"The {resource} with id {id} was not found.",
        }


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
