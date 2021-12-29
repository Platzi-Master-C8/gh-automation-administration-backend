import bcrypt


def hash_password(password: str) -> str:
    """
    Hash a given password.
    """

    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    return hashed_password.decode("utf-8")
