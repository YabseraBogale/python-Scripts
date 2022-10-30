import pandas as pd

df = pd.read_csv("google.csv")

lst_letter={}
j=0
for i in df["pwd"]:
	if(type(i)==float):
		i=str(i)
	for k in i:
		if(k not in lst_letter):
			lst_letter[k]=1
		else:
			lst_letter[k]+=1
	print(i)
	"""
	if(j==5):
		break
	j+=1
	"""
