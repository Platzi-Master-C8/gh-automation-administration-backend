from typing import List, Type, TypeVar

from fastapi import APIRouter, status
from pydantic import BaseModel
from app.resources import BaseResource

from app.responses import NotFoundExeption

ResourceType = TypeVar("ResourceType", bound=BaseResource)
SingleSchemaType = TypeVar("SingleSchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

def configure(
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
    async def create_resource(data: create_schema):
        """
        Create a new resource with requested data.
        """
        created = resource.create(data)
        return created

    @router.get(
        "/",
        status_code=status.HTTP_200_OK,
        response_model=List[single_schema],
    )
    async def read_resources():
        """
        Retrieve all requested users.
        """
        all = resource.get_all()

        return all

    @router.get(
        "/{id}",
        status_code=status.HTTP_200_OK,
        response_model=single_schema,
    )
    async def read_resource(id: int):
        """
        Retrieve an specific user.
        """
        obtained = resource.get_one(id)
        if obtained == None:
            raise NotFoundExeption(resource_name, id)
        return obtained

    @router.put(
        "/{id}",
        status_code=status.HTTP_200_OK,
        response_model=single_schema,
    )
    async def update_resource(id: int, data: update_schema):
        """
        Update an specific user with requested data.
        """
        updated = resource.update(id, data)
        if updated == None:
            raise NotFoundExeption(resource_name, id)
        return updated

    @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
    async def delete_resource(id: int):
        """
        Soft-delete an specific user.
        """
        deleted = resource.delete(id)
        if deleted == None:
            raise NotFoundExeption(resource_name, id)
        return None

    return router