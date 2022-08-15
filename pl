#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 14:36:22 2022

@author: yabsera
"""

from math import radians, cos, sin, asin, sqrt


def place(log1,lat1,log2,lat2):
    lat1=radians(lat1)
    lat2=radians(lat2)
    log1=radians(log1)
    log2=radians(log2)
    dlong=log2-log1
    dlat=lat2-lat1
    a = (sin(dlat/2)**2) + (cos(lat1) * cos(lat2) * (sin(dlong/2)**2))
    r=2 * asin(sqrt(a))
    c=6371
    return r*c
