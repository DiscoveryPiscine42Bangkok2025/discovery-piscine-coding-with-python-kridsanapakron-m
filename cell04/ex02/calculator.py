#!/usr/bin/env python3
def main():
    first_number = int(input("Give me the first number: "))
    second_number = int(input("Give me the second number: "))
    print("Thank you!")
    print(str(first_number) + " + " + str(second_number) + " = " + str(first_number + second_number))
    print(str(first_number) + " - " + str(second_number) + " = " + str(first_number - second_number))
    if second_number != 0:
        print(str(first_number) + " / " + str(second_number) + " = " + str(first_number // second_number))
    else:
        print("Division by zero is not allowed.")
    print(str(first_number) + " * " + str(second_number) + " = " + str(first_number * second_number))
main()