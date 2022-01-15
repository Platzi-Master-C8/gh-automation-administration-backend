from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.resources import users
from app.responses import MismatchCredentialsExeption
from app.utils import create_access_token, verify_password


router = APIRouter(
    prefix='/auth',
    tags=['auth']
)

@router.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users.get_by_email(form_data.username)
    if not user:
        raise MismatchCredentialsExeption()
    if not verify_password(form_data.password, user.password):
        raise MismatchCredentialsExeption()
    data = {
        'sub': user.email,
        'role_id': user.role_id
    }
    access_token = create_access_token(data)
    return {"access_token": access_token, "token_type": "bearer"}
