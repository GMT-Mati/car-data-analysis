import tkinter as tk


class HeaderLabel(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(font=("Helvetica", 24))


class SubheaderLabel(tk.Label):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.config(font=("Helvetica", 16))


class DataEntry(tk.Frame):
    def __init__(self, parent, label_text, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add label
        label = tk.Label(self, text=label_text)
        label.pack(side="left")

        # Add entry field
        self.entry = tk.Entry(self)
        self.entry.pack(side="left", padx=5)

    def get_text(self):
        return self.entry.get()


class DataDisplay(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Add label
        label = tk.Label(self, text="Search Results:")
        label.pack(pady=5)

        # Add text box
        self.text_box = tk.Text(self, height=20, width=70)
        self.text_box.pack()

    def set_text(self, text):
        self.text_box.delete("1.0", tk.END)
        self.text_box.insert(tk.END, text)
