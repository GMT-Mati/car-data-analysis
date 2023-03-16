from flask import g, request, session

from app.security.authentication import authenticate

# This module defines several utility functions for working with authentication and authorization.#
# The login function takes a username and password, authenticates the user,
# and logs them in by setting the user_id key in the session.
# It returns True if the login was successful, and False otherwise.#
# The logout function logs the user out by clearing the session.#
# The get_current_user function sets the g.user object to the current authenticated user based on
# the user_id key in the session. If the user_id key is not set, g.user is set to None.#
# The require_login decorator is used to require authentication to access a view.
# If the user is not authenticated, they are redirected to the login page.#
# Note that this implementation is just an example and may need to be adapted to the specific requirements
# of your application.


def login(username: str, password: str):
    """Authenticate the user and log them in"""
    user = authenticate(username, password)
    if not user:
        return False
    session.clear()
    session['user_id'] = user['id']
    return True


def logout():
    """Log the user out"""
    session.clear()


def get_current_user():
    """Get the current authenticated user"""
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        db = get_db()
        g.user = db.execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


def require_login(view):
    """Decorator to require authentication to access a view"""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view
