import time
import os
import random

def number():
	lst_of_lst=[]
	i=0
	while i<20:
		j=0
		lst=[]
		while j<20:
			num=random.randint(0,1)
			lst.append(num)
			j+=1
		lst_of_lst.append(lst)
		i+=1
	return lst_of_lst

def numbertostring():
	tostring=""
	numbers=number()
	for i in numbers[random.randint(0,19)]:
		tostring+=f'|{i}|'
	return tostring


def Cell():
	
	cell=('-'*60)+'\n'+(f'|{num}|'*20)+'\n'+('-'*60)
	return cell

i=0
while i<4:
	print(numbertostring())
	i+=1
