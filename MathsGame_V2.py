import random
import time

def MathsGame():
	print("\tEnter \"E\" to Exit")
	Exit="E"
	life_point=3
	while Exit=="E":
		number_one=random.randint(1,10)
		number_two=random.randint(1,10)
		operations_random=random.randint(0,3)
		operations=["+","-","/","*"]
		User_operations=operations[operations_random]
		print("\n\tYour life point is",life_point)
		if(User_operations=="/"):
			print("\n\tYou can round to 2 certain values fractional points")
			print("\n\t",number_one,User_operations,number_two)
		else:
			print("\n\t",number_one,User_operations,number_two)
		User_Answer=input("\n\tEnter Your Answer: ")
		if(User_Answer=="E"):
			Exit="Exit"
		else:
			User_Answer=float(User_Answer)
			if(User_operations=="+"):
				Right_Answer=number_one+number_two
			elif(User_operations=="-"):
				Right_Answer=number_one-number_two
			elif(User_operations=="*"):
				Right_Answer=number_one*number_two
			elif(User_operations=="/"):
				Right_Answer=number_one/number_two
			if(User_Answer==round(Right_Answer,2)):
				life_point+=1
				print("\n\tThe Answer is Right")
			else:
				life_point-=1
				print("\n\tThe Answer is Wrong")
		if(life_point==0):
			return "\n\tGame over"


print("\tHow Quick can you Answer")
print(MathsGame())
