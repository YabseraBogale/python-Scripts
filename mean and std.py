#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 11:28:10 2022
lst=np.array(list[0:3])
  lst2=np.array(list[3:6])
  lst3=np.array(list[6:9])
  print(lst2,lst3)
  return lst.append(lst2)
@author: yabsera
"""

import numpy as np

def calculate(list):
  if(len(list)>9):
    raise ValueError("List must contain nine numbers.")
  lst=np.array([list[0:3],list[3:6],list[6:9]])
  
  mean_row=[lst[0].mean(),lst[1].mean(),lst[2].mean()]
  mean_col=[lst[:,0].mean(),lst[:,1].mean(),lst[:,2].mean()]
  mean_flat=lst.mean()
  
  var_col=[lst[:,0].var(),lst[:,1].var(),lst[:,2].var()]
  var_row=[lst[0].var(),lst[1].var(),lst[2].var()]
  var_flat=lst.var()
  
  std_col=[lst[:,0].std(),lst[:,1].std(),lst[:,2].std()]
  std_row=[lst[0].std(),lst[1].std(),lst[2].std()]
  std_flat=lst.std()
  
  max_row=[lst[0].max(),lst[1].max(),lst[2].max()]
  max_col=[lst[:,0].max(),lst[:,1].max(),lst[:,2].max()]
  max_flat=lst.max()
  
  min_row=[lst[0].min(),lst[1].min(),lst[2].min()]
  min_col=[lst[:,0].min(),lst[:,1].min(),lst[:,2].min()]
  min_flat=lst.min()
  
  sum_row=[lst[0].sum(),lst[1].sum(),lst[2].sum()]
  sum_col=[lst[:,0].sum(),lst[:,1].sum(),lst[:,2].sum()]
  sum_flat=lst.sum()
  
  cal={'mean':[mean_col,mean_row,mean_flat],
       'variance':[var_col,var_row,var_flat],
       'standard deviation':[std_col,std_row,std_flat],
       'max':[max_col,max_row,max_flat],
       'min':[min_col,min_row,min_flat],
       'sum':[sum_col,sum_row,sum_flat]
       }
  return cal
print(calculate([0,1,2,3,4,5,6,7,8]))