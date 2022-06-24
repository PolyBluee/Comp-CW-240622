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
    
    def fib(n):

        a=0
        b=1

        if fibn == 1:
            print(a)
        
        elif fibn<1:
            print("Expected positive integer.")

        else:
            print(a)
            print(b)


            for i in range(2,n):

                c=a+b
                a=b
                b=c
            
                print(c)
    
    fibn = int(input("How many would you like to generate? > "))
    fib(fibn)
    


else:
    print("Incorrect argument! Closing...")
    time.sleep(3)
    exit()
