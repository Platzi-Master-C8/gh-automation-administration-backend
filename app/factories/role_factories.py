import factory
from faker import Faker

from app.models import Role


fake = Faker()


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
