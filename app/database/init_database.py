from sqlmodel import SQLModel

from app.models import *
from app.database import engine
from app.database import roles as first_roles
from app.database import superuser
from app.resources import roles
from app.resources import users


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("DEBUG:   ", "Database and tables created.")

def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)
    print("DEBUG:   ", "Database and tables dropped.")

def create_first_roles():
    for role in first_roles:
        roles.create(role)
    print("DEBUG:   ", "First roles created.")

def create_first_admin():
    users.create(superuser)
    print("DEBUG:   ", "First administrator created.")
