def get_response_login(access_token: str, token_type: str = "bearer") -> dict:
    """
    Create the response data for a successful login attempt.
    """
    response_login = { "access_token": access_token, "token_type": token_type }
    return response_login
