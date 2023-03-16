# app/gui/__init__.py

from tkinter import *

# This creates a simple GUI class that initializes a blank window with a title of "App Name".
# You can add your own GUI elements to the __init__ method as needed.


class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("App Name")

        # TODO: Add GUI elements here
