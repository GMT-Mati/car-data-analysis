import csv

def read_csv_file(file_path):
    """
    Reads a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
    """
    rows = []
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)
    return rows
