#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:17:01 2022

@author: yabsera
"""

import pandas as pd
def people(item):
  i_num={}
  for i in item:
      if(i not in i_num):
          i_num[i]=1
      else:
          i_num[i]+=1
  return i_num



df=pd.read_csv('school.csv')
print(df.info())
Item=df['Item']
Region=df['Region']
Rep=df['Rep']


print("ITEM LIST",people(Item))
print("REGION LIST",people(Region))
print("REP LIST\n",people(Rep))
print("\nMEAN IS",df['Units'].mean())
print("SUM IS",df['Units'].sum())
print("STANDARD DEVATION",df['Units'].std())
print("VARIANCE",df['Units'].var())
print("MAX IS",df['Units'].max())
print("MIN IS",df['Units'].min())



Binder=df[df['Item']=='Binder']
print(Binder['Units'].nlargest(5))
print(Binder.loc[22])

Jones=df[df['Rep']=='Jones']

print(people(Jones['Item']))
print(Jones['Unit Cost'].nlargest(3))







