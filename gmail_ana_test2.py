import pandas as pd

df = pd.read_csv("google.csv")

lst=[]
for i in df["pwd"]:
	lst.append(i)
lst_count={}
for i in lst:
	j=lst.count(i)
	if(i not in lst_count.keys()):
		lst_count[i]=j
	else:
		lst_count[i]+=j
k=0
l=0
for i,j in lst_count.items():
	if(l<j):
print("password keys and values the same number",len(lst_count.keys()))
print("Uniqe password number",len(df["pwd"].unique()))
print("higest Number of times",lst_count.values())
