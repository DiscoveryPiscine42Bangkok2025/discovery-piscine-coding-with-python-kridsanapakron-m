#!/usr/bin/env python3  
import sys
def main():
    if len(sys.argv) == 1:
        print("none")
        return
    count = sys.argv[1].count('z')
    print(count * "z" if count > 0 else "none")
main()