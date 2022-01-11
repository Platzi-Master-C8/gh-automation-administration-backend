from app.core import settings


def get_first_admin_data():
    """
    Get first admin data from settings.
    This data is used to create first admin user and are setted in `.env` file.
    """

    return {
        "role_id": settings.FIRST_ADMIN_ROLE_ID,
        "email": settings.FIRST_ADMIN_EMAIL,
        "password": settings.FIRST_ADMIN_PASSWORD,
    }

superuser = get_first_admin_data()
