#!/usr/bin/env python

def counter(a, b):
   c = 0
   processed = ""
   for c1 in range(len(str(a))):
      cur_dig_a = str(a)[c1:c1+1]
      for c2 in range(len(str(b))):
         cur_dig_b = str(b)[c2:c2+1]
         if cur_dig_a == cur_dig_b and processed.find(cur_dig_b) == -1:
            processed += cur_dig_b
            c += 1
   return c


print counter(1233211, 12128)
