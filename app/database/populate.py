from app.factories import AdministratorRoleFactory
from app.factories import IndividualRoleFactory
from app.factories import OrganizationRoleFactory
from app.factories import RandomPermissionFactory
from app.factories import RandomRoleFactory
from app.factories import RandomUserFactory
from app.factories import SuperadminUserFactory
from app.resources import permissions
from app.resources import roles
from app.resources import users


def populate_permissions(quantity: int)-> None:
    """
    Populate the database with specified quantity of permissions.
    """
    random_permissions = RandomPermissionFactory.create_batch(quantity)
    for permission in random_permissions:
        permissions.create(permission, 1)
    print("DEBUG:   ", f"{quantity} permissions created.")

def populate_roles(quantity: int) -> None:
    """
    Populate the database with specified quantity of roles.
    """
    administrator_role = AdministratorRoleFactory.create()
    individual_role = IndividualRoleFactory.create()
    organization_role = OrganizationRoleFactory.create()
    roles.create(administrator_role, 1)
    roles.create(individual_role, 1)
    roles.create(organization_role, 1)
    random_roles = RandomRoleFactory.create_batch(quantity - 3)
    for role in random_roles:
        roles.create(role, 1)
    print("DEBUG:   ", f"{quantity} roles created.")

def populate_users(quantity: int)-> None:
    """
    Populate the database with specified quantity of users.
    First, create a superadmin user and then create the rest of the users.
    """
    superadmin = SuperadminUserFactory.create()
    users.create(superadmin, 1)
    random_users = RandomUserFactory.create_batch(quantity - 1)
    for user in random_users:
        users.create(user, 1)
    print("DEBUG:   ", f"{quantity} users created.")
