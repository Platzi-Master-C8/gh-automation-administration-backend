from typing import List

from fastapi import APIRouter, status

from app.resources import roles
from app.responses import NotFoundExeption
from app.schemas import Role, RoleCreate, RoleUpdate


router = APIRouter(
    prefix="/api/roles",
    tags=["roles"],
)

@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=Role,
)
async def create_role(data: RoleCreate):
    """
    Create a new role with requested data.
    """
    created_role = roles.create(data)
    return created_role

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[Role],
)
async def read_roles():
    """
    Retrieve all requested roles.
    """
    all_roles = roles.get_all()

    return all_roles

@router.get(
    "/{role_id}",
    status_code=status.HTTP_200_OK,
    response_model=Role,
)
async def read_role(role_id: int):
    """
    Retrieve an specific role.
    """
    role = roles.get_one(role_id)
    if role == None:
        raise NotFoundExeption("role", role_id)
    return role

@router.put(
    "/{role_id}",
    status_code=status.HTTP_200_OK,
    response_model=Role,
)
async def update_role(role_id: int, role: RoleUpdate):
    """
    Update an specific role with requested data.
    """
    updated_role = roles.update(role_id, role)
    if updated_role == None:
        raise NotFoundExeption("role", role_id)
    return updated_role

@router.delete("/{role_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_role(role_id: int):
    """
    Soft-delete an specific role.
    """
    role = roles.delete(role_id)
    if role == None:
        raise NotFoundExeption("role", role_id)
    return None
