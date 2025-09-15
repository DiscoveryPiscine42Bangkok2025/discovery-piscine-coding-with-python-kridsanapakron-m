#!/usr/bin/env python3  
import sys
def main():
    if len(sys.argv) == 1:
        print("none")
        return
    user_input = input("What was the parameter? ")
    if sys.argv[1] == user_input:
        print("Good job!")
    else:
        print("Nope, sorry...")
main()