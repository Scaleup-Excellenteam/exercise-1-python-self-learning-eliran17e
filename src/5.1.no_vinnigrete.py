import datetime
import random

def no_vinnigrete(date1,date2):
    """
    Generate a random date between two dates, regardless of their order
    and checks if its monday.

    Parameters:
    date1 (datetime or date): One of the boundary dates
    date2 (datetime or date): The other boundary date

    Returns true if its monday, false otherwise
    """



    start_date = min(date1, date2)
    end_date = max(date1, date2)
    # Calculate the difference between dates in days
    delta = (end_date - start_date).days
    random_days = random.randint(0, delta)
    date_result = start_date + datetime.timedelta(days=random_days)
    if (date_result.weekday() == 0):
        return True
    else:
        return False


def main():
    dates = []
    while True:
        user_input = input("Please enter a date (YYYY-MM-DD): ")
        try:
            dates.append(datetime.datetime.strptime(user_input, "%Y-%m-%d"))
        except ValueError:
            print("Invalid date format. Please try again.")
        if len(dates) == 2:
            break
    if(no_vinnigrete(dates[0], dates[1])):
        print("No vinngrete for you")
    else:
        print("we have vinnigrete for you")
if __name__ == "__main__":
    main()
