# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 18:11:03 2022

@author: Luca
"""

# Implement the function "remove_vowel(S,X)", which takes two parameters as arguments: a
# string S a char X. Where S is of any possible lenght containing digits and letters.
# The function returns a new string considering the following rules:
# - letters equal to A, E, I, O, U both lowercase and uppercase should be substituted by X (only if
# X is a vowel), otherwise, if X is not a vowel, they should be deleted.
# - sequences of consonants like 'CCBBB' should be changed as follows 'C2B3'.
# - digits are not changed.

import string

S="123AbbaCChIoTTo456"
X="3"

vowels=["A","E","I","O","U","a","e","i","o","u"]

L=[]
for c in S:
    L.append(c)


if X in vowels:
    for c in range(len(S)):
        if L[c] in vowels:
            L[c]=X

else: 
    L=[]
    for c in range(len(S)):
        if S[c] not in vowels:
            L.append(S[c])
            

        
                    
                
                
   


    
    
