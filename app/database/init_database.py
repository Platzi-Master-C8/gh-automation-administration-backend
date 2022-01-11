from sqlmodel import SQLModel

from app.models import *
from app.database import superuser
from app.database import engine
from app.resources import users


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("DEBUG:   ", "Database and tables created.")

def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)
    print("DEBUG:   ", "Database and tables dropped.")

def create_first_admin():
    users.create(superuser)
    print("DEBUG:   ", "First administrator created.")
