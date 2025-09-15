#!/usr/bin/env python3
def main():
    old_list = [2, 8, 9, 48, 8, 22, -12, 2]
    new_list = [x + 2 for x in old_list]
    print("Original array: " + str(old_list))
    print("New array: " + str(new_list))
main()