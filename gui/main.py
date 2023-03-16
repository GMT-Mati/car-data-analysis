import tkinter as tk
import tkinter.ttk as ttk
import threading
from app.scraper.scraper import Scraper
from app.database.connection import db
from app.exporter.exporter import Exporter
from app.reader.reader import Reader
from app.analyzer.analyzer import Analyzer
from app.security.authentication import authenticate_user


class AppGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Otomoto Scraper")
        self.master.geometry("500x300")
        self.create_widgets()

    def create_widgets(self):
        # create labels
        self.search_label = tk.Label(self.master, text="Search:")
        self.search_label.grid(row=0, column=0, sticky="W")

        self.make_label = tk.Label(self.master, text="Make:")
        self.make_label.grid(row=1, column=0, sticky="W")

        self.model_label = tk.Label(self.master, text="Model:")
        self.model_label.grid(row=2, column=0, sticky="W")

        self.year_label = tk.Label(self.master, text="Year:")
        self.year_label.grid(row=3, column=0, sticky="W")

        # create search entry
        self.search_entry = tk.Entry(self.master)
        self.search_entry.grid(row=0, column=1, pady=5)

        # create make dropdown
        makes = ["", "Audi", "BMW", "Mercedes-Benz", "Volkswagen"]
        self.make_var = tk.StringVar()
        self.make_var.set("")
        self.make_dropdown = ttk.Combobox(self.master, textvariable=self.make_var, values=makes)
        self.make_dropdown.grid(row=1, column=1, pady=5)

        # create model entry
        self.model_entry = tk.Entry(self.master)
        self.model_entry.grid(row=2, column=1, pady=5)

        # create year entry
        self.year_entry = tk.Entry(self.master)
        self.year_entry.grid(row=3, column=1, pady=5)

        # create buttons
        self.scrape_button = tk.Button(self.master, text="Scrape", command=self.scrape)
        self.scrape_button.grid(row=4, column=0, pady=10)

        self.export_button = tk.Button(self.master, text="Export to CSV", command=self.export)
        self.export_button.grid(row=4, column=1, pady=10)

        self.analyze_button = tk.Button(self.master, text="Analyze", command=self.analyze)
        self.analyze_button.grid(row=4, column=2, pady=10)

        # create status label
        self.status_label = tk.Label(self.master, text="")
        self.status_label.grid(row=5, column=0, columnspan=3)

    def scrape(self):
        # authenticate user before scraping data
        if not authenticate_user():
            self.status_label.config(text="Authentication failed.")
            return

        # retrieve search filters
        search_filter = {}
        search_filter["search"] = self.search_entry.get()
        search_filter["make"] = self.make_var.get()
        search_filter["model"] = self.model_entry.get()
        search_filter["year"] = self.year_entry.get()

        # run scraper in a separate thread
        t = threading.Thread(target=self.run_scraper, args=(search_filter,))
        t.start()

    def run_scraper(self, search_filter):
        try:
            scraper = Scraper(search_filter)
        scraper.run()
        self.status_label.config(text="Scraping completed successfully.")
        except:
        self.status_label.config(text="Error occurred during scraping.")

    def export(self):
        # authenticate user before exporting data
        if not authenticate_user():
            self.status_label.config(text="Authentication failed.")
            return

        # create Exporter object and run export in a separate thread
        t = threading.Thread(target=self.run_export)
        t.start()

    def run_export(self):
        try:
            exporter = Exporter(db)
            exporter.export_to_csv()
            self.status_label.config(text="Exporting completed successfully.")
        except:
            self.status_label.config(text="Error occurred during exporting.")

    def analyze(self):
        # authenticate user before analyzing data
        if not authenticate_user():
            self.status_label.config(text="Authentication failed.")
            return

        # create Reader and Analyzer objects and run analysis in a separate thread
        t = threading.Thread(target=self.run_analyze)
        t.start()

    def run_analyze(self):
        try:
            reader = Reader(db)
            analyzer = Analyzer(reader.read_all())
            results = analyzer.analyze()
            self.status_label.config(text=f"Analysis completed successfully.\n{results}")
        except:
            self.status_label.config(text="Error occurred during analysis.")
