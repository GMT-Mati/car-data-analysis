import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect("cars.db")
        self.c = self.conn.cursor()

        self.c.execute("""CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price INTEGER,
            year INTEGER,
            mileage INTEGER,
            location TEXT
        )""")

    def add_car(self, title, price, year, mileage, location):
        self.c.execute("INSERT INTO cars (title, price, year, mileage, location) VALUES (?, ?, ?, ?, ?)",
                       (title, price, year, mileage, location))
        self.conn.commit()

    def get_cars(self):
        self.c.execute("SELECT * FROM cars")
        return self.c.fetchall()

    def delete_all_cars(self):
        self.c.execute("DELETE FROM cars")
        self.conn.commit()

    def __del__(self):
        self.conn.close()
