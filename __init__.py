"""
The app package contains the main modules for the application.
"""

__version__ = '1.0.0'

# Import main modules
from .scraper.otomoto_scraper import OtomotoScraper
from .database.mysql_db import MySQLDatabase
from .data_processing.data_cleaning import clean_data
from .data_processing.data_transform import transform_data
from .data_processing.data_structuring import structure_data
from .export.csv_exporter import CSVExporter
from .import.csv_importer import CSVImporter
from .analysis.data_visualization import visualize_data
from .analysis.statistical_analysis import analyze_data
from .gui.app_gui import AppGUI
from .security.auth import authenticate, authorize
from .security.encryption import encrypt, decrypt
from .security.secure_protocol import secure_protocol

# Set up logging
import logging
logging.basicConfig(level=logging.INFO)

# Set up global app configuration
from . import config
