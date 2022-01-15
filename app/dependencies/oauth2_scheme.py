from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
"""
Instance of the OAuth2PasswordBearer class that is used to authenticate users.
"""
