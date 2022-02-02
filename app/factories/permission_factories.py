import factory

from app.models import Permission
from app.utils import get_permission_name


class RandomPermissionFactory(factory.Factory):
    """
    Class representing a random permission factory.
    Use random data to create random permission.
    The crated permissions follow the next rules:
    `can-{action}-{scope}-{resource}`
    """
    class Meta:
        model = Permission


    permission_name = factory.LazyFunction(get_permission_name)
    permission_description = factory.Faker("text", max_nb_chars=80)
