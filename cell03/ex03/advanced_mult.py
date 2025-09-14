#!/usr/bin/env python3
import sys
def main():
    i = 0
    j = 0
    if len(sys.argv) == 1:
        while i < 11:
            my_list = []
            my_list.append("Table de " + str(i) + ":")
            while j < 11:
                my_list.append(str(i * j))
                j += 1
            i += 1
            j = 0
            print(" ".join(my_list))
    else:
        print("none")
main()