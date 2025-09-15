#!/usr/bin/env python3  
import sys
def main():
    my_list = []
    if len(sys.argv) <= 1:
        print("none")
        return
    if sys.argv[2] > sys.argv[1]:
        step = 1
    else:
        step = -1
    for i in range(int(sys.argv[1]), int(sys.argv[2]) + 1, step):
        my_list.append(i)
    print(my_list)
main()