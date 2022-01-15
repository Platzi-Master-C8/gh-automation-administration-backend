from sqlmodel import SQLModel

from app.core import settings
from app.models import *
from app.database import engine
from app.database.populate import populate_permissions
from app.database.populate import populate_roles
from app.database.populate import populate_users

def init_database()->None:
    """
    Run the database initialization functions according to the settings.
    """
    if settings.DB_RESET:
        SQLModel.metadata.drop_all(engine)
        print("DEBUG:   ", "Database and tables dropped.")
        SQLModel.metadata.create_all(engine)
        print("DEBUG:   ", "Database and tables created.")
    if settings.DB_POPULATE:
       populate_permissions(settings.DB_POPULATION) 
       populate_roles(settings.DB_POPULATION) 
       populate_users(settings.DB_POPULATION) 
