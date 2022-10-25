import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as mp

df=pd.read_csv("IBM_Attrition_Data.csv")
IBMCOL=df.columns
attdf=df[[IBMCOL[1],IBMCOL[0]]]
attdf_yes=attdf[attdf[IBMCOL[1]]=="Yes"]
attdf_no=attdf[attdf[IBMCOL[1]]=="No"]
print("=====================================")
print("Mean ",round(df[IBMCOL[0]].mean(),2))
print("Median",df[IBMCOL[0]].median())
print("Var",round(df[IBMCOL[0]].var(),2))
print("Std",round(df[IBMCOL[0]].std(),2))
print("=====================================")
print("=========Attrition Yes===============")
print("=====================================")
print("Yes",len(attdf_yes))
print("shape",attdf_yes.shape)
print("Mean",round(attdf_yes[IBMCOL[0]].mean(),2))
print("Median",attdf_yes[IBMCOL[0]].median())
print("Var",round(attdf_yes[IBMCOL[0]].var(),2))
print("Std",round(attdf_yes[IBMCOL[0]].std(),2))
print("Example")
print(attdf_yes.iloc[5])
print("=====================================")
print("=========Attrition No================")
print("=====================================")
print("No",len(attdf_no))
print("shape",attdf_no.shape)
print("Mean",round(attdf_no[IBMCOL[0]].mean(),2))
print("Median",attdf_no[IBMCOL[0]].median())
print("Var",round(attdf_no[IBMCOL[0]].var(),2))
print("Std",round(attdf_no[IBMCOL[0]].std(),2))
print("Example")
print(attdf_no.iloc[5])
print("=====================================")
print("==========Eduation filed=============")
print("=====================================")
"""
attdf_ms=df[IBMCOL[8]]
print(attdf_ms.head())
data=sb.heatmap(df.corr(), cmap="YlGnBu", annot=True)
mp.show()

"""
