from app.core.config import settings


def get_sqlite_uri():
    """
    Create a URI to connect to the SQLite database.
    """

    driver = "sqlite"
    host = ":memory:"
    uri = f"{driver}:///{host}"
    return uri
    
def get_postgresql_uri():
    """
    Create a URI to connect to the PostgreSQL database.
    """
 
    driver = settings.DB_DRIVER
    host = settings.DB_HOST
    port = settings.DB_PORT
    user = settings.DB_USER
    password = settings.DB_PASSWORD
    name = settings.DB_NAME
    uri = f"{driver}://{user}:{password}@{host}:{port}/{name}"
    return uri
    
def get_uri():
    """
    Get the database URI.
    """
 
    env = settings.APP_ENV
    if env == "development":
        uri = get_sqlite_uri()
    elif env == "production":
        driver = settings.DB_DRIVER
        if driver == "postgresql":
            uri = get_postgresql_uri()
        else:
            raise Exception("Unknown driver: %s" % driver)
    else:
        raise Exception("Unknown environment: %s" % env)
    return uri
