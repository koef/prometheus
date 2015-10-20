#!/usr/bin/env python
import sys
import math

x = float(sys.argv[1])
u = float(sys.argv[2])
q = float(sys.argv[3])

f = 1/(q*math.sqrt(2*math.pi))*math.exp(-((x-u)**2/(2*q**2)))

print f

