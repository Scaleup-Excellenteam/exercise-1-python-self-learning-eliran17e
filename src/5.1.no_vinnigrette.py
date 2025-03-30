"""
Module: no_vinnigrete
This module provides a function to generate a random date between two dates
and check if it is a Monday.
"""
import datetime
import random



def no_vinnigrete(date1, date2):
    """
    Generate a random date between two dates, regardless of their order
    and checks if its monday.
    Parameters:
    date1 (datetime or date): One of the boundary dates
    date2 (datetime or date): The other boundary date
    Returns true if its monday, false otherwise
    """
    if isinstance(date1, str):
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
    if isinstance(date2, str):
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d")
    start_date = min(date1, date2)
    end_date = max(date1, date2)
    delta = (end_date - start_date).days
    random_days = random.randint(0, delta)
    date_result = start_date + datetime.timedelta(days=random_days)
    if date_result.weekday() == 0:
        print("Ain't gettin' no vinaigrette today :(")

def main():
    """
    Main function to prompt user for two dates and check if a random date
    between them is a Monday.
    """
    dates = []
    while True:
        user_input = input("Please enter a date (YYYY-MM-DD): ")
        try:
            dates.append(datetime.datetime.strptime(user_input, "%Y-%m-%d"))
        except ValueError:
            print("Invalid date format. Please try again.")
        if len(dates) == 2:
            break
    no_vinnigrete(dates[0], dates[1])

if __name__ == "__main__":
    main()
