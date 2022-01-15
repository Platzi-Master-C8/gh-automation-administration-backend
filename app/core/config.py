import os

from dotenv import load_dotenv


load_dotenv()


class Settings():
    """
    Class representing a settings object.
    Set a couple of environment variables to configure the application.
    """
    # Application
    APP_NAME: str = os.getenv("APP_NAME")
    APP_PORT: str = os.getenv("APP_PORT")
    APP_ENV: str = os.getenv("APP_ENV")

    # Database
    DB_DRIVER: str = os.getenv("DB_DRIVER")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_RESET: bool = bool(os.getenv("DB_RESET"))
    DB_POPULATE: bool = bool(os.getenv("DB_POPULATE"))
    DB_POPULATION: int = int(os.getenv("DB_POPULATION"))

    # First administrator
    FIRST_ADMIN_ROLE_ID: str = os.getenv("FIRST_ADMIN_ROLE_ID")
    FIRST_ADMIN_EMAIL: str = os.getenv("FIRST_ADMIN_EMAIL")
    FIRST_ADMIN_PASSWORD: str = os.getenv("FIRST_ADMIN_PASSWORD")

    # Access Token
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM', 'HS256')
    EXPIRE_MINUTES: int = int(os.getenv('EXPIRE_MINUTES', '15'))


settings = Settings()
"""
Contain the application settings.
"""
