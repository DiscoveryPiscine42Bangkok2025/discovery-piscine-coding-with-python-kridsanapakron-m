#!/usr/bin/env python3
def main(text):
    for i in text:
        if i.islower():
            print(i.upper(), end="")
        else:
            print(i.lower(), end="")
main(input())