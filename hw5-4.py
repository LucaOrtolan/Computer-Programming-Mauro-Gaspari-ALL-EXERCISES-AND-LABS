# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 17:23:42 2022

@author: Luca
"""

# Write a function that takes as input two lists of floating point
# numbers having the same lenght, and computes the scalar product.
# a°b=sum(ai*bi,i=1,n)

a=[1.0,2.0,3.0]
b=[4.0,5.0,6.0]
# S=[4+10+18=32] expected result

def scalar(a,b):
    S=0
    for i in range(len(a)):
        s=a[i]*b[i]
        S=S+s
    return S

print(scalar(a,b))
    

