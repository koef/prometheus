# -*- coding: utf-8 -*-
__author__ = 'koef'


def find_fraction(summ):
    if summ <= 2:
        return False
    if summ % 2 == 0:
        a = b = summ/2
        a -= 1
        b += 1
        if a % 2 == 0:
            a -= 1
            b += 1
    else:
        a = summ/2
        b = summ/2 + 1
    return a, b

print find_fraction(2)