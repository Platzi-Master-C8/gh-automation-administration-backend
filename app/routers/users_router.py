from typing import List

from fastapi import APIRouter, status

from app.resources import users
from app.responses import NotFoundExeption
from app.schemas import User, UserCreate, UserUpdate


router = APIRouter(
    prefix="/api/users",
    tags=["users"],
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=User,
)
async def create_user(data: UserCreate):
    """
    Create a new user with requested data.
    """

    created_user = users.create(data)
    return created_user

@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[User],
)
async def read_users():
    """
    Retrieve all requested users.
    """
    
    all_users = users.get_all()

    return all_users

@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=User,
)
async def read_user(user_id: int):
    """
    Retrieve an specific user.
    """

    user = users.get_one(user_id)
    if user == None:
        raise NotFoundExeption("user", user_id)
    return user

@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=User,
)
async def update_user(user_id: int, user: UserUpdate):
    """
    Update an specific user with requested data.
    """

    updated_user = users.update(user_id, user)
    if updated_user == None:
        raise NotFoundExeption("user", user_id)
    return updated_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """
    Soft-delete an specific user.
    """

    user = users.delete(user_id)
    if user == None:
        raise NotFoundExeption("user", user_id)
    return None
