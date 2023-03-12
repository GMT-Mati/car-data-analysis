import tkinter as tk
from tkinter import filedialog
import OtomotoScraper
import OtomotoAnalyzer

# This GUI allows the user to upload the Otomoto car dataset in CSV format,
# analyze the dataset using the OtomotoAnalyzer class,
# and display the results of the analysis in a label widget.

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Otomoto Car Dataset Analyzer')
        self.geometry('500x400')
        self.file_path = ''
        self.dataset = None
        self.analyzer = OtomotoAnalyzer()

        # create widgets

        self.upload_btn = tk.Button(self, text='Upload Dataset', command=self.upload_dataset)
        self.analyze_btn = tk.Button(self, text='Analyze Dataset', command=self.analyze_dataset)
        self.results_lbl = tk.Label(self, text='Results will be displayed here.')

        # add widgets to window

        self.upload_btn.pack(pady=10)
        self.analyze_btn.pack(pady=10)
        self.results_lbl.pack(pady=10)

    def upload_dataset(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.dataset = OtomotoScraper.read_csv(self.file_path)
            self.results_lbl.config(text='Dataset uploaded successfully.')

    def analyze_dataset(self):
        if self.dataset:
            results = self.analyzer.analyze(self.dataset)
            self.display_results(results)
        else:
            self.results_lbl.config(text='Please upload a dataset first.')

    def display_results(self, results):
        self.results_lbl.config(text=results)


if __name__ == '__main__':
    app = App()
    app.mainloop()
