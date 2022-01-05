from typing import List, Union

from sqlmodel import select, Session

from app.models import User
from app.database import engine
from app.schemas import UserCreate, UserUpdate
from app.utils import hash_password, to_dict


class UsersResource():
    def __init__(self, model: User, session: Session):
        self.model = model
        self.session = session

    def create(self, data: Union[dict, UserCreate]) -> User:
        obj_in_data = to_dict(data)
        obj_in_data["password"] = hash_password(obj_in_data["password"])
        user = self.model(**obj_in_data)
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
            statement = select(self.model).where(self.model.is_deleted == False)
            result = session.exec(statement)
            users = result.all()
            session.close()
            return users

    def update(self, id: int, data: UserUpdate) -> User:
        obj_in_data = to_dict(data)
        if "password" in obj_in_data:
            obj_in_data["password"] = hash_password(obj_in_data["password"])
        with self.session as session:
            user = session.get(self.model, id)
            for key, value in obj_in_data.items():
                setattr(user, key, value)
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user

    def delete(self, id: int) -> None:
        with self.session as session:
            user = session.get(self.model, id)
            user.is_deleted = True
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user


users = UsersResource(User, Session(engine))
