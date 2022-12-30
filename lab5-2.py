# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:04:33 2022

@author: Luca
"""

#Write a function that gets as input a matrix and returns its
# transpose.
M=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

T=[]

for i in range(len(M[0])):
    t=[]
    for j in range(len(M)):
        t.append(M[j][i])
    T.append(t)

print(T)
    
    
    



    
    
    

    
    
# T[0][0]=M[0][0]
# T[0][1]=M[1][0]