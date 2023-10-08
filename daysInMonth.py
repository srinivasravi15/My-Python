# Functions with outputs
def leap_year(year_in):
    if year_in % 4 == 0:
        if year_in % 100 == 0:
            if year_in % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
def days_in_month(year_input, month_input):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    year_is_leap = leap_year(year_input)
    if year_is_leap:
        if month_input == 2:
            month_days = month_days[1] + 1
            print(f"Since this is a Leap year, there are {month_days} days in month {month_input} of the year {year_input}")
        else:
            month_days = month_days[month_input - 1]
            print(f"There are {month_days} days in month {month_input} of the year {year_input}")
    else:
        month_days = month_days[month_input - 1]
        print(f"There are {month_days} days in month {month_input} of the year {year_input}")

year = int(input("Enter the year: "))
if year > 10000:
    print("Invalid year input. Please provide a valid year.")
    exit()
month = int(input("Enter the month: "))
if month > 12:
    print("Invalid month entered. Please provide a valid month in the range 1 - 12.")
    exit()
days = days_in_month(year, month)
