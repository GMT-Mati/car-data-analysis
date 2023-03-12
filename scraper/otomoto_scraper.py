"""
The otomoto_scraper module contains the OtomotoScraper class for scraping data from the otomoto.pl website.
"""

import requests
from bs4 import BeautifulSoup


class OtomotoScraper:
    def __init__(self):
        self.url = 'https://www.otomoto.pl/osobowe'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    def get_page(self, page_number):
        """
        Fetches the HTML content of the specified page from otomoto.pl.
        """
        params = {'page': page_number}
        response = requests.get(self.url, headers=self.headers, params=params)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    def get_car_data(self, car):
        """
        Extracts the relevant data from the HTML content of a single car listing.
        """
        title = car.find('a', {'class': 'offer-title__link'}).text.strip()
        price = car.find('span', {'class': 'offer-price__number ds-price-number'}).text.strip()
        year = car.find('li', {'class': 'offer-item__params-item'}).text.strip()
        mileage = car.find_all('li', {'class': 'offer-item__params-item'})[1].text.strip()
        fuel_type = car.find_all('li', {'class': 'offer-item__params-item'})[2].text.strip()
        location = car.find('span', {'class': 'ds-location-city'}).text.strip()
        link = car.find('a', {'class': 'offer-title__link'})['href']
        return {'Title': title, 'Price': price, 'Year': year, 'Mileage': mileage, 'Fuel Type': fuel_type,
                'Location': location, 'Link': link}

    def scrape(self, num_pages):
        """
        Scrapes the specified number of pages from otomoto.pl and returns a list of car data dictionaries.
        """
        all_cars = []
        for page_num in range(1, num_pages + 1):
            soup = self.get_page(page_num)
            cars = soup.find_all('div', {'class': 'offer-item__wrapper'})
            for car in cars:
                car_data = self.get_car_data(car)
                all_cars.append(car_data)
        return all_cars
