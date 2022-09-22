#!/usr/bin/env python3

import pandas as pd
import streamlit as st

df=pd.read_csv('csvData.csv')
l50=df.sort_values(by=['percPoverty'])
l50=(l50.sort_index(ascending=True))
l50=df.sort_values(by=['percPoverty'])
print(l50)