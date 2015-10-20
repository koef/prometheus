# -*- coding: utf-8 -*-
__author__ = 'koef'


class SuperStr(str):
    def __init__(self, source_string):
        self.src_str = source_string

    def is_repeatance(self, s):
        if not isinstance(s, str) or self.src_str == "":
            return False
        src_len = len(self.src_str)
        s_len = len(s)
        s_repeats = self.src_str.count(s)
        if s_len * s_repeats == src_len:
            return True
        else:
            return False

    def is_palindrom(self):
        s = self.src_str
        if not isinstance(s, str):
            return False
        reversed_str = s[::-1]
        if s.lower().replace(' ', '') == reversed_str.lower().replace(' ', '') or s == "":
            return True
        else:
            return False


s2 = SuperStr('')
print s2.is_repeatance('')
print s2.is_repeatance('a')