from app.resources import users
from app.schemas import User, UserCreate, UserUpdate
from app.routers import setup_router


users_router = setup_router(users, "users", User, UserCreate, UserUpdate)
