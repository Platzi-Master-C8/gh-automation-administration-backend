__all__ = ["auth_router","permissions_router", "roles_router", "users_router"]
from app.routers.auth_router import router as auth_router
from app.routers.base_router import setup_router
from app.routers.permissions_router import permissions_router
from app.routers.roles_router import roles_router
from app.routers.users_router import users_router
