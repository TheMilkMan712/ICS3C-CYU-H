# Programmer: Jerome
# Description: Days in a Month

months = [
    "January", 
    "February", 
    "March", 
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

month = input("Enter a month: ")

for month in months:
    print("Invalid month! Try again.")
    month = input("Enter a month: ")

if month == "January", or "March", or "May", or "July", or "August", or "October", or "December":
    print(f"{month} has 31 days")