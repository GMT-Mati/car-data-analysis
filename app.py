from scraper.scraper import scrape_data
from database.connection import create_db_connection
from exporter.exporter import export_data_to_csv
from reader.reader import read_csv_file
from analyzer.analyzer import analyze_data
from gui.main import run_gui

# Define the entry point for the app
def main():
    # Scrape data from otomoto.pl
    data = scrape_data()

    # Create a database connection
    db_conn = create_db_connection()

    # Save the scraped data to the database
    db_conn.save_data(data)

    # Export the data from the database to a CSV file
    export_data_to_csv(db_conn)

    # Read the CSV file
    csv_data = read_csv_file()

    # Analyze the data
    analyzed_data = analyze_data(csv_data)

    # Start the GUI
    run_gui(analyzed_data)

if __name__ == '__main__':
    main()
