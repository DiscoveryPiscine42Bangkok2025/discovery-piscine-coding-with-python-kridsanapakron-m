#!/usr/bin/env python3
def array_of_names(my_dict):
    my_list = []
    for key, value in my_dict.items():
        my_list.append(key[0].upper() + key[1:] + " " + value[0].upper() + value[1:])
    return my_list


def main():
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier",
    }
    print(array_of_names(persons))


main()
