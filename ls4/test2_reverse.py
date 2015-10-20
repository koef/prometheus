#!/usr/bin/env python
import sys

in_args = sys.argv[1:]
out_str = ''

in_args.reverse()

for cur_word in in_args:
   out_str = out_str + ' ' + str(cur_word)

print out_str[1:]
