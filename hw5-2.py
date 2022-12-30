# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:30:09 2022

@author: Luca
"""

# Write a function that takes as input a list of strings, and generate a
# dictionary where to each string in the list is associated the number
# of vowels it contains.

S=["caio","tizio","sempronio"]


def dic_vow(S):
    vowels=["a","e","i","o","u"]
    numvow={}
    i=0
    while i<len(S):
        k=0   #k is the number of vowels in each string
        for c in S[i]:
            if c in vowels:
                k=k+1
            numvow[S[i]]=k
        i+=1
    return numvow

print(dic_vow(S))

