#!/usr/bin/python3

print("give me a bottle of rum!")

file_in=open("file_1.txt","r")
poss=""
lst=[]
lst2=[]
for i in file_in.readlines():
	lst2.append(i)
	for j in i:
		if(j!="@"):
			poss+=j
		else:
			lst.append(poss)
			poss=""
			break		
print(lst[0:4])
print(lst2[0:4])
