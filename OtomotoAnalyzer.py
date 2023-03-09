import pandas as pd
import numpy as np

class OtomotoAnalyzer:

    # This class contains methods for performing various data analysis operations on the scraped data.

    def __init__(self, data):
        self.data = data

    def calculate_avg_price_mileage_age(self):
        avg_price = np.mean(self.data['price'])
        avg_mileage = np.mean(self.data['mileage'])
        avg_age = np.mean(self.data['age'])
        return avg_price, avg_mileage, avg_age

    def group_by_make_model_year(self):
        grouped = self.data.groupby(['make', 'model', 'year'])
        grouped_stats = grouped.agg(
            {'price': 'mean', 'mileage': 'mean', 'age': 'mean'}
        )
        return grouped_stats

    def group_by_fuel_type(self):
        grouped = self.data.groupby(['fuel type'])
        grouped_stats = grouped.agg(
            {'price': 'mean', 'mileage': 'mean'}
        )
        return grouped_stats

    def group_by_body_type(self):
        grouped = self.data.groupby(['body type'])
        grouped_stats = grouped.agg(
            {'price': 'mean', 'mileage': 'mean'}
        )
        return grouped_stats

    def calculate_transmission_percentage(self):
        total_cars = len(self.data)
        auto_cars = len(self.data[self.data['transmission'] == 'Automatic'])
        manual_cars = len(self.data[self.data['transmission'] == 'Manual'])
        auto_percentage = auto_cars / total_cars * 100
        manual_percentage = manual_cars / total_cars * 100
        return auto_percentage, manual_percentage

    def group_by_region(self):
        grouped = self.data.groupby(['region'])
        grouped_stats = grouped.agg(
            {'price': 'mean', 'mileage': 'mean'}
        )
        return grouped_stats

    def calculate_top_colors(self, n=10):
        top_colors = self.data['color'].value_counts().nlargest(n)
        return top_colors

    def calculate_safety_percentage(self):
        airbag_cars = len(self.data[self.data['airbag']])
        abs_cars = len(self.data[self.data['abs']])
        tc_cars = len(self.data[self.data['traction control']])
        total_cars = len(self.data)
        airbage_percentage = airbag_cars / total_cars * 100
        abs_percentage = abs_cars / total_cars * 100
        tc_percentage = tc_cars / total_cars * 100
        return airbage_percentage, abs_percentage, tc_percentage
