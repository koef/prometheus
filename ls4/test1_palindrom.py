#!/usr/bin/env python
import sys

in_str = str(sys.argv[1])
reversed_str = in_str[::-1] 

if in_str.lower().replace(' ', '') == reversed_str.lower().replace(' ', ''):
  print 'YES'
else:
  print 'NO'
