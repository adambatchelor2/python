from datetime import date
from datetime import datetime

today = str(date.today())
time = datetime.now().strftime("%H:%M")

first = input("whats your first name: ")
\
second =input("whats your middle name: ")
third=input("whats your last name: ")
print("hello " +first+" "+ second +" "+ third +" my name is ingwato today is " + today + " time is "+time)