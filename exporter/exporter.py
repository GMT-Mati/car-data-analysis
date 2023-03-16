import tkinter as tk
from tkinter import filedialog
from ..database.utils import export_to_csv, import_from_csv

# This code defines a GUI for exporting and importing listings to and from a CSV file.
# The GUI has two buttons, one for exporting listings and one for importing listings.
# The export_to_csv function is called when the user clicks the "Export" button,
# and the import_from_csv function is called when the user clicks the "Import" button.#
# The ExporterGUI class initializes the GUI and creates the two buttons.
# The export_to_csv and import_from_csv methods prompt the user for a filename
# using the filedialog module, and then call the export_to_csv and import_from_csv functions
# from the database.utils module, passing the filename as an argument.
# If the export or import is successful, a message box is displayed to inform the user.#
# Finally, the run_exporter_gui function creates an instance of the ExporterGUI class
# and runs the GUI loop using root.mainloop().


class ExporterGUI:
    """A GUI for exporting and importing listings to and from a CSV file"""

    def __init__(self, master):
        self.master = master
        master.title("Exporter")

        # Create the "Export" button
        self.export_button = tk.Button(
            master,
            text="Export to CSV",
            command=self.export_to_csv
        )
        self.export_button.pack()

        # Create the "Import" button
        self.import_button = tk.Button(
            master,
            text="Import from CSV",
            command=self.import_from_csv
        )
        self.import_button.pack()

    def export_to_csv(self):
        """Export the listings to a CSV file"""
        filename = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            title="Export Listings"
        )
        if filename:
            export_to_csv(filename)
            tk.messagebox.showinfo(
                "Export Complete",
                f"The listings have been exported to {filename}."
            )

    def import_from_csv(self):
        """Import listings from a CSV file"""
        filename = filedialog.askopenfilename(
            filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")],
            title="Import Listings"
        )
        if filename:
            import_from_csv(filename)
            tk.messagebox.showinfo(
                "Import Complete",
                f"The listings have been imported from {filename}."
            )


def run_exporter_gui():
    """Run the exporter GUI"""
    root = tk.Tk()
    gui = ExporterGUI(root)
    root.mainloop()
