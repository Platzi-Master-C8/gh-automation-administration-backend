from typing import List, Type, TypeVar

from fastapi import APIRouter, Depends, status
from pydantic import BaseModel

from app.dependencies import get_current_user_id
from app.resources import BaseResource
from app.responses import NotFoundExeption


ResourceType = TypeVar("ResourceType", bound=BaseResource)
SingleSchemaType = TypeVar("SingleSchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

def setup_router(
    resource: Type[ResourceType],
    resource_name: str,
    single_schema: Type[SingleSchemaType],
    create_schema: Type[CreateSchemaType],
    update_schema: Type[UpdateSchemaType],
) -> APIRouter:
    """
    Set up a router for a given resource by adding basic CRUD operations.
    """
    router = APIRouter(
        prefix=f"/api/{resource_name}",
        tags=[f"{resource_name}"],
    )

    @router.post(
        "/",
        status_code=status.HTTP_201_CREATED,
        response_model=single_schema,
    )
    async def create_resource(
        data: create_schema,
        current_user_id: int = Depends(get_current_user_id),
    ):
        """
        Create a new resource with requested data.
        """
        created = resource.create(data, current_user_id)
        return created

    @router.get(
        "/",
        status_code=status.HTTP_200_OK,
        response_model=List[single_schema],
    )
    async def read_resources(
        current_user_id: int = Depends(get_current_user_id),
    ):
        """
        Retrieve all requested resources.
        """
        all = resource.get_all()
        return all

    @router.get(
        "/{resource_id}",
        status_code=status.HTTP_200_OK,
        response_model=single_schema,
    )
    async def read_resource(
        resource_id: int,
        current_user_id: int = Depends(get_current_user_id),
    ):
        """
        Retrieve an specific resource.
        """
        obtained = resource.get_one(resource_id)
        if obtained == None:
            raise NotFoundExeption(resource_name, resource_id)
        return obtained

    @router.put(
        "/{resource_id}",
        status_code=status.HTTP_200_OK,
        response_model=single_schema,
    )
    async def update_resource(
        resource_id: int,
        data: update_schema,
        current_user_id: int = Depends(get_current_user_id),
    ):
        """
        Update an specific resource with requested data.
        """
        updated = resource.update(resource_id, data, current_user_id)
        if updated == None:
            raise NotFoundExeption(resource_name, resource_id)
        return updated

    @router.delete("/{resource_id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_resource(
        resource_id: int,
        current_user_id: int = Depends(get_current_user_id),
    ):
        """
        Soft-delete an specific resource.
        """
        deleted = resource.delete(resource_id, current_user_id)
        if deleted == None:
            raise NotFoundExeption(resource_name, resource_id)
        return None

    return router
