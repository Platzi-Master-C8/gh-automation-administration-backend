import os

from dotenv import load_dotenv


load_dotenv()


class Settings():
    # Application
    APP_NAME = os.getenv("APP_NAME")
    APP_PORT = os.getenv("APP_PORT")
    APP_ENV = os.getenv("APP_ENV")

    # Database
    DB_DRIVER=os.getenv("DB_DRIVER")
    DB_HOST=os.getenv("DB_HOST")
    DB_PORT=os.getenv("DB_PORT")
    DB_USER=os.getenv("DB_USER")
    DB_PASSWORD=os.getenv("DB_PASSWORD")
    DB_NAME=os.getenv("DB_NAME")

    # First administrator
    FIRST_ADMIN_ROLE_ID: str = os.getenv("FIRST_ADMIN_ROLE_ID")
    FIRST_ADMIN_EMAIL: str = os.getenv("FIRST_ADMIN_EMAIL")
    FIRST_ADMIN_PASSWORD: str = os.getenv("FIRST_ADMIN_PASSWORD")

    # Access Token
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALGORITHM = os.getenv('ALGORITHM', 'HS256')
    EXPIRE_MINUTES = int(os.getenv('EXPIRE_MINUTES', '15'))


settings = Settings()
