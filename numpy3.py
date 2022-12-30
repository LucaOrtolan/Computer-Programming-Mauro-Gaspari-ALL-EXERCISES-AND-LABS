# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 17:53:18 2022

@author: Luca
"""

# In this exercise, the names A and B represent the last versions of
# the arrays you created in exercises 1 and 2.
# 1. Change all the elements of the 3rd column of B to a value of 1.
# Hint: you can access position (i,j) inside a 2D array B with the
# command B[i,j].
# 2. Transpose B.
# 3. Create the array “C”, equal to the matrix product of B and A
# (in this order!).
# Extra: try without using any loop.

import numpy as np

# B
B=np.arange(0,150,3)
B=B.reshape(10,5)
B=B[1::2]

# A
A=np.arange(1,11)
A=A[A%2!=0]
A=np.round(A**0.5, decimals=2)  

#1
B[:,2]=1

#2
B=np.transpose(B)

#3
C=B@A
print(C)
print(C.shape)
print(C.dtype)