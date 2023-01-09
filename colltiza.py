import numpy as np
def Collatzsequence(number):
	lst=[]
	if number==1:
		lst.append(number)
		return lst
	while number!=1:
		if number%2==0:
			number=int(number/2)
			lst.append(number)
		else:
			number=int((3*number)+1)
			lst.append(number)

	return lst
	
numberstr=str(Collatzsequence(7)).replace("[","").replace("]","")
print(numberstr)

number=np.array(Collatzsequence(7))
print("Max number in The series is",number.max())
print("sum number in The series is",number.sum())
