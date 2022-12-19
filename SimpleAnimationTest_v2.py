from time import sleep
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
	
def Game(num):
	game=num				
	i=0
	while i<20:
		lst1=game[i]
		if i==19:
			numbers=number()
			lst2=numbers[1]
		else:
			lst2=game[i+1]
		j=0
		while j<20:
			if j==19:
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

def numbertostring(times):
	tostring="\n\n\n\t\t\t\t\t\t "
	numbers=number()
	while times>0:
		numbers=Game(numbers)
		times-=1
	i=0
	while i<20:
		j=0
		while j<20:
			tostring+=f' {numbers[i][j]} '
			j+=1
		tostring+='\n\t\t\t\t\t\t '
		i+=1
	return tostring


number_of_times=int(input('''
		> Enter Number of Simulation for the same Data
		> is going to be fade to the recursive function (give low number): 

		'''))

def display():
	print("\n\n\n")
	print('\t\t\t\t\t\t',numbertostring(number_of_times))
	sleep(1)
	os.system('clear')
	return 'Running'
while True:
	print(display())
