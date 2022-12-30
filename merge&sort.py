# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 23:39:02 2022

@author: Luca
"""

#  Implement a function merge list that takes two list of integers of the same length and returns a list
# that contains all the elements of both the lists where odd numbers come first and even numbers at
# the end

M= [1,2,3,4,5]
N= [6,7,8,9,0]

L= M+N
S= []
for i in range(len(L)):
    if L[i]%2!=0:
        S.insert(0, L[i])
    else:
        S.append(L[i])

        
    
            