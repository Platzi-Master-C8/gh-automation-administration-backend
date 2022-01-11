from typing import Optional, Union

from sqlmodel import Session

from app.models import User
from app.database import engine
from app.resources import BaseResource
from app.schemas import UserCreate, UserUpdate
from app.utils import hash_password, to_dict


class UsersResource(BaseResource[User, UserCreate, UserUpdate]):
    """
    Class representing a users resource.
    """
    def create(self, data: Union[dict, UserCreate]) -> User:
        """
        Receive data from router to insert it into database.
        Before insert, hash the password.
        """
        obj_in_data = to_dict(data)
        obj_in_data["password"] = hash_password(obj_in_data["password"])
        user = self.model(**obj_in_data)
        with self.session as session:
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user

    def update(self, id: int, data: UserUpdate) -> Optional[User]:
        """
        Receive ID and data from router to update an item in database.
        Check if data contains the password key to hash it before update.
        """
        obj_in_data = to_dict(data)
        if "password" in obj_in_data:
            obj_in_data["password"] = hash_password(obj_in_data["password"])
        with self.session as session:
            user = session.get(self.model, id)
            if user == None:
                session.close()
                return None
            for key, value in obj_in_data.items():
                setattr(user, key, value)
            session.add(user)
            session.commit()
            session.refresh(user)
            session.close()
            return user

    def get_by_email(self, email: str) -> Optional[User]:
        """
        Receive email from router to get an item from database.
        """
        with self.session as session:
            user = session.exec(self.model).filter_by(email=email).first()
            session.close()
            return user


users = UsersResource(User, Session(engine))
