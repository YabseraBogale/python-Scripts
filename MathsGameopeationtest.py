import random
operations=["+","-","/","*","%"]
test_opeation={"+":0,"-":0,"%":0,"/":0,"*":0}
j=0
while j<50000:
	j+=1
	operations_random=random.randint(0,4)
	if(operations[operations_random] in test_opeation):
		test_opeation[operations[operations_random]]+=1
print(test_opeation)
	 
