# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:56:08 2021

@author: robert
"""

class ArrayStack:
    """LIFO Stack implementation"""
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self,_data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self,e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()
    
""" Transfer stack T to stack S """

str= " Transfer stack T to stack S "
print(str.center(40, '#'))
    
T=ArrayStack()
for i in range(10):
    x=input("Please input a letter:", )
    T.push(x)
print("Top of stack T is:" ,T.top())

S=ArrayStack()
for i in range(10):
    y=T.pop()
    print(y, end=' ')
    S.push(y)
print("Top of stack S is:" ,S.top())

""" Reverse contents in stack A """
str= " Reverse contents in stack A "
print(str.center(40, '#'))
    
A=ArrayStack()
for i in range(10):
    z=A.push(i)
    print(A.top(), end=' ')
    
print("Top of stack A is:" ,A.top())
    
T=ArrayStack()
for i in range(10):
    x=A.pop()
    T.push(x)
    
for i in range(10):
    y=T.pop()
    S.push(y)
  

for i in range(10):
    z=S.pop()
    print(z, end=' ')
    A.push(z)    
    
print("Top of stack A is:" ,A.top())
    
