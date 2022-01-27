from typing import List, Optional, Union

from sqlmodel import Session
from sqlalchemy.exc import IntegrityError

from app.models import Role
from app.database import engine
from app.resources import BaseResource
from app.resources import permissions
from app.responses import UniqueConstraintException
from app.schemas import RoleCreate
from app.schemas import RoleUpdate
from app.schemas import Permission
from app.utils import to_dict


class RolesResource(BaseResource[Role, RoleCreate, RoleUpdate]):
    """
    Class representing a roles resource.
    """
    def get_permissions(
        self,
        id: int,
    ) -> Optional[List[Permission]]:
        """
        Obtain permissions for a specific role from the database.
        """
        with self.session as session:
            role = session.get(self.model, id)
            if role == None or not role.active:
                return None
            return role.permissions

    def update_permissions(
        self,
        id: int,
        data: Union[List[Permission], List[dict]],
        current_user_id: int,
    ) -> Optional[List[Permission]]:
        """
        Overwrite the relationship between permissions and roles in the
        database.
        """
        with self.session as session:
            role = session.get(self.model, id)
            if role == None or not role.active:
                return None
            role.permissions = []
            for item in data:
                obj_in_item = to_dict(item)
                permission = permissions.get_one(obj_in_item["permission_id"])
                if permission == None or not permission.active:
                    return None
                role.permissions.append(permission)
            role.updated_by = current_user_id
            session.add(role)
            try:
                session.commit()
            except IntegrityError:
                raise UniqueConstraintException()
            session.refresh(role)
            return role.permissions


roles = RolesResource(Role, Session(engine))
