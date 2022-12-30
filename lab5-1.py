# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 17:46:42 2022

@author: Luca
"""

# Write a script that gets two integer numbers N and M from the
# user and generates a NxM matrix filled with random numbers.
# ● Hint use the random module generating new numbers as follow:
# import random
# newNumber = random.randint(1,100)
import random

#N are rows, M are columns

def row(M):
    r=[]
    j=0
    while j<M:
        r.append(random.randint(0,100))
        j+=1
    return r

def matrix(N,M):
    m=[]
    i=0
    while i<N:
        row(M)
        print(row(M))
        m.append(row(M))
        i+=1
    return m

matrix(4,3)
    
    
    