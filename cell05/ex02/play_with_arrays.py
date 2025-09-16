#!/usr/bin/env python3
def main():
    old_list = [2, 8, 9, 48, 8, 22, -12, 2]
    new_list = [x + 2 for x in old_list if x > 5]
    print(old_list)
    print(new_list)
main()