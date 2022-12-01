import random
import time
def MathsGame():
	number_one=random.randint(1,100)
	number_two=random.randint(1,100)
	operations_random=random.randint(0,4)
	operations=["+","-","/","*","%"]
	User_operations=operations[operations_random]
	print("\n\t",number_one,User_operations,number_two)
	User_Answer=float(input("\n\tEnter Your Answer: "))
	if(User_operations=="+"):
		Right_Answer=number_one+number_two
	elif(User_operations=="-"):
		Right_Answer=number_one-number_two
	elif(User_operations=="*"):
		Right_Answer=number_one*number_two
	elif(User_operations=="/"):
		Right_Answer=number_one/number_two
	elif(User_operations=="%"):
		Right_Answer=number_one%number_two
	if(User_Answer==round(Right_Answer,2)):
		return "\n\tThe Answer is Right"
	else:
		return "\n\tThe Answer is Wrong"



print("\tHow Quick can you Answer")
print(MathsGame())

