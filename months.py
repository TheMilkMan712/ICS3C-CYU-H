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
    "December"]

month = input("Enter a month: ")

while month not in months:
    print("Invalid month! Try again.")
    month = input("Enter a month: ")

if month in ["January", "March", "May", "July", "August", "October", "December"]:
    print(f"{month} has 31 days")
    
if month in ["April", "June", "September", "November"]:
    print(f"{month} has 30 days")

if month == "February":
    print(f"{month} has 28 or 29 days")
