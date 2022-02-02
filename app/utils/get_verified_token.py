from jose import jwt, JWTError

from app.core import settings
from app.responses import InvalidTokenException
from app.utils import get_response_login

def get_verified_token(token: str) -> dict:
    """
    Obtain the payload of a given token.
    """
    try:
        jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
    except JWTError:
        raise InvalidTokenException()
    response_login = get_response_login(token)
    return response_login
