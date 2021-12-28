from sqlmodel import SQLModel

from app.models import *
from app.database import first_admin
from app.database import engine
from app.resources import users


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("DEBUG:   ", "Database and tables created.")

def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)
    print("DEBUG:   ", "Database and tables dropped.")

def create_admin_user():
    users.create(first_admin)
    print("DEBUG:   ", "Admin user created.")
