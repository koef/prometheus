#!/usr/bin/env python
import sys

fist_num = int(sys.argv[1])
sec_num = int(sys.argv[2])
counter = 0

for cur_num in range(fist_num, sec_num + 1):
   cur_num = str(cur_num)
   while len(cur_num) != 6:
      cur_num = "0" + cur_num
   
   sum_first_three_digit = 0
   for digit in cur_num[0:3]:
      sum_first_three_digit = sum_first_three_digit + int(digit)
   
   sum_last_three_digit = 0
   for digit in cur_num[3:6]:
      sum_last_three_digit = sum_last_three_digit + int(digit)
   if sum_first_three_digit == sum_last_three_digit:
      counter = counter + 1

print counter
