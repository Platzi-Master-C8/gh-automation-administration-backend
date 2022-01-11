from sqlmodel import Session

from app.models import Role
from app.database import engine
from app.resources import BaseResource
from app.schemas import RoleCreate, RoleUpdate


class RolesResource(BaseResource[Role, RoleCreate, RoleUpdate]):
    """
    Class representing a roles resource.
    """
    pass


roles = RolesResource(Role, Session(engine))
