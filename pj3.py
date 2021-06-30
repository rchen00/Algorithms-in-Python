# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:56:08 2021

@author: robert
"""

class ArrayStack_maxLen:
    """LIFO Stack implementation"""
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self,_data)
    
    def __maxlen__(self):
        self.__maxlen__=
    
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
    
