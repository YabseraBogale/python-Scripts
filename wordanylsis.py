#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 09:29:54 2022

@author: yabsera
"""

import pandas as pd
import csv
file=open('mobydick.txt')
words={"A":0, "B":0, "C":0, "D":0, "E":0,"F":0,"G":0, "H":0, "I":0, "J":0, "K":0, "L":0, "M":0,
       "N":0, "O":0, "P":0, "Q":0, "R":0, "S":0, "T":0, "U":0, "V":0, "W":0, "X":0, "Y":0, "Z":0}
lst=[]
num=0
for key,value in words.items():
    lst.append(key)
for i in file:
    i=i.upper().rstrip()
    for j in i:
        if(j not in lst):
            words[j]=1
        else:
            words[j]+=1

df=pd.DataFrame(list(words.items()))
print(df.loc[0:25])
"""High_6=df['Number'].nlargest(5)
high_6=(high_6.reset_index().drop(columns="index"))
print(high_6.set_index("letters",drop=True,inplace=True))
print(high_6.plot.bar())
"""