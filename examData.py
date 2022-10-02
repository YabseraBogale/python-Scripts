#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:01:46 2022

math=df[['gender','parental level of education','lunch','test preparation course','math score']]
pass_math=math[math['math score']>50].reset_index()
failed_math=math[math['math score']<50].reset_index()


@author: yabsera
"""

import pandas as pd
df = pd.read_csv('exams.csv')
print(df['parental level of education'].unique())

