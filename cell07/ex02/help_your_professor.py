#!/usr/bin/env python3
def average(my_dict):
    totol = 0
    for value in my_dict.values():
        totol += value
    return totol / len(my_dict)
def main():
    class_3B = {
        "marine": 18,
        "jean": 15,
        "coline": 8,
        "luc": 9
    }
    class_3C = {
        "quentin": 17,
        "julie": 15,
        "marc": 8,
        "stephanie": 13
    }
    print(f"Average for class 3B: {average(class_3B)}.")
    print(f"Average for class 3C: {average(class_3C)}.")
main()