from werkzeug.security import check_password_hash, generate_password_hash

from app.database.connection import get_db

# This module defines two functions: authenticate and create_user.#
# The authenticate function takes a username and password as arguments,
# looks up the user in the users table of the database using the get_db function from app/database/connection.py,
# and returns the user if the username and password match the stored user's credentials.
# It uses the check_password_hash function
# from werkzeug.security to check the hashed password against the provided password.
# The create_user function takes a username and password as arguments,
# inserts a new user into the users table of the database with the provided username
# and a hashed password using the generate_password_hash function from werkzeug.security.
# It then commits the changes to the database.
# Note that this implementation is just an example and
# may need to be adapted to the specific requirements of your application.


def authenticate(username, password):
    """Check if a username and password match a user in the database"""
    db = get_db()
    user = db.execute(
        'SELECT * FROM users WHERE username = ?', (username,)
    ).fetchone()
    if user and check_password_hash(user['password'], password):
        return user


def create_user(username, password):
    """Create a new user with the given username and password"""
    db = get_db()
    db.execute(
        'INSERT INTO users (username, password) VALUES (?, ?)',
        (username, generate_password_hash(password))
    )
    db.commit()
