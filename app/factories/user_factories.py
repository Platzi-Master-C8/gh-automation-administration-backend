import factory

from app.core import settings
from app.models import User


class SuperadminUserFactory(factory.Factory):
    """
    Class representing a superadmin user factory.
    Take data from settings and create admin user.
    """
    class Meta:
        model = User

    
    role_id = settings.FIRST_ADMIN_ROLE_ID
    email = settings.FIRST_ADMIN_EMAIL
    password = settings.FIRST_ADMIN_PASSWORD
    
    
    
class RandomUserFactory(factory.Factory):
    """
    Class representing a random user factory.
    Use random data to create random user.
    By default password is fixed to `password`.
    """
    class Meta:
        model = User


    name = factory.Faker("name")
    email = factory.Faker("free_email")
    password = "password"
    role_id = factory.Faker(
        "pyint",
        min_value=1,
        max_value=settings.DB_POPULATION
    )
