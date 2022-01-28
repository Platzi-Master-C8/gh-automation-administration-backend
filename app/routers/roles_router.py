from typing import List

from fastapi import Depends
from fastapi import status

from app.dependencies import get_current_user_id
from app.responses import NotFoundException
from app.resources import roles
from app.routers import setup_router
from app.schemas import Permission
from app.schemas import Role
from app.schemas import RoleCreate
from app.schemas import RoleUpdate


roles_router = setup_router(roles, "roles", Role, RoleCreate, RoleUpdate)

@roles_router.get(
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
    permissions = roles.get_permissions(id)
    if permissions == None:
        raise NotFoundException("roles", id)
    return permissions

@roles_router.put(
    "/{id}/permissions",
    status_code=status.HTTP_200_OK,
    response_model=List[Permission],
)
def update_role_permissions(
    id: int,
    permissions: List[Permission],
    current_user_id: int = Depends(get_current_user_id),
):
    """
    Update permissions for a specific role.
    """
    updated = roles.update_permissions(id, permissions, current_user_id)
    if updated == None:
        raise NotFoundException("roles", id)
    return updated
