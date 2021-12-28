import os

from dotenv import load_dotenv


load_dotenv()


class Settings():
    FIRST_ADMIN_ROLE_ID: str = os.getenv('FIRST_ADMIN_ROLE_ID')
    FIRST_ADMIN_EMAIL: str = os.getenv('FIRST_ADMIN_EMAIL')
    FIRST_ADMIN_PASSWORD: str = os.getenv('FIRST_ADMIN_PASSWORD')


settings = Settings()
