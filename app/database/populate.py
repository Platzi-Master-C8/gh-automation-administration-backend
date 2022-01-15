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
        permissions.create(permission)
    print("DEBUG:   ", f"{quantity} random permissions created.")

def populate_roles(quantity: int) -> None:
    """
    Populate the database with specified quantity of roles.
    """
    random_roles = RandomRoleFactory.create_batch(quantity)
    for role in random_roles:
        roles.create(role)
    print("DEBUG:   ", f"{quantity} random roles created.")

def populate_users(quantity: int)-> None:
    """
    Populate the database with specified quantity of users.
    First, create a superadmin user and then create the rest of the users.
    """
    superadmin = SuperadminUserFactory.create()
    users.create(superadmin)
    print("DEBUG:   ", "Superadministrator user created.")
    random_users = RandomUserFactory.create_batch(quantity - 1)
    for user in random_users:
        users.create(user)
    print("DEBUG:   ", f"{quantity} random users created.")
