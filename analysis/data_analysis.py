from .csv_reader import read_csv_file

def get_mean_mpg(car_data):
    """
    Calculates the mean MPG for a list of car data.
    """
    total_mpg = 0
    num_cars = len(car_data)
    for car in car_data:
        total_mpg += int(car['mpg'])
    return total_mpg / num_cars
