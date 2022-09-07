#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:32:26 2022
Create a function that takes the height and radius of a cone as arguments 
and returns the volume of the cone rounded to the nearest hundredth.
Return approximate answer by rounding the answer to the nearest hundredth.
Use python PI property, don't fall for 3.14 ;-)
If the cone has no volume, return 0.
@author: yabsera
"""

import math
def cone(h,r):
    volume=(pow(r,2)*h*math.pi)/3
    return round(volume*100+0.5)/100
print(cone(100,2))