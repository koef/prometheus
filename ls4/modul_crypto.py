#!/usr/bin/env python
import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

in_str = sys.argv[1].replace(' ', '')
dec_str = ''
shift = 5

while shift <= len(in_str):
   word = in_str[shift-5:shift]
   shift = shift + 5
   dec_word = ''
   for letter in word:
      if letter.islower():
         dec_word = dec_word + "a"
      else:
         dec_word = dec_word + "b"

   dec_str = dec_str + alphabet[key.find(dec_word)]

print dec_str
