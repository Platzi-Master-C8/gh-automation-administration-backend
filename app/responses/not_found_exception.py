from fastapi import HTTPException, status


class NotFoundException(HTTPException):
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
