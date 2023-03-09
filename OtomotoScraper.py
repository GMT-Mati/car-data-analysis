import requests
from bs4 import BeautifulSoup
import pandas as pd


class OtomotoScraper:

    # The OtomotoScraper class takes the URL of the page to scrape as an argument when initialized.
    # The scrape() method is responsible for actually scraping the data from the page
    # and adding it to the self.data list.
    # The save_to_csv() method saves the scraped data to a CSV file,
    # and the load_from_csv() method loads the data from a CSV file into the self.data list.

    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/58.0.3029.110 Safari/537.3'})
        self.data = []

    def scrape(self):
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # scrape data from the page
        # add data to self.data list

    def save_to_csv(self, filename):
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)

    def load_from_csv(self, filename):
        df = pd.read_csv(filename)
        self.data = df.to_dict('records')