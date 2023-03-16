import csv
from .models import save_listings

# This code defines two functions for importing and exporting listings to and from a CSV file.
# The export_to_csv function exports the listings from the listings table in the database to a CSV file.
# The import_from_csv function imports listings from a CSV file into the listings table in the database.


def export_to_csv(filename):
    """Export the listings from the database to a CSV file"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow([
            'Title',
            'URL',
            'Price',
            'Year',
            'Mileage',
            'Fuel',
            'Location',
            'Posted At'
        ])

        # Query the listings table and write each row to the CSV file
        with get_database_connection() as cnx:
            cursor = cnx.cursor()
            query = "SELECT * FROM listings"
            cursor.execute(query)

            for row in cursor.fetchall():
                writer.writerow(row[1:])  # Skip the ID column


def import_from_csv(filename):
    """Import listings from a CSV file into the database"""
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)

        # Skip the header row
        next(reader)

        # Create a list of dictionaries representing each row in the CSV file
        listings = []
        for row in reader:
            listing = {
                'title': row[0],
                'url': row[1],
                'price': int(row[2]),
                'year': int(row[3]),
                'mileage': int(row[4]),
                'fuel': row[5],
                'location': row[6],
                'posted_at': row[7],
            }
            listings.append(listing)

        # Save the listings to the database
        save_listings(listings)
