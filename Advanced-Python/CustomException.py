# How to raise custom exceptions through your code and handle those
import datetime


class Error(Exception):
    pass


class dobException(Error):
    pass


year = int(input("Enter year of Birth: "))
age = int(datetime.date.today().year) - year
try:
    if age > 30 or age <= 20:
        raise dobException
except dobException:
    print("You're not eligible for the exam")
else:
    print("You're eligible.")
