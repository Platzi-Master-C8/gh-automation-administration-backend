from sqlmodel import Session

from app.models import Permission
from app.database import engine
from app.resources import BaseResource
from app.schemas import PermissionCreate, PermissionUpdate


class PermissionsResource(
    BaseResource[Permission, PermissionCreate, PermissionUpdate]
):
    """
    Class representing a roles resource.
    """
    pass


permissions = PermissionsResource(Permission, Session(engine))
