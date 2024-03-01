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
    start_date = datetime.date(2024, 3, 1)
    current_date = datetime.date(2024, 3, 7) #overwrite current date for testing

    # Create a range of dates from start_date to current_date
    date_range = [start_date + datetime.timedelta(days=x) for x in range((current_date - start_date).days)]

    # Convert the dates to the desired format (YYYY-MM-DD HH:MM:SS)
    for date in date_range:
        # How many times will we commit today
        dist = [0,0,0,0,0,1,2,2,2,3,3,3,4,4,5,5,5,5,6,7,8,9,10]
        if isWeekend(date):
            dist = [0,0,0,0,0,0,1,2,3,4,5]
        choice = random.choice(dist)

        # Reformat Date
        date = date.strftime("%Y-%m-%d %H:%M:%S")

        with open("comment.txt", "a") as f:
            f.writelines("Another line\n")

        msg = "historical commit test"
        for x in range(choice):
            os.system(f"git add .")
            os.system(f"git commit --date=\"{date}\" -m \"{msg}\"")
            time.sleep(1000 + random.randint(-100,100))

if __name__ == '__main__':
    main()