import bcrypt

def verify_password(plain_password: str, hashed_password: str):
    """
    Compare a given password with another one stored in the database.
    """
    it_matches = bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
    return it_matches