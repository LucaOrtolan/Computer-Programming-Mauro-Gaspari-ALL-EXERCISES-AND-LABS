# -*- coding: utf-8 -*-
"""
Created on Sat Dec 17 17:01:28 2022

@author: Luca
"""
# 1. Create the array “A” with length 10 and elements from 1 to 10.
# 2. Now keep inside ”A” only the odd elements.
# 3. Take the square root of each element of the new ”A” (**0.5).
# 4. Print the last element of the new ”A”.
# Extra: try without using any loop.

import numpy as np

#1
A=np.arange(1,11)

#2
A=A[A%2!=0]

#3
A=np.round(A**0.5, decimals=2)  

#4 
print(A[-1])