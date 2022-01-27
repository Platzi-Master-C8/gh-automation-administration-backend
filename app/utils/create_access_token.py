from datetime import datetime, timedelta

from jose import jwt

from app.core import settings


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
