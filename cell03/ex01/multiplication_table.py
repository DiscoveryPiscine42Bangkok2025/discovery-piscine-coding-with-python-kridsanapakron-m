#!/usr/bin/env python3
def main(number):
    for i in range(10):
        print(str(i) + " X " + str(number) + " = " + str(number * i))
main(int(input("Enter a number: \n")))