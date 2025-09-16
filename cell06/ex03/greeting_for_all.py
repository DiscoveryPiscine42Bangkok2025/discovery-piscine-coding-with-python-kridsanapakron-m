#!/usr/bin/env python3
def greetings(param = "noble stranger"):
    if str(param).isdigit():
        print("Error! It was not a name.")
    else:
        print("Hello, "  + str(param) + ".")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)