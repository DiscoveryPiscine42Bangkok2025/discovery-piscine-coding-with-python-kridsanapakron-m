#!/usr/bin/env python3
import sys
def shrink(text):
    s = slice(0, 8)
    return text[s]

def enlarge(text):
    return text.ljust(8, 'z')

def main():
    if len(sys.argv) <= 1:
        print("none")
        return
    for i in sys.argv[1:]:
        if len(shrink(i)) < 8:
            print(enlarge(i))
        else:
            print(shrink(i))
main()