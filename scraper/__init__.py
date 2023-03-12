"""
The scraper module contains the OtomotoScraper class for scraping data from the otomoto.pl website.
"""

from .otomoto_scraper import OtomotoScraper
import app.scraper

# Create a scraper instance
scraper = app.scraper.OtomotoScraper()
