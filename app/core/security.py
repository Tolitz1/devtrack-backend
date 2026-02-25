import bcrypt

BCRYPT_ROUNDS = 12  # good default security level

def hash_password(password: str) -> str:
    # """
    # Hash plain password before storing in DB.
    # """
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=BCRYPT_ROUNDS)
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # """
    # Verify password during login.
    # """
    return bcrypt.checkpw(
        plain_password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )