from app.resources import users
from app.schemas import User, UserCreate, UserUpdate
from app.routers import configure


users_router = configure(users, "users", User, UserCreate, UserUpdate)
