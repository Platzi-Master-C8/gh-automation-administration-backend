from fastapi import HTTPException, status


class UniqueConstraintException(HTTPException):
    """
    Class reperesenting a `unique constraint` custom exception.
    Throw this exception when attempting to create a resource with a duplicated
    value on fields with `unique` constraint.
    """
    def __init__(self):
        self.status_code = status.HTTP_400_BAD_REQUEST
        self.detail = {
            "status": status.HTTP_400_BAD_REQUEST,
            "code": "PENGUIN",
            "title": "Unique constraint violation",
            "description":
                "One or more fields already exists with the same value.",
        }
