from typing import Optional, Union

from sqlalchemy.exc import IntegrityError
from sqlmodel import select, Session

from app.database import engine
from app.models import User
from app.resources import BaseResource
from app.responses import UniqueConstraintException
from app.schemas import UserCreate, UserUpdate
from app.utils import hash_password, to_dict


class UsersResource(BaseResource[User, UserCreate, UserUpdate]):
    """
    Class representing a users resource.
    """
    def create(
        self,
        data: Union[dict, UserCreate],
        current_user_id: int,
    ) -> User:
        """
        Receive data from router to insert it into database.
        Before insert, hash the password.
        """
        obj_in_data = to_dict(data)
        obj_in_data["password"] = hash_password(obj_in_data["password"])
        user = self.model(**obj_in_data)
        user.created_by = current_user_id
        with self.session as session:
            session.add(user)
            try:
                session.commit()
            except IntegrityError as e:
                raise UniqueConstraintException()
            session.commit()
            session.refresh(user)
            return user

    def update(
        self,
        id: int,
        data: UserUpdate,
        current_user_id: int,
    ) -> Optional[User]:
        """
        Receive ID and data from router to update an item in database.
        Check if data contains the password key to hash it before update.
        """
        obj_in_data = to_dict(data)
        obj_in_data.update({"updated_by": current_user_id})
        if "password" in obj_in_data:
            obj_in_data["password"] = hash_password(obj_in_data["password"])
        with self.session as session:
            user = session.get(self.model, id)
            if user == None or not user.active:
                return None
            for key, value in obj_in_data.items():
                setattr(user, key, value)
            session.add(user)
            try:
                session.commit()
            except IntegrityError as e:
                raise UniqueConstraintException()
            session.refresh(user)
            return user

    def get_by_email(self, email: str) -> Optional[User]:
        """
        Receive email from router to get an item from database.
        """
        with self.session as session:
            statement = select(self.model).where(self.model.email == email)
            user = session.exec(statement).first()
            if user == None or not user.active:
                return None
            return user


users = UsersResource(User, Session(engine))
