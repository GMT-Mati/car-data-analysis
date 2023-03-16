from flask import abort, g

from app.database.connection import get_db

# This module defines two functions: authorize and is_admin.#
# The authorize function checks if the current user is authenticated by checking if the g.user object exists.
# If the g.user object does not exist, it raises a 401 Unauthorized error using Flask's abort function.#
# The is_admin function checks if the current user is an admin by looking up the user
# in the users table of the database using the get_db function from app/database/connection.py
# and checking if the is_admin column is set to True for that user.
# It returns True if the user is an admin, and False otherwise.#
# Note that this implementation is just an example and may need to be adapted to the specific requirements
# of your application.


def authorize():
    """Check if the current user is authorized to access the application"""
    if not g.user:
        abort(401)


def is_admin():
    """Check if the current user is an admin"""
    db = get_db()
    user = db.execute(
        'SELECT * FROM users WHERE id = ?', (g.user['id'],)
    ).fetchone()
    if user['is_admin']:
        return True
    else:
        return False
