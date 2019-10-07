# Python Self Learning - Udara Alwis
# https://www.youtube.com/playlist?list=PLlrxD0HtieHhS8VzuMCfQD4uJ9yne1mE6
# Learnings from Video 14-
# Contains: Date, Time

from datetime import datetime, timedelta

#start app

#get current date time
current_date = datetime.now()
print(f"Today - {str(current_date)}")

#get current date time in details
print(f"Today day: {str(current_date.strftime('%A'))}")
print(f"Today date: {str(current_date.day)}")
print(f"Today month: {str(current_date.month)}")
print(f"Today year: {str(current_date.year)}")

print(f"Time Now: {str(current_date.hour)}:" +
                f"{str(current_date.minute)}:" +
                f"{str(current_date.second)} " +
                f"{current_date.strftime('%p')}")

#define a timedelta period
one_day = timedelta(days=1)

#calculate previous date
yesterday_date = current_date - one_day
print(f"Yesterday date was - {str(yesterday_date)}")

#calculate tomorrow date
tomorrow_date = current_date + one_day
print(f"Tomorrow date is - {str(tomorrow_date)}")

#define a timedelta period
one_week = timedelta(weeks=1)
#calculate one week before todaay
last_week = current_date - one_week
print(f"One week ago from today was - {last_week}")


# print("Let's play a little date game...")
# birthday = input("Sir, what is your Birthday? Please let me know as dd/mm/yyyy - ")

# #protecting the execution with try catch error handling
# try:

#     #stripping date time object from string
#     birthday_value = datetime.strptime(birthday, "%d/%m/%Y")
    
#     print("So your Birthday was on: " + str(birthday_value))

#     #calculate one day before birthday
#     one_day_before_birthday = birthday_value - one_day
#     print("One day before your Birthday was: " + str(one_day_before_birthday))

# except ValueError as error: #ops error ocurred
#     print("Ops! You entered a wrong date! Try again!")
# else:
#     print("Something went wrong bruh!")
# finally:
#     print("Wasn't that cool eh!")



value = input("What's your income? ")

value = float(value)

if value >= 1.00:
    tax = 0.07
else:
    tax = 0

print(f"Your tax: {tax}")

#end app