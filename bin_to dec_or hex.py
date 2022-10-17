#!/usr/bin/python3
print("give me a bottle of rum!")

def change_into(Input):
	newstr=Input.split(" ")
	word=""
	for i in newstr:
		num=int(i,2)
		word+=chr(num)
	return word

def change_into8(Input):
	newstr=Input.split(" ")
	word=""
	for i in newstr:
		num=chr(oct(i))
		word+=num
	return word
	


	
	
print("Enter 2 for binary")
print("Enter 1 for decemial")
print("Enter 6 for hexa")
print("Enter 8 for octa")
Take=input("Enter: ")

if(Take=="2"):
	from_user=input("Enter binary string: ")
	print(change_into(from_user))
elif(Take=="1"):
	from_user=input("Enter decmail string: ")
	print(change_into8(from_user))
	
