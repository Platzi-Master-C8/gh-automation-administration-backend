from app.resources import roles
from app.schemas import Role, RoleCreate, RoleUpdate
from app.routers import configure


roles_router = configure(roles, "roles", Role, RoleCreate, RoleUpdate)
