# Program to validate a leap year

import time

# Unnecessary start wizard because i am extra cool

print("Welcome to Lorem Ipsum Dolor Sit Amet.")
print("Type in 'r' to begin program.")
print("")

start_cmd = input("> ")

if start_cmd == 'r':
    print("Starting program...")
    time.sleep(2)
    print("")
    print("")


    year = int(input("Enter a year: "))

    if (year % 400 == 0) and (year % 100 == 0):
        print(year, "is a leap year!")

    elif (year % 4 ==0) and (year % 100 != 0):
        print(year, "is a leap year!")

    else:
        print(year, "isn't a leap year... (Suggestion: If you like leap years, try '2012'!)")
