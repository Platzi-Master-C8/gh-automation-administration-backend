import pyotp

from fastapi import APIRouter
from fastapi import Depends, Form
from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

from app.resources import users
from app.responses import MismatchCredentialsExeption
from app.schemas import Token
from app.utils import create_access_token
from app.utils import get_permissions_as_string
from app.utils import get_response_login
from app.utils import get_verified_token
from app.utils import verify_password
from app.utils import get_payload


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
    sub = user.email
    user_id = user.user_id
    role_id = user.role_id
    permissions = users.get_permissions(user_id)
    scope = get_permissions_as_string(permissions)
    data = {
        "sub": sub,
        "user_id": user_id,
        "role_id": role_id,
        "scope": scope,
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


            ##########################
            ### MFA Authentication ###
            ##########################

class UserCredentials():
    def __init__(
        self,
        username: str = Form(...),
        password: str = Form(...)
    ):
        self.username = username
        self.password = password

class PreLoginToken(BaseModel):
    grant_token: str
    mfa_active: bool

@router.post('/pre-login', response_model=PreLoginToken)
def pre_login(form_data: UserCredentials = Depends()):
    user = users.get_by_email(form_data.username)
    # 1. Verify if user exist
    if not user:
        raise MismatchCredentialsExeption()
    # 2. Verify password
    if not verify_password(form_data.password, user.password):
        raise MismatchCredentialsExeption()
    # 3. Check if user has a UserOTPkey and set mfaActive bool value
    isMFAactivated = False
    # 4. Tokenize user info
    token = create_access_token({
        'sub': user.email,
        'user_id': user.user_id,
        'mfa_active': isMFAactivated
    })
    # 5. Return token and mfaActive boolean
    return PreLoginToken(grant_token=token, mfa_active=isMFAactivated)



class GetQRrequest(BaseModel):
    grant_token: str

class URLforQR(BaseModel):
    grant_token: str
    url: str

@router.get('/mfa-qr', response_model=URLforQR)
def multifactor_auth_qr(req: GetQRrequest):
    # 1. Verify token signature and content
    payload = get_payload(req.grant_token)
    # 2. Generate url to activate OTP
    SECRET_OTP = pyotp.random_base32()
    otp_url = pyotp.totp.TOTP(SECRET_OTP).provisioning_uri(
        name=payload.sub,
        issuer_name='getHired App'
    )
    # 2.1 Store generated UserOTPkey

    # Generate new token, changing mfaActive
    payload.mfa_active = True
    return URLforQR(grant_token=payload, url=otp_url)



class MFAloginRequest(BaseModel):
    grant_token: str
    otp_code: str

class AccessToken(BaseModel):
    access_token: str
    token_type: str = 'bearer'


@router.post('/mfa-login', response_model=AccessToken)
def mfa_login(req: MFAloginRequest):
    # 1. Verify token signature and content
    payload = get_payload(req.grant_token)
    # 1.1 Get user SECRET_OTP
    SECRET_OTP = 'getFromDB'
    # 2. Verify OTP code
    totp = pyotp.TOTP(SECRET_OTP)
    if not totp.verify(totp.now()):
        # Rise auth error
        pass
    # 3. Generate new token with all user info
    pass