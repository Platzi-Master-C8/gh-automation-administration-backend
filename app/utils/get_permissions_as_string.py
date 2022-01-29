from typing import List

from app.models import Permission


def get_permissions_as_string(permissions: List[Permission]) -> str:
    """
    Convert a list of permissions to a string.
    """
    permissions_string = ",".join(map(lambda x: str(x.permission_name), permissions))
    return permissions_string