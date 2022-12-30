# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 00:08:20 2022

@author: Luca
"""

# write a circle data type: a circle is individuated by the coordinates of the center and the radious.
# Write the following methods:
# - compute_area()
# - compute_perimeter()
# - move_to(X,Y) where X and Y are the new coordinates of the center.

import math

class circle:
    def __init__(self, ctr_x, ctr_y, rad):
        self.ctr_x= ctr_x
        self.ctr_y= ctr_y
        self.rad= rad
        
    def compute_area(self):
        rad= circle.rad
        area= rad**2*math.pi
        return area
    
    def compute_perimeter(self):
        rad= circle.rad
        perimeter= rad*2*math.pi
        return perimeter
    
    def move_to(self,X,Y):
        self.ctr_x= X
        self.ctr_y= Y


circle=circle(10,10,5)