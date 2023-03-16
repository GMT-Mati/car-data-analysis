import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd
from datetime import datetime
import mysql.connector
from mysql.connector import errorcode
from app.config import Config


class Scraper:
    def __init__(self):
        self.base_url = 'https://www.otomoto.pl/osobowe'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        self.params = {
            'search%5Border%5D': 'created_at%3Adesc',
            'search%5Bbrand_program_id%5D[0]': '42',  # show only offers from verified dealers
            'page': 1  # start from the first page
        }
        self.df = pd.DataFrame()

        # Set up MySQL database connection
        try:
            self.db_connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='password',
                database='car_data'
            )
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your username or password")
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(error)
            exit(1)

    def scrape(self):
        while True:
            # Make a request to the current page
            response = requests.get(self.base_url, headers=self.headers, params=self.params)

            # Parse the HTML content of the response with BeautifulSoup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the car offer details from the HTML
            offers = soup.find_all('div', {'class': 'offer-item__content'})

            # Check if there are any offers left on the page
            if not offers:
                break

            # Process each car offer and add it to the DataFrame
            for offer in offers:
                title = offer.find('a', {'class': 'offer-title__link'}).text
                url = offer.find('a', {'class': 'offer-title__link'})['href']
                price = offer.find('span', {'class': 'offer-price__number'}).text
                price = int(re.sub(r'\s+', '', price))  # remove spaces and convert to int

                # Check if the offer includes the year of production
                year = offer.find('li', {'data-code': 'year'}).text.strip()
                if not year:
                    continue  # skip offers without a year of production

                # Parse the year of production from the offer
                year = int(year.split('/')[-1])

                # Extract other offer details if available
                mileage = offer.find('li', {'data-code': 'mileage'}).text.strip()
                if mileage:
                    mileage = int(re.sub(r'\s+', '', mileage))  # remove spaces and convert to int
                fuel_type = offer.find('li', {'data-code': 'fuel_type'}).text.strip()
                engine_capacity = offer.find('li', {'data-code': 'engine_capacity'}).text.strip()
                power = offer.find('li', {'data-code': 'power'}).text.strip()
                transmission = offer.find('li', {'data-code': 'transmission'}).text.strip()
                # Add the offer details to the DataFrame
                row = pd.DataFrame({
                    'title': [title],
                    'year': [year],
                    'price': [price],
                    'mileage': [mileage],
                    'fuel_type': [fuel_type],
                    'engine_capacity': [engine_capacity],
                    'power': [power],
                    'transmission': [transmission],
                    'url': [url]
                })
                self.df = pd.concat([self.df, row])

            # Move to the next page
            self.params['page'] += 1

        # Save the DataFrame to a CSV file
        filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_car_data.csv"
        self.df.to_csv(filename, index=False)

        # Save the DataFrame to a MySQL database
        self.save_to_mysql()

    def save_to_mysql(self):
        # Create the table if it doesn't exist
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS car_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255) NOT NULL,
            year INT NOT NULL,
            price INT NOT NULL,
            mileage INT,
            fuel_type VARCHAR(255),
            engine_capacity VARCHAR(255),
            power VARCHAR(255),
            transmission VARCHAR(255),
            url VARCHAR(255) NOT NULL
        )'''
        with self.db_connection.cursor() as cursor:
            cursor.execute(create_table_query)

        # Insert the data into the table
        insert_query = '''
        INSERT INTO car_data (title, year, price, mileage, fuel_type, engine_capacity, power, transmission, url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        with self.db_connection.cursor() as cursor:
            for i, row in self.df.iterrows():
                values = (row['title'], row['year'], row['price'], row['mileage'], row['fuel_type'],
                          row['engine_capacity'], row['power'], row['transmission'], row['url'])
                cursor.execute(insert_query, values)
            self.db_connection.commit()

    def load_from_csv(self, filename):
        self.df = pd.read_csv(filename)

    def analyze_data(self):
        # Example analysis: calculate the average price of cars by year of production
        result = self.df.groupby('year').agg({'price': 'mean'})
        print(result)
