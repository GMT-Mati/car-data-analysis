import csv
from ..database.models import Listing

# This code defines two functions, export_to_csv and import_from_csv, which are used to export listings to a CSV file
# and import listings from a CSV file, respectively.#
# The export_to_csv function retrieves all listings from the database using the Listing.select() method
# and writes them to a CSV file specified by the filename argument.
# The function uses the csv.writer object to write the listings to the file,
# starting with the header row and then writing each listing as a row of values.#
# The import_from_csv function reads listings from a CSV file specified by the filename argument
# and adds them to the database using the Listing model.
# The function uses the csv.reader object to read the listings from the file, skipping the header row.
# For each row of values, the function creates a new Listing object with the values
# and saves it to the database using the save() method.


def export_to_csv(filename):
    """Export the listings to a CSV file"""
    listings = Listing.select()
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Make', 'Model', 'Year', 'Mileage', 'Price', 'Location', 'URL'])
        for listing in listings:
            writer.writerow([
                listing.make,
                listing.model,
                listing.year,
                listing.mileage,
                listing.price,
                listing.location,
                listing.url
            ])


def import_from_csv(filename):
    """Import listings from a CSV file"""
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            make, model, year, mileage, price, location, url = row
            listing = Listing(
                make=make,
                model=model,
                year=int(year),
                mileage=int(mileage),
                price=int(price),
                location=location,
                url=url
            )
            listing.save()
