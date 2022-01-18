from sqlmodel import SQLModel

from app.database import engine
from app.models import *


def drop_all_tables()->None:
    """
    Drop all tables in the database.
    """
    SQLModel.metadata.drop_all(engine)
    print("DEBUG:   ", "Database and tables dropped.")

def crate_all_tables()->None:
    """
    Create all tables in the database according to models.
    """
    SQLModel.metadata.create_all(engine)
    print("DEBUG:   ", "Database and tables created.")
