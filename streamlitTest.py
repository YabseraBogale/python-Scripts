import time
import streamlit as st
from time import sleep
import random
import numpy as np
import os
import matplotlib.pyplot as plt


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

def Game(numbers):
	game=numbers			
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
 
def Change(numbers):
	lst=str(np.array(numbers))
	lst=lst.replace('0','🟩').replace('[','').replace(']','').replace('1','⬜').replace('\n','\n\t\t\t\t\t\t')
	return '\n\n\n\t\t\t\t\t\t '+lst
 
with st.empty():
	while True:
		numbers=Change(Game(number()))
		st.text(numbers)
		sleep(1)
