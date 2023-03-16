import tkinter as tk
from tkinter import filedialog, messagebox

class MainView:
    def __init__(self, scraper, exporter, reader, analyzer):
        self.scraper = scraper
        self.exporter = exporter
        self.reader = reader
        self.analyzer = analyzer

        self.root = tk.Tk()
        self.root.title("Otomoto Scraper")
        self.root.geometry("400x400")

        self.search_label = tk.Label(self.root, text="Search:")
        self.search_label.pack()

        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack()

        self.search_button = tk.Button(self.root, text="Scrape", command=self.scrape_data)
        self.search_button.pack()

        self.export_button = tk.Button(self.root, text="Export to CSV", command=self.export_data)
        self.export_button.pack()

        self.import_button = tk.Button(self.root, text="Import from CSV", command=self.import_data)
        self.import_button.pack()

        self.analyze_button = tk.Button(self.root, text="Analyze data", command=self.analyze_data)
        self.analyze_button.pack()

        self.root.mainloop()

    def scrape_data(self):
        search_query = self.search_entry.get()
        data = self.scraper.scrape(search_query)
        messagebox.showinfo("Scraping Complete", f"{len(data)} listings scraped.")

    def export_data(self):
        filename = filedialog.asksaveasfilename(defaultextension=".csv")
        if filename:
            self.exporter.export_to_csv(filename)
            messagebox.showinfo("Export Complete", f"Data exported to {filename}.")

    def import_data(self):
        filename = filedialog.askopenfilename(defaultextension=".csv")
        if filename:
            self.reader.read_csv(filename)
            messagebox.showinfo("Import Complete", f"Data imported from {filename}.")

    def analyze_data(self):
        data = self.reader.get_data()
        result = self.analyzer.analyze(data)
        messagebox.showinfo("Analysis Complete", result)
