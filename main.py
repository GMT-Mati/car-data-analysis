import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import threading
import OtomotoScraper
import OtomotoAnalyzer

# the main.py file creates an instance of the Application class, which is the main tkinter window for the app.
# The OtomotoScraper and OtomotoAnalyzer objects are also created and stored as attributes of the Application instance.
# The Application class contains methods for creating the GUI elements,
# starting the scraping process, and opening the data analysis window.
# The confirm_exit method is used to prompt the user to confirm before closing the app.
# This file is responsible


def create_widgets():

    # create GUI elements
    ...
    pass


class Application(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Otomoto Scraper & Analyzer")
        self.geometry("600x400")
        self.resizable(False, False)
        self.protocol('WM_DELETE_WINDOW', self.confirm_exit())
        self.scrap_thread = None

        # create GUI elements

        self.search_params = {
            'make': tk.StringVar(),
            'model': tk.StringVar(),
            'min_price': tk.StringVar(),
            'max_price': tk.StringVar(),
            'min_year': tk.StringVar(),
            'max_year': tk.StringVar(),
            'fuel_type': tk.StringVar(),
            'transmission': tk.StringVar(),
            'body_type': tk.StringVar()
        }
        create_widgets()

        # initialization database connection

        self.scraper = OtomotoScraper()
        self.analyzer = OtomotoAnalyzer()

    def start_scraping(self):

        # get search parameters from GUI

        make = self.search_params['make'].get()
        model = self.search_params['model'].get()
        min_price = self.search_params['min_price'].get()
        max_price = self.search_params['max_price'].get()
        min_year = self.search_params['min_year'].get()
        max_year = self.search_params['max_year'].get()
        fuel_type = self.search_params['fuel_type'].get()
        transmission = self.search_params['transmission'].get()
        body_type = self.search_params['body_type'].get()

        # check if all required parameters are filled

        if not make or not model or not fuel_type or not transmission or not body_type:
            messagebox.showerror('Error', 'Please fill in all required fields')
            return

        # create a new thread for scrapping
        self.scrap_thread = threading.Thread(
            target=self.scraper.scrape_cars,
            args=(make, model, min_price, max_price, min_year, max_year, fuel_type, transmission, body_type),
            daemon=True
        )
        self.scrap_thread.start()

    def analyze_data(self):

        # check if database is empty

        if not self.analyzer.check_data_exists():
            messagebox.showerror('Error', 'Please scrape data first')
            return

        # open a new window for data analysis

        analysis_window = tk.Toplevel(self)
        analysis_window.title('Otomoto Analyzer')
        analysis_window.geometry('800x600')
        analysis_window.resizable(False, False)

        # create analyzer object and pass the analysis window to it

        OtomotoAnalyzer(analysis_window)

    def confirm_exit(self):
        if messagebox.askyesno('Quit', 'Are you sure you want to quit'):
            self.destroy()


if __name__ == '__main__':
    app = Application()
    app.mainloop()
