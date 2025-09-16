#!/usr/bin/env python3
def main():
    number = float(input())
    if number % 1  > 0:
        print("The number " + str(number) + " is a decimal.")
    else:
        print("The number " + str(int(number)) + " is an integer.")
main()