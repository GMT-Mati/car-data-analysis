import csv

# This code defines the read_csv function, which reads a CSV file specified by the filename argument
# and returns a list of dictionaries. The function uses the csv.DictReader object to read the file,
# which automatically maps each row to a dictionary with keys based on the header row of the CSV file.
# Each dictionary represents a single row of data in the CSV file,
# and the list of dictionaries returned by the function represents all the data in the file.


def read_csv(filename):
    """Read a CSV file and return a list of dictionaries"""
    rows = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows
