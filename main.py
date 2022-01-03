import os
import time
import datetime
import random

def isWeekend(date):
    return date.weekday() >=5

def main():
    # Date Format: YYYY-MM-DD HH:MM:SS

    # Get the current date
    current_date = datetime.datetime.now().date()

    # Start date
    start_date = datetime.date(2022, 1, 1)

    # Create a range of dates from start_date to current_date
    date_range = [start_date + datetime.timedelta(days=x) for x in range((current_date - start_date).days)]

    # Convert the dates to the desired format (YYYY-MM-DD HH:MM:SS)
    for date in date_range:
        # How many times will we commit today
        choice = random.randint(0,10)
        if isWeekend(date):
            choice = 0

        # Reformat Date
        date = date.strftime("%Y-%m-%d %H:%M:%S")

        msg = "historical commit test"
        for x in range(choice):
            with open("comment.txt", "a") as f:
                f.writelines("Another line\n")

                os.system(f"git add .")
                os.system(f"git commit --date=\"{date}\" -m \"{msg}\"")

if __name__ == '__main__':
    main()