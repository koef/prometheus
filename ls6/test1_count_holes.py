#!/usr/bin/env python

def count_holes(n):
    number_of_holes = {"0": 1, "1": 0, "2": 0, "3": 0, "4": 1, "5": 0, "6": 1, "7": 0, "8": 2, "9": 1}

    if not isinstance(n, int) and not isinstance(n, long) and not isinstance(n, str):
        return "ERROR"

    try:
        numb = str(int(n))
    except ValueError:
        return "ERROR"

    counter = 0
    for digit in numb:
        counter += number_of_holes.get(digit, 0)

    return counter

print count_holes(888888888888888888888)