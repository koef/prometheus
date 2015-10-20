# -*- coding: utf-8 -*-
__author__ = 'koef'

class CombStr(object):
    def __init__(self, string):
        self.string = string
    def count_substrings(self, length=0):
        if not length or length > len(self.string):
            return 0
        n = length
        lst = []
        while n <= len(self.string):
            seq = self.string[n-length:n]
            if seq not in lst:
                lst.append(seq)
            n += 1
        return len(lst)

test = CombStr("qqqqqqweqqq%")
print test.count_substrings(15)