import tkinter as tk
from tkinter import ttk
from typing import List


class Utils:
    @staticmethod
    def create_label(parent, text: str, row: int, column: int, **kwargs):
        label = ttk.Label(parent, text=text, **kwargs)
        label.grid(row=row, column=column, padx=5, pady=5, sticky='w')
        return label

    @staticmethod
    def create_entry(parent, row: int, column: int, **kwargs):
        entry = ttk.Entry(parent, **kwargs)
        entry.grid(row=row, column=column, padx=5, pady=5, sticky='w')
        return entry

    @staticmethod
    def create_dropdown(parent, values: List[str], row: int, column: int, **kwargs):
        dropdown = ttk.Combobox(parent, values=values, **kwargs)
        dropdown.grid(row=row, column=column, padx=5, pady=5, sticky='w')
        return dropdown

    @staticmethod
    def crate_button(parent, text: str, row: int, column: int, command=None, **kwargs):
        button = ttk.Button(parent, text=text, command=command, **kwargs)
        button.grid(row=row, column=column, padx=5, pady=5, sticky='w')
        return button

    @staticmethod
    def crate_scroller(parent, row: int, column: int, **kwargs):
        scroller = ttk.Scrollbar(parent, **kwargs)
        scroller.grid(row=row, column=column, sticky='nsew')
        return scroller

    @staticmethod
    def create_listbox(parent, row: int, column: int,  **kwargs):
        listbox = tk.Listbox(parent, **kwargs)
        listbox.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        return listbox

    @staticmethod
    def create_text(parent, row: int, column: int, **kwargs):
        text = tk.Text(parent, **kwargs)
        text.grid(row=row, column=column, padx=5, pady=5, sticky='nsew')
        return text
