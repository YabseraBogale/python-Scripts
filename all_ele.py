#!/usr/bin/python3

import timeit

start_time=timeit.default_timer()

words=open("enwords.txt")

lst=[]
count_lines=0
for i in words.readlines():
	count_lines+=1
	if(len(i)==6):
		i=i.split('\n')
		lst.append(i[0].lower())

lst2=[]
for i in lst:
	j=0
	ok=True
	while j <len(i):
		
		if(i.count(i[j])!=1):
			ok=False
			break
		else:
			ok=True
		j+=1
	if(ok==True):
		lst2.append(i)
for i in lst2:
	j=0
	while j < len(i):
		if(i.count(i[j])!=1):
			print(i)
		j+=1

lst3=[]
w1="a"
w2="i"
w3="e"
w4="o"
w5="u"	
for i in lst2:
	if(i.find(w1)==-1 and i.find(w2)==-1 and i.find(w5)==-1 and i.find(w3)==-1):
		lst3.append(i)
	
	
stop_time=timeit.default_timer()
finish_time=round(stop_time-start_time,2)
print("Time taken to finsih program:",finish_time,"sec")
print("Total lines in the txt:",count_lines)
print("1st list no:",len(lst))
print("2ndlist list no:",len(lst2))
print("3rdlist list no:",len(lst3))
print("not in list_1:",len(lst)-len(lst2))
print("Example of 3rdlist:")
print(lst3[10:15])


		

		
