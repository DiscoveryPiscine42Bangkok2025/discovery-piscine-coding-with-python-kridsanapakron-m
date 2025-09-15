#!/usr/bin/env python3
def main():
    old_list = [2, 8, 9, 48, 8, 22, -12, 2]
    my_set = set()
    for x in old_list:
        if x > 5 :
            my_set.add(x + 2)
    print(str(old_list))
    print(my_set)
main()