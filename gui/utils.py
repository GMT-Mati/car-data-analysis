import tkinter.messagebox as messagebox
from security.authentication import authenticate


def show_error(message):
    """
    Shows an error message in a message box.
    """
    messagebox.showerror("Error", message)


def show_info(message):
    """
    Shows an info message in a message box.
    """
    messagebox.showinfo("Info", message)


def authenticated(func):
    """
    Decorator function that checks if the user is authenticated before executing
    a function.
    """
    def wrapper(*args, **kwargs):
        if not authenticate():
            show_error("Authentication failed.")
        else:
            func(*args, **kwargs)
    return wrapper
