# Program to print fibonacci sequence

import time

print("Welcome to Lorem Ipsum Dolor Sit Amet.")
print("Type in 'r' to begin program.")
print("")

start_cmd = input("> ")

if start_cmd == 'r':
    print("Starting program...")
    time.sleep(2)
    print("")
    print("")
    t = int(input("How many terms would you like to generate? > "))

    
    n1, n2 = 0, 1
    count = 0

    if t <= 0:
        print("Expected: Positive Integer.")
    
    elif t == 1:
            print("Fibonacci sequence upto: ",t,":")
            print(n1)
    
    else:
        print("Fibonacci sequence:")
        while count < t:
            print(n1)
            nth = n1 + n2
            
            n1 = n2
            n2 = nth
            count += 1

else:
    print("Incorrect argument! Closing...")
    time.sleep(3)
    exit()