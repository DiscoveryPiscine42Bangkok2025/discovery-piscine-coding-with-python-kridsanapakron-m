#!/usr/bin/env python3  
import sys
def main():
    my_list = []
    if len(sys.argv) <= 1:
        print("none")
        return
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    if end > start:
        step = 1
        stop = end + 1
    else:
        step = -1
        stop = end - 1
    for i in range(start, stop, step):
        my_list.append(i)
    print(my_list)
main()