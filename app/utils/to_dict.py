from pydantic import BaseModel


def to_dict(obj: any) -> dict:
    """
    Convert an object to a dictionary.
    """

    if obj is None:
        return {}
    if isinstance(obj, dict):
        return obj
    if isinstance(obj, BaseModel):
        return obj.dict(exclude_unset=True)
    if isinstance(obj, list):
        return [to_dict(item) for item in obj]
    if hasattr(obj, "__dict__"):
        return to_dict(obj.__dict__)
    return obj
