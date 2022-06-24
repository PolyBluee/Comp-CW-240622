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
        print("{0} is a leap year!".format(year))

    elif (year % 4 ==0) and (year % 100 != 0):
        print("{0} is a leap year!".format(year))

    else:
        print("{0} is not a leap year...".format(year))