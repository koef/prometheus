#!/usr/bin/env python


def convert_n_to_m(x, n, m):
    x_dec = 0
    gt_to_nine = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15,
        "G": 16,
        "H": 17,
        "I": 18,
        "J": 19,
        "K": 20,
        "L": 21,
        "M": 22,
        "N": 23,
        "O": 24,
        "P": 25,
        "Q": 26,
        "R": 27,
        "S": 28,
        "T": 29,
        "U": 30,
        "V": 31,
        "W": 32,
        "X": 33,
        "Y": 34,
        "Z": 35
    }
    result = ""

    number_of_digits = len(str(x)) - 1

    try:
        if 1 < n <= 10:
            for digit in str(x):
                if int(digit) > n - 1:
                    return False
                x_dec += int(digit) * n ** number_of_digits
                number_of_digits -= 1

        elif n == 1:
            if int(x) != 0:
                return False
            x_dec = str(x).count("0")
        elif n > 10:
            for digit in str(x):
                if gt_to_nine[digit.upper()] > n -1:
                    return False
                x_dec += gt_to_nine[digit.upper()] * n ** number_of_digits
                number_of_digits -= 1
        else:
            return False
    except (ValueError, KeyError):
        return False

    if m == 10:
        return x_dec
    elif 1 < m < 10:
        lp = True
        while lp:
            result = str(x_dec % m) + result
            x_dec = x_dec/m
            if x_dec == 0:
                lp = False
        result = int(result)
    elif m == 1:
        for lp in range(x_dec):
            result += "0"
    elif 10 < m <= 36:
        lp = True
        while lp:
            for key, val in gt_to_nine.items():
                if val == x_dec % m:
                    result = key + result
            x_dec = x_dec/m
            if x_dec == 0:
                lp = False

    return result


print convert_n_to_m(777, 10, 2)