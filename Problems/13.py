
from datetime import date

def sundays(): 
    counter = 0

    for year in range(1901, 2001):
        for month in range(1, 13):
            day = date(year, month, 1)
            if day.weekday() == 6:
                counter += 1

    return counter

print(sundays())

    