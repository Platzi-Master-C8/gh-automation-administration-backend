from app.resources import roles
from app.schemas import Role, RoleCreate, RoleUpdate
from app.routers import setup_router


roles_router = setup_router(roles, "roles", Role, RoleCreate, RoleUpdate)
