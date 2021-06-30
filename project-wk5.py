# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:41:18 2021

@author: robert
"""
import random
import time
    
"""generate 1000 random floting numbers"""
start_time = time.time() #start timer
s=[]
for i in range (1000):
    n= random.random()
    s.append(n)
print(s)
print("\n")    
print("--- %s seconds ---" % (time.time() - start_time))     