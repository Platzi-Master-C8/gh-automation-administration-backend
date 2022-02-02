from jose import jwt, JWTError

from app.core import settings
from app.responses import MismatchCredentialsExeption


def get_payload(token: str):
    """
    Obtain the payload of a given token.
    """
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )
    except JWTError:
        raise MismatchCredentialsExeption()
    return payload
