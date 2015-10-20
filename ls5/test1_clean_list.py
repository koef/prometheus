#!/usr/bin/env python

def clean_list(list_to_clean):
   new_list = []
   for element in list_to_clean:
      flag = 0
      for new_el in new_list:
         if element == new_el and type(element) == type(new_el):
            flag = 1
      if flag == 0: 
         new_list.append(element)
   return new_list


lst = ['asd', 'dsa', 1, '1', 1.0, 44, 1.2, 1.0, "asd", "True", "True", True, False, False, None, None]
print lst
print clean_list(lst) 

