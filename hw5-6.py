# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:37:49 2022

@author: Luca
"""

# Write a function that takes two matrices of strings and
# returns a cartesian product matrix.

# M e N sono il club della briscola

M=[["Sergio","Franco"],["Luigi","Olga"]]
N=[["Luisa","Maria"],["Luisa","Luigi"],["Anna","Olga"]]

# Should return:
# C=[[Sergio,Franco,Luisa,Maria],
   # [Sergio,Franco,Luisa,Luigi],
   # [Sergio,Franco,Anna,Olga],
   # [Luigi,Olga,Luisa,Maria],
   # [Luigi,Olga,Luisa,Luigi],
   # [Luigi,Olga,Anna,Olga]]

def cartesian(M,N):
    C=[] 
    for i in range(len(M)):
        for j in range(len(N)):
            c=M[i]+N[j]
            C.append(c)
    return C
        
print(cartesian(M,N))