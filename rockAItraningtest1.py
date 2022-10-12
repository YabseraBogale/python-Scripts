#!/usr/bin/python3

import random
import numpy as np

class rockai():
	
	def __init__(self,n_feature,n_neural):
		self.weight=0.10*np.random.randn(n_feature,n_neural)
		self.bias=np.zeros((1,n_neural))
	def forword(self,inputs):
		self.out=np.dot(inputs,self.weight)+self.bias

def game(fromuser):
	num=random.randint(0,2)
	if(fromuser==num):
		print(num)
		return "Draw"
	elif(fromuser==0 and num==1):
		print(num)
		return "you win"
	elif(fromuser==1 and num==0):
		print(num)
		return "you loss"
	elif(fromuser==2 and num==1):
		print(num)
		return "you loss"
	elif(fromuser==1 and num==2):
		print(num)
		return "you win"
	elif(fromuser==2 and num==0):
		print(num)
		return "you win"
	print(num)
	return "you loss"

Game=True

while Game==True:
	
	print("Enter for rock 0:")
	print("Enter for scissor 1:")
	print("Enter for paper 2:")
	num=int(input("Enter "))
	print(game(num))
	print()
	print("Enter 1 to contniue or other to exit")
	take=int(input("Enter "))
	if(take!=1):
		Game=False
