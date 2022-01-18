import factory
from faker import Faker

# from app.core import settings
# from app.factories import RandomPermissionFactory
from app.models import Role


fake = Faker()
# population = settings.DB_POPULATION

# random_permissions = RandomPermissionFactory().build_batch(population)
# """
# Group of instances of the `Permission` model.
# """

# def _get_permissions()->set:
#     """
#     Create a set of random permissions.
#     """
#     max_value = len(random_permissions)
#     permissions = set()
#     number_of_permissions = fake.pyint(1, max_value)
#     for _ in range(number_of_permissions):
#         index = fake.pyint(max_value - 1)
#         permissions.add(random_permissions[index])
#     return permissions


class AdministratorRoleFactory(factory.Factory):
    """
    Class representing the administrator role.
    """
    class Meta:
        model = Role

        
    role_name = "administrator"
    role_description = "Grant total control over the application."


class IndividualRoleFactory(factory.Factory):
    """
    Class representing the individual role.
    """
    class Meta:
        model = Role

    role_name = "individual"
    role_description = "Standard user with limited permissions."


class OrganizationRoleFactory(factory.Factory):
    """
    Class representing the organization role.
    """
    class Meta:
        model = Role

    role_name = "organization"
    role_description = "Oriented to talent searchers"


class RandomRoleFactory(factory.Factory):
    """
    Class representing a random role factory.
    Use random data to create random role. Attach random permissions to role.
    """
    class Meta:
        model = Role


    role_name = factory.Faker("word")
    role_description = factory.Faker("text", max_nb_chars=80)
    # permissions = factory.LazyFunction(_get_permissions())