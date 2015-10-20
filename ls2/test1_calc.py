#!/usr/bin/env python
import sys
import math

a = float(sys.argv[1])
b = float(sys.argv[2])

x = math.sqrt(a*b)/(math.pow(math.e, a)*b)+a*math.e**(2*a/b)

print x
print 10/4**3.0
