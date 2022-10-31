import pandas as pd
import numpy as np
df = pd.read_csv("google.csv")
lst=[]
for i in df["pwd"]:
	lst.append(i)
lst_count={}
for i in lst:
	if(lst.count(i)!=0):
		j=1
	if(i not in lst_count.keys()):
		lst_count[i]=j
	else:
		lst_count[i]+=j

lst=[]
for i in lst_count.values():
	lst.append(i)
b=np.array(lst)
c=b.max()
for i in lst_count.keys():
	if(lst_count[i]==2):
		print(i)
