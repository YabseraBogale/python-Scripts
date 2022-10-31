import pandas as pd
df =pd.read_csv("google.csv").drop(["Unnamed: 0"],axis=1)
pwdun=df["pwd"].unique()
allpwd=len(df["pwd"])
print("Number of unique password",len(pwdun))
print("All Number password",allpwd)
print("Number of people who have the same password",allpwd-len(pwdun))
lst=[]
for i in pwdun:
	lst.append(i)
count=0
lst_same=[]
for i in df["pwd"]:
	i=str(i)
	if(i in lst):
		count+=1
	else:
		lst_same.append(i)
print("All count of i in unique",count)
print("is the i counted in pw unique equal to count",len(pwdun)==count,"Diffrence",len(pwdun)-count)

	
