import matplotlib.pyplot as plt

def visualize_mpg_data(car_data):
    """
    Visualizes the MPG data for a list of car data.
    """
    mpg_values = [int(car['mpg']) for car in car_data]
    plt.hist(mpg_values, bins=20)
    plt.title('MPG Data')
    plt.xlabel('MPG')
    plt.ylabel('Frequency')
    plt.show()
