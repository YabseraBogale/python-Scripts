
"""
	state "1" is for dead
	state "0" is for alive

"""

from time import sleep
import random
import numpy as np
import os
import matplotlib.pyplot as plt


def number():
	lst_of_lst=[]
	i=0
	while i<30:
		j=0
		lst=[]
		while j<30:
			num=random.randint(0,1)
			lst.append(num)
			j+=1
		lst_of_lst.append(lst)
		i+=1
	return lst_of_lst

def Game(numbers):
	game=numbers			
	i=0
	while i<30:
		lst1=game[i]
		if i==29:
			numbers=number()
			lst2=numbers[1]
		else:
			lst2=game[i+1]
		j=0
		while j<30:
			if j==29:
				state=lst1[j]+lst2[j]+lst2[j]
				break
			else:
				state=lst1[j+1]+lst2[j]+lst2[j+1]
				if state<2:
					game[i][j]=1
				elif state==2:
					game[i][j]=lst1[j]
				elif state==3 and lst1[j]==1:
					game[i][j]=0
				elif state==3 and lst1[j]==0:
					game[i][j]=1
				j+=1			
		i+=1
	return game
 
def Change(numbers):
	lst=np.array(numbers)
	i=0
	j=1
	while i<30:
		x=lst[i]
		y=lst[j]
		i+=1
		j+=1
		if j==30:
			j=29
		plt.plot(x,y)
	return plt.show()
 
def display():
	
	numbers=number()
	while True:
		num=1
		if num==1:
			numbers=Game(numbers)
		else:
			numbers=number()
		
		print(Change(numbers),)
		sleep(2)
		os.system('clear')

print(display())
