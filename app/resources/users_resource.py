from typing import List, Union

from sqlmodel import select, Session

from app.models import User
from app.database import engine
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.utils import hash_password


class UsersResource():
    def __init__(self, model: User, session: Session):
        self.model = model
        self.session = session

    def create(self, data: Union[dict, UserCreate]) -> User:
        if type(data) is not dict:
            data_as_dict = data.dict()
            data_as_dict["password"] = hash_password(data_as_dict["password"])
            user = self.model(**data_as_dict)
        else:
            data["password"] = hash_password(data["password"])
            user = self.model(**data)
        with self.session as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user

    def get_one(self, id: int) -> User:
        with self.session as session:
            user = session.get(self.model, id)
            session.close()
            return user
 
    def get_all(self) -> List[User]:
        with self.session as session:
            statement = select(self.model).where(self.model.is_active == True)
            result = session.exec(statement)
            users = result.all()
            session.close()
            return users

    def update(self, id: int, data: UserUpdate) -> User:
        data_as_dict = data.dict(exclude_unset=True)
        if "password" in data_as_dict:
            data_as_dict["password"] = hash_password(data_as_dict["password"])
        with self.session as session:
            user = session.get(self.model, id)
            for key, value in data_as_dict.items():
                setattr(user, key, value)
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user

    def delete(self, id: int) -> None:
        with self.session as session:
            user = session.get(self.model, id)
            user.is_active = False
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user


users = UsersResource(User, Session(engine))
