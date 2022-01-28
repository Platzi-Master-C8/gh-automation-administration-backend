from typing import List

from app.models import Permission


def get_permissions_as_string(permissions: List[Permission]) -> str:
    """
    Convert a list of permissions to a string.
    """
    permissions_string = ""
    for permission in permissions:
        permissions_string += permission.permission_name + ","
    return permissions_string[:-1]
