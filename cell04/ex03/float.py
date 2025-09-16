#!/usr/bin/env python3
def main():
    number = float(input())
    if number % 1  > 0:
        print("The number is a decimal.")
    else:
        print("The number is an integer.")
main()