# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 20:01:05 2022

@author: Luca
"""

#  Write a function reverse_vocabulary that takes a dictionary containing an italia to english
# vocabulary and returns the corresponding english to italian as a python dictionary

ita2eng= {"Ciao": "Hello", "Grazie": "Thanks", "Arrivederci": "Goodbye"}

eng2ita={values: keys for keys,values in ita2eng.items()}
    
    