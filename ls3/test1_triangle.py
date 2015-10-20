#!/usr/bin/env python
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

control_var = 0

if (a + b) > c:
   control_var = control_var + 1
if (c + b) > a:
   control_var = control_var + 1
if (a + c) > b:
   control_var = control_var + 1

if control_var == 3:
   print 'triangle'
else:
   print 'not triangle'

