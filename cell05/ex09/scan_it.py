#!/usr/bin/env python3  
import sys
def main():
    if len(sys.argv) != 3:
        print("none")
        return
    target = sys.argv[1]
    word = sys.argv[2]
    count = sum(1 for w in word.split() if w == target)
    print(count if count > 0 else "none")
main()