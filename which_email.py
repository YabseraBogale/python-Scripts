import numpy as np

File=open("file_1.txt","r")

lst={}

for i in File.readlines():
	i=i.split("@")[1].split(".")[0]
	if(i not in lst):
		lst[i]=1
	else:
		lst[i]+=1
	
	
	
lst2=[i for i in lst.values()]
lst2=np.array(lst2).max()

for i,j in lst.items():
	if(j>1000):
		print(i,j)
print("mean",lst2.mean())
print("sum",lst2.sum())
print("median",np.median(lst2))


