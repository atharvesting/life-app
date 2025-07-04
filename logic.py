import datetime
from dateutil.relativedelta import relativedelta
from dateutil import parser

# Initialisation with required dates

birthdate = parser.parse("31.03.2007")  # input("What is your birthdate? ")
today_date = datetime.datetime.today()  # .date() at the end returns the date part only

# Various calculations necessary for future logic

age = relativedelta(today_date, birthdate)
date_at_ninety = birthdate + relativedelta(years=90)
full_delta = date_at_ninety - birthdate
past_delta = today_date - birthdate  # this is a time delta, you are subtracting dates and the output will not be in days.
future_delta = date_at_ninety - today_date
weeks_lived = past_delta.days // 7  # past_delta.days will convert the difference into days.
remaining_weeks = future_delta.days // 7
weeks_in_life = full_delta.days // 7

# Milestones calculator

date_at_18 = birthdate + relativedelta(years=18)
date_at_50 = birthdate + relativedelta(years=50)

# progress bar

progress_bar = "|"
progress_percentage = int((age.years / 90) * 100)
current_bars = progress_percentage // 10
iter = 0
while iter < current_bars:
    progress_bar += "$"
    iter += 1
progress_bar += ("-"*(10-iter))
progress_bar += "|"
print(f"Your life progress bar: {progress_bar}")

# Printing processed information

print(f"Right now, your age is {age.years} years, {age.months} months, and {age.days} days.")
print(f"You are on week number {weeks_lived}.")
print(f"Assuming you die at the age of 90, you are going to live till {date_at_ninety.strftime('%d/%m/%Y')}")
print(f"You will have lived a total of {weeks_in_life} weeks and right now, {remaining_weeks} remain.")