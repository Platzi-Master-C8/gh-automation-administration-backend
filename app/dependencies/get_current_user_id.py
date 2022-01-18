from fastapi import Depends

from app.dependencies.oauth2_scheme import oauth2_scheme
from app.resources import users
from app.utils import get_payload
from app.utils import to_dict


async def get_current_user_id(token: str = Depends(oauth2_scheme)):
    """
    Obtain the current user from the JWT token.
    Decode the token, extract the email and looking for matching user.
    """
    payload = get_payload(token)
    user_email = payload.get("sub")
    user = users.get_by_email(user_email)
    user_as_dict = to_dict(user)
    user_id = user_as_dict.get("id")
    return user_id
