# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 11:58:48 2022

@author: Luca
"""

# Write a function get float that checks if the user types a float and
# if this is the case returns it; otherwise it asks the user again.
# ● NB. The function should work without generating runtime errors.
# ● Hint use the try/except statement.

    
def get_float():
    n=input("Insert a float number: ")
    if "." in n:
        try:
            print(float(n))
        except:
            get_float()
    else:
        get_float()

get_float()

    
    