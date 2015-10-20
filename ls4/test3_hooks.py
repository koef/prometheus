#!/usr/bin/env python
import sys

in_str = str(sys.argv[1])
shift_r = 0
shift_l = 0
pdp = False
rev_pdp = False

if in_str.find('(') != -1 or in_str.find(')') != -1:
   while in_str.find('(', shift_r) != -1:
      if shift_l == 0:
         shift_l = in_str.find('(', shift_r) + 1
      if in_str.find(')', shift_l) != -1:
         pdp = True
         shift_r = in_str.find('(', shift_r) + 1
         shift_l = in_str.find(')', shift_l) + 1
      else:
         pdp = False
         break
   
   shift_l = len(in_str)
   shift_r = len(in_str)
   while in_str.rfind(')', 0, shift_l) != -1:
      if shift_r == len(in_str):
         shift_r = in_str.rfind(')', 0, shift_l)
      if in_str.rfind('(', 0, shift_r) != -1:
         rev_pdp = True
         shift_l = in_str.rfind(')', 0, shift_l)
         shift_r = in_str.rfind('(', 0, shift_r)
      else:
         rev_pdp = False
         break
else:
   pdp = True
   rev_pdp = True

if pdp == True and rev_pdp == True:
   print 'YES'
else:
   print 'NO'
