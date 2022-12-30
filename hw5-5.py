# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 18:08:16 2022

@author: Luca
"""

# Write a function that implements the merge sort sorting algorithm
# which exploits a divide et impera approach.
# ● The list is divided in two parts having the same length, the two
# parts are sorted independently, and after that, they are merged.
# ● The process should be repeated several time
# ● Us the notation [:N] e [N:] two create two sublists of the same
# length..

L=["gallo","cane","topo","serpente","coniglio","bue","maiale","tigre"]


def mergeandsort(L):
    h=int(len(L)/2)
    M=L[:h]
    N=L[h:]
    for i in range(len(M)-1):
        flag=True
        while flag:
            flag=False
            if M[i].lower()>M[i+1].lower():
                M[i],M[i+1]=M[i+1],M[i]
                flag=True
    for i in range(len(N)-1):
        flag=True
        while flag:
            flag=False
            if N[i].lower()>N[i+1].lower():
                N[i],N[i+1]=N[i+1],N[i]
                flag=True
    MS=M+N
    return MS

print(mergeandsort(L))
        