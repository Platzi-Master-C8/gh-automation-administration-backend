from datetime import datetime, timedelta

from fastapi import HTTPException, status
from jose import jwt, JWTError

from app.core import settings
from app.responses import MismatchCredentialsExeption


def create_access_token(data: dict):
    """
    Create an access token based on environment variables.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt

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
