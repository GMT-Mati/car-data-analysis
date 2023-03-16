from mysql.connector.errors import ProgrammingError
from .connection import get_database_connection
from datetime import datetime

# This code defines several functions for interacting with the MySQL database.
# The create_tables function creates the necessary database tables if they don't already exist.
# The save_listings function saves a list of listings to the listings table.
# The save_scraping_session function saves a scraping session to the scraping_sessions table.
# The get_latest_scraping_session function retrieves the latest scraping session from
# the scraping_sessions table.


def create_tables():
    """Create the necessary database tables if they don't already exist"""
    with get_database_connection() as cnx:
        cursor = cnx.cursor()

        # Create the listings table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS listings (
                id INT(11) NOT NULL AUTO_INCREMENT,
                title VARCHAR(255),
                url VARCHAR(255),
                price INT(11),
                year INT(11),
                mileage INT(11),
                fuel VARCHAR(255),
                location VARCHAR(255),
                posted_at DATETIME,
                PRIMARY KEY (id)
            )
            """
        )

        # Create the scraping_sessions table
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS scraping_sessions (
                id INT(11) NOT NULL AUTO_INCREMENT,
                started_at DATETIME,
                ended_at DATETIME,
                PRIMARY KEY (id)
            )
            """
        )

        cnx.commit()


def save_listings(listings):
    """Save a list of listings to the database"""
    with get_database_connection() as cnx:
        cursor = cnx.cursor()

        for listing in listings:
            # Insert the listing into the listings table
            query = """
                INSERT INTO listings
                    (title, url, price, year, mileage, fuel, location, posted_at)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (listing['title'], listing['url'], listing['price'], listing['year'],
                      listing['mileage'], listing['fuel'], listing['location'], listing['posted_at'])
            cursor.execute(query, values)

        cnx.commit()


def save_scraping_session(started_at, ended_at):
    """Save a scraping session to the database"""
    with get_database_connection() as cnx:
        cursor = cnx.cursor()

        # Insert the scraping session into the scraping_sessions table
        query = """
            INSERT INTO scraping_sessions
                (started_at, ended_at)
            VALUES
                (%s, %s)
        """
        values = (started_at, ended_at)
        cursor.execute(query, values)

        cnx.commit()


def get_latest_scraping_session():
    """Get the latest scraping session from the database"""
    with get_database_connection() as cnx:
        cursor = cnx.cursor()

        # Query the scraping_sessions table for the latest session
        query = """
            SELECT * FROM scraping_sessions
            ORDER BY ended_at DESC
            LIMIT 1
        """
        cursor.execute(query)

        result = cursor.fetchone()
        if result:
            return {
                'id': result[0],
                'started_at': result[1],
                'ended_at': result[2]
            }
        else:
            return None
