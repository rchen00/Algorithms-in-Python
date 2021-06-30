""" 
Project (Week 6)

1)	(10pts) Study the textbook Code Fragment 12.5 and implement the Quick-Sort for a Python list. Hint: Use Python list for S, L, E, and G. Use list built-in methods to achieve the enqueuer and dequeuer operations. Test your code and show your results before and after the sorting by using a Python list of simple integers.
2)	(5pts) Study the textbook Code Fragment 12.6 and (modify if necessary) to implement another in-place Quick-Sort for a Python list. Test your code and show your results before and after the sorting by using a Python list of simple integers. 
3)	(5pts) Experimentally compare the performance of above in-place and not in-place Quick-Sort code with a list of random float data. You can select the size of the Python list between 100-10000 so each run will take just several seconds.

Submit your code together with the run results.

"""


# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:37:45 2021

@author: robert
"""
from linked_queue import LinkedQueue
from quick_queue import quick_sort
from quick_inplace import inplace_quick_sort
import random
import time


""" Original List """ 
    
s=[23, 45, 50, 13, 100, 4, 28, 46, 37]

print("\nOriginal List:")
print(s)

""" put Original List into queue """ 
    
A=LinkedQueue()
for item in s: 
   A.enqueue(item)    
   
""" Quick Sort """   
  
quick_sort(A)
output=[]
for i in range (0,len(A)): 
    item=A.dequeue()
    output.append(item)
print("\nSorted by not inplace quick sort: ")   
print(output)
 


""" Inplace Quick Sort """ 
  
inplace_quick_sort(s,0,len(s)-1)
print("\nSorted by inplace quick sort: ")   
for i in range (len(s)): 
    print("%d" % s[i],end=', ')  
  
    
"""generate 100 random floting numbers"""
number=input("Input number from 100-10000: ")
s=[]
for i in range (int(number)):
    n= random.random()
    s.append(n)
print("\nGenerated ",number,"random numbers: ")
print(s)


""" Quick Sort """       

A=LinkedQueue()
for item in s: 
   A.enqueue(item)    

start_time = time.time() #start timer   
quick_sort(A)
end_time= time.time() # enf timer

output=[]
for i in range (0,len(A)): 
    item=A.dequeue()
    output.append(item)
    
print("\nSorted by not inplace quick sort: ")   
print(output)
print("--- %s seconds ---" % (end_time - start_time))   
    


""" Inplace Quick Sort """ 

start_time = time.time()        #start timer  
inplace_quick_sort(s,0,len(s)-1)
end_time= time.time()           # enf timer

print("\nSorted by inplace quick sort: ")   
print(s)
print("--- %s seconds ---" % (end_time - start_time))    