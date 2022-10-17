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


				
stop_time=timeit.default_timer()
finish_time=round(stop_time-start_time,2)
print("Time taken to finsih program:",finish_time,"sec")
print("Total lines in the txt:",count_lines)
print("1st list no:",len(lst))
print("2ndlist list no:",len(lst2))
print("not in list_1:",len(lst)-len(lst2))
print("Example of 2ndlist:",lst2[100:105])


		
