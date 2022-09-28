#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 09:43:14 2022

@author: yabsera
"""
import pandas as pd
import seaborn as sns
df= pd.read_csv('csvData.csv')
df.set_index("country", drop=True,inplace=True)
data_2015=df[df['dataYear']>=2015]
data_2015=data_2015.sort_values(by='percPoverty')
lst_index=[]
i=1
while i<=len(data_2015):
    lst_index.append(i)
    i+=1
data_2015['index']=lst_index
print(data_2015.head(5))
data_large=data_2015['percPoverty'].nlargest(5)
data_small=data_2015['percPoverty'].nsmallest(5)
print("the data of 2016 and above")
print("Maxium percPoverty is",data_2015['percPoverty'].max())
print("Minium percPoverty is",data_2015['percPoverty'].min())
print("Sum percPoverty is",data_2015['percPoverty'].sum())
print("Average percPoverty is",round(data_2015['percPoverty'].mean(),2))
print("Standard devation percPoverty is",round(data_2015['percPoverty'].std(),2))
print("variance is",round(data_2015['percPoverty'].var(),2))
print("Ethiopia index",data_2015.loc['Ethiopia']['index'])
print("graph",data_large.plot.heatbar())
