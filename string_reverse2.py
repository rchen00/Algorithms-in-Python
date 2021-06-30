# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 14:11:40 2021

@author: robert
"""

def string_reverse2(in_string, rev_string):
    if in_string=="":
        return rev_string
    else:
        rev_string+=in_string[-1]
        print(rev_string, end=' _ ')
        print(in_string[:-1])
        return string_reverse2(in_string[:-1], rev_string)
in_string=input("input string is: ")
rev_string=string_reverse2(in_string, '')
print(f"reverse of {in_string} is {rev_string}")

""" this program has a recursively function to add and assign the last character form in_string to 
rev_string until the in_string equal to "". I add two print statements in the function just to see the intermediate result.

"""

