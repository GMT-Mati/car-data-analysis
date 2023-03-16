from collections import Counter
from app.reader import read_csv
from app.reader.utils import calculate_age

# This code defines the analyze_data function, which takes a filename of a CSV file containing car listing data
# and analyzes the data to produce a dictionary of results.
# The function uses the read_csv function from the reader package to read the data from the CSV file
# into a list of dictionaries. It then uses the collections.Counter class to count the number of listings
# by make and model, and calculates the average age of the cars by using the calculate_age function
# from the reader.utils module.
# Finally, it calculates the average price of the cars by make and model, and returns the results as a dictionary.


def analyze_data(filename):
    """Analyze data from a CSV file and return a dictionary of results"""
    # Read data from CSV file
    data = read_csv(filename)

    # Count number of listings by make and model
    counts = Counter((row['make'], row['model']) for row in data)
    make_model_counts = [{'make': make, 'model': model, 'count': count}
                         for (make, model), count in counts.items()]

    # Calculate average age of cars
    ages = [calculate_age(row['year']) for row in data]
    avg_age = sum(ages) / len(ages)

    # Calculate average price of cars by make and model
    prices = {}
    for row in data:
        make_model = (row['make'], row['model'])
        if make_model not in prices:
            prices[make_model] = []
        prices[make_model].append(int(row['price']))
    avg_prices = [{'make': make, 'model': model, 'avg_price': sum(prices) / len(prices)}
                  for (make, model), prices in prices.items()]

    # Return dictionary of results
    return {'make_model_counts': make_model_counts,
            'avg_age': avg_age,
            'avg_prices': avg_prices}
