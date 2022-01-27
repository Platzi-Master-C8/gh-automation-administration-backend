from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm

from app.resources import users
from app.responses import MismatchCredentialsExeption
from app.schemas import Token
from app.utils import create_access_token
from app.utils import get_response_login
from app.utils import get_verified_token
from app.utils import verify_password


router = APIRouter(
    tags=["auth"],
)

@router.post("/token", status_code=status.HTTP_200_OK, response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()) -> dict:
    """
    Provide access token for user.
    Must receive `username` and `password`  into a `x-www-form-urlencoded`
    format to return a JWT token.
    """
    user = users.get_by_email(form_data.username)
    if not user:
        raise MismatchCredentialsExeption()
    if not verify_password(form_data.password, user.password):
        raise MismatchCredentialsExeption()
    data = {
        "sub": user.email,
        "user_id": user.user_id,
        "role_id": user.role_id,
    }
    access_token = create_access_token(data)
    response_login = get_response_login(access_token)
    return response_login 

@router.get(
    "/token/verify",
    status_code=status.HTTP_200_OK,
    response_model=Token
)
async def verify_token(token: str) -> dict:
    """
    Verify integrity of token.
    """
    verified_token = get_verified_token(token)
    return verified_token
