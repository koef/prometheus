#!/usr/bin/env python
import sys

n = int(sys.argv[1])
prev = 0
cur = 1

if n <= 0:
   cur = 0
else:
   for i in range(n-1):
      bak = cur
      cur = cur + prev
      prev = bak

print cur
