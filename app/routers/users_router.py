from typing import List

from fastapi import Depends
from fastapi import status

from app.dependencies import get_current_user_id
from app.responses import NotFoundException
from app.resources import users
from app.schemas import Permission
from app.schemas import User
from app.schemas import UserCreate
from app.schemas import UserUpdate
from app.routers import setup_router


users_router = setup_router(users, "users", User, UserCreate, UserUpdate)

@users_router.get(
    "/{id}/permissions",
    status_code=status.HTTP_200_OK,
    response_model=List[Permission],
)
def get_role_permissions(
    id: int,
    current_user_id: int = Depends(get_current_user_id),
):
    """
    Retrieve permissions for a specific role.
    """
    permissions = users.get_permissions(id)
    if permissions == None:
        raise NotFoundException("users", id)
    return permissions

