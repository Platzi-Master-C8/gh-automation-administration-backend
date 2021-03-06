from typing import Generic, List, Optional, Type, TypeVar, Union

from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from sqlmodel import select, Session

from app.models import Auditor
from app.responses import UniqueConstraintException
from app.utils import to_dict


ModelType = TypeVar("ModelType", bound=Auditor)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class BaseResource(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], session: Session):
        self.model = model
        self.session = session

    def create(
        self,
        data: Union[CreateSchemaType, dict],
        current_user_id: int,
    ) -> ModelType:
        obj_in_data = to_dict(data)
        resource = self.model(**obj_in_data)
        resource.created_by = current_user_id
        with self.session as session:
            session.add(resource)
            try:
                session.commit()
            except IntegrityError as e:
                raise UniqueConstraintException()
            session.refresh(resource)
            return resource

    def get_one(self, id: int) -> Optional[ModelType]:
        with self.session as session:
            resource = session.get(self.model, id)
            if resource == None or not resource.active:
                return None
            return resource
 
    def get_all(self) -> List[ModelType]:
        with self.session as session:
            statement = select(self.model).where(self.model.active == True)
            result = session.exec(statement)
            users = result.all()
            return users

    def update(
        self,
        id: int,
        data: Union[UpdateSchemaType, dict],
        current_user_id: int,
    ) -> Optional[ModelType]:
        obj_in_data = to_dict(data)
        with self.session as session:
            resource = session.get(self.model, id)
            if resource == None or not resource.active:
                return None
            for key, value in obj_in_data.items():
                setattr(resource, key, value)
            resource.updated_by = current_user_id
            session.add(resource)
            try:
                session.commit()
            except IntegrityError as e:
                raise UniqueConstraintException()
            session.refresh(resource)
            return resource

    def delete(self, id: int, current_user_id: int) -> bool:
        with self.session as session:
            resource = session.get(self.model, id)
            if resource == None or not resource.active:
                return None
            resource.active = False
            resource.updated_by = current_user_id
            session.add(resource)
            session.commit()
            session.refresh(resource)
            return True
