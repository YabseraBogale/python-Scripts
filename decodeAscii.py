#!/usr/bin/python3

print("give me a bottle of rum!")

file =open("file.txt","r")
code=""
for i in file.readlines():
	code+=chr(int(i))
	
print(code)
