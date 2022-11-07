import numpy as np

File=open("file_1.txt","r")

lst={}

for i in File.readlines():
	i=i.split("@")[1].split(".")[0]
	if(i not in lst):
		lst[i]=1
	else:
		lst[i]+=1
	


print("hotmail",lst["hotmail"])
print("gmail",lst["gmail"])
print("yahoo",lst["yahoo"])
print("aol","aol" in lst.keys(),lst["aol"])
print("outlook","outlook" in lst.keys(),lst["outlook"])
print("icloud","icloud" in lst.keys(),lst["icloud"])

