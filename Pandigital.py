#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 15:28:25 2022
A pandigital number contains all digits (0-9) at least once. Write a function that takes an integer, 
returning true if the integer is pandigital, and false otherwise.
@author: yabsera
"""
def num(Pal):
   numstr=str(Pal)
   count={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
   countkey=[]
   boo=False
   for i in count.keys():
       countkey.append(i)
   for i in numstr:
       if(i in countkey):
           count[i]=1
   for i in count.values():
       if(i==1):
           boo=True
       else:
           return False
   return boo
print(num(1234590))
