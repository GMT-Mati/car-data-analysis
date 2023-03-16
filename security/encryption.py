import bcrypt


def hash_password(password):
    # Hash a password using bcrypt and return the hashed value
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password


def verify_password(password, hashed_password):
    # Verify that the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
