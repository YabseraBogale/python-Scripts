import numpy as np
from random import randint

def random_ones(arr):
	return arr+randint(0,1)


arr=np.zeros((20,20))
arr2=np.zeros((20,20))

for i in arr:
	print(list(map(random_ones,i)))
	



