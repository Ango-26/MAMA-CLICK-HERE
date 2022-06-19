import calendar


class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


year_or_month = input("Do you want the calendar for the year or just for a particular month? Type 'month' or 'year': ")

if year_or_month == "month":
    print(bColors.OKGREEN + "Welcome to the Calendar Program!" + bColors.BOLD)

    year = int(input("Enter Year: "))
    month = int(input("Enter Month: "))

    if year < 0:
        print(bColors.WARNING + "Warning: Input cannot be below 0!" + bColors.ENDC)

    if month > 12 or month < 1:
        print(
            bColors.WARNING + "Warning: Months below 1 (January) and greater than 12 (December), will not be in order" + bColors.ENDC)

    if year > 0 and 12 > month > 0:
        print(calendar.month(year, month))


elif year_or_month == "year":

    years = int(input("Year : "))
    print(f"The calendar of {years} is : ")
    print(calendar.calendar(years))
