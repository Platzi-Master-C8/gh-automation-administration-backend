from app.core import settings
from app.database.populate import populate_permissions
from app.database.populate import populate_roles
from app.database.populate import populate_users
from app.database.populate import set_relationships
from app.database.reset import crate_all_tables
from app.database.reset import drop_all_tables


def init_database()->None:
    """
    Run the database initialization functions according to the settings.
    """
    if settings.DB_RESET == "true" or settings.DB_RESET == "True":
        drop_all_tables()
        crate_all_tables()
    if settings.DB_POPULATE == "true" or settings.DB_POPULATE == "True":
        populate_permissions(settings.DB_POPULATION) 
        populate_roles(settings.DB_POPULATION) 
        populate_users(settings.DB_POPULATION) 
        set_relationships(settings.DB_POPULATION) 
