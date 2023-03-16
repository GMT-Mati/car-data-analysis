import tkinter as tk
from gui.widgets import HeaderLabel, SubheaderLabel, DataEntry, DataDisplay


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Car Data Analysis")
        self.geometry("800x600")

        # Add header label
        header_label = HeaderLabel(self, text="Car Data Analysis")
        header_label.pack(pady=10)

        # Add subheader label
        subheader_label = SubheaderLabel(self, text="Enter search criteria below")
        subheader_label.pack(pady=5)

        # Add data entry widgets
        make_entry = DataEntry(self, label_text="Make:")
        make_entry.pack()
        model_entry = DataEntry(self, label_text="Model:")
        model_entry.pack()
        year_entry = DataEntry(self, label_text="Year:")
        year_entry.pack()
        location_entry = DataEntry(self, label_text="Location:")
        location_entry.pack()
        max_price_entry = DataEntry(self, label_text="Max Price:")
        max_price_entry.pack()

        # Add data display widget
        data_display = DataDisplay(self)
        data_display.pack(pady=10)

        # Add button to initiate search
        search_button = tk.Button(self, text="Search", command=lambda: self.search_cars(
            make_entry.get_text(),
            model_entry.get_text(),
            year_entry.get_text(),
            location_entry.get_text(),
            max_price_entry.get_text(),
            data_display
        ))
        search_button.pack(pady=10)

    def search_cars(self, make, model, year, location, max_price, data_display):
        # Placeholder function for searching cars, replace with actual implementation
        data_display.set_text(f"Searching for {make} {model} ({year}) in {location} with a max price of {max_price}...")
