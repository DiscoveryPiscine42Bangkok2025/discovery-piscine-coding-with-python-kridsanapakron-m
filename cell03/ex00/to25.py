#!/usr/bin/env python3
def main(number):
    if number > 25:
        print("Error")
    else:
        for i in range(number, 26):
            print("Inside the loop, my variable is " + str(i))
main(int(input("Enter a number less than 25\n")))