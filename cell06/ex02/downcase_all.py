#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) <= 1:
        print("none")
        return
    for i in sys.argv[1:]:
        print(i.lower())
main()