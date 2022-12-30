# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 15:50:41 2022

@author: Luca
"""

# 1. Create an array “B” with all the elements from 0 to 150 (150
# excluded) that are divisible by 3.
# Tip: you can do this with a single line from the “Array creation”
# slide!
# 2. Change ”B” to a 2D array of size 10X5
# 3. Print only the odd rows of B
# Extra: try without using any loop.

import numpy as np

#1
B=np.arange(0,150,3)
print(B)

#2 
B=B.reshape(10,5)
print(B)

#3 with loop
for i in range(1,len(B),2):
    print(B[i])
    
#can also be done by:
for i in range(1,B.shape[0],2): #B.shape is the n° of rows
    print(B[:][i] #columns(all of them):rows 

# without loop
B=B[1::2]
print(B)  #start:end:step
