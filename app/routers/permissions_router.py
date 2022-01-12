from app.resources import permissions
from app.schemas import Permission, PermissionCreate, PermissionUpdate
from app.routers import setup_router


permissions_router = setup_router(
    permissions,
    "permissions",
    Permission,
    PermissionCreate,
    PermissionUpdate
)
