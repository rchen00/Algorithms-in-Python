# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 21:12:26 2021

@author: robert
"""

def string_reverse1(s): 
    if len(s) == 0: 
        return s 
    else:
        return string_reverse1(s[1:]) + s[0] 
        
    
      
s = "Robert"
  
print ("The original string  is: ",end="") 
print (s) 
  
print ("The reversed string(using recursion) is: " , end="") 
print (string_reverse1(s))

"""
String is passed as the argument to a recursive function to reverse a string. 
The base case is that the length of the string equal to 0, the string is returned.
If the length of the string is not 0, the reverse string function is recursively 
called to slice the part of the string except the first character and move the 
first character to the endof the sliced string.

"""