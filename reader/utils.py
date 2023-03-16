from datetime import datetime

# This code defines the calculate_age function, which takes a birthdate string in the format YYYY-MM-DD
# and calculates the age based on the current date.
# The function uses the datetime module to convert the birthdate string to a datetime object,
# and then calculates the age based on the difference between the birth year and the current year,
# taking into account whether the person has had their birthday yet this year.


def calculate_age(birthdate_str):
    """Calculate age from a birthdate string"""
    birthdate = datetime.strptime(birthdate_str, '%Y-%m-%d')
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age
