import factory
from faker import Faker

from app.core import settings
from app.models import Role
from app.database.factories.permission_factories import RandomPermissionFactory


fake = Faker()

random_permissions = RandomPermissionFactory().build_batch(
    settings.DB_POPULATION
)
"""
Group of instances of the `Permission` model.
"""

def _get_permissions():
    """
    Create a set of random permissions.
    """
    max_value = len(random_permissions)
    permissions = set()
    number_of_permissions = fake.pyint(1, max_value)
    for _ in range(number_of_permissions):
        index = fake.pyint(max_value - 1)
        permissions.add(random_permissions[index])
    return permissions


class RandomRoleFactory(factory.Factory):
    """
    Class representing a random role factory.
    Use random data to create random role. Attach random permissions to role.
    """
    class Meta:
        model = Role


    role_name = factory.Faker("word")
    role_description = factory.Faker("text", max_nb_chars=80)
    permissions = factory.LazyFunction(_get_permissions)
