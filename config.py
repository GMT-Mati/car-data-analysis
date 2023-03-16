import os

# This code simply imports the get_database_connection function from app/database/db.py
# and exposes it as part of the app.database module.


class Config:
    # Database configuration
    DATABASE_URI = os.getenv('DATABASE_URI', 'mysql://user:password@localhost/db_name')
    DATABASE_TABLE_NAME = 'car_data'

    # CSV export configuration
    CSV_FILENAME = 'car_data.csv'
    CSV_DELIMITER = ';'
    CSV_QUOTECHAR = '"'

    # GUI configuration
    GUI_TITLE = 'Car Data Analyzer'

    # Security configuration
    SECRET_KEY = os.getenv('SECRET_KEY', 'replace-with-a-secure-secret-key')
