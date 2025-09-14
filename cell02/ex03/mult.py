#!/usr/bin/env python3
def main(number1, number2):
    total = number1 * number2
    print(str(number1) + " X " + str(number2) + " = " + str(total))
    if total == 0:
        print("This number is both positive and negative.")
    elif total < 0:
        print("This number is negative.")
    else:
        print("This number is positive.")
main(int(input("Enter the first number: \n")), int(input("Enter the second number: \n")))