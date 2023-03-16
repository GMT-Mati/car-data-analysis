import bcrypt

# This module defines two functions: encrypt_password and check_password.#
# The encrypt_password function encrypts a password using bcrypt by generating a random salt and hashing the password
# with that salt. The resulting hashed password is returned as bytes.#
# The check_password function checks if a given password matches a given hashed password by re-encrypting the password
# with the same salt used to hash the original password and comparing the resulting hashed password
# to the given hashed password. It returns True if the passwords match, and False otherwise.#
# Note that this implementation is just an example and may need to be adapted to the specific requirements
# of your application.


def encrypt_password(password: str) -> bytes:
    """Encrypt a password using bcrypt"""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password


def check_password(password: str, hashed_password: bytes) -> bool:
    """Check if a password matches a given hashed password"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
