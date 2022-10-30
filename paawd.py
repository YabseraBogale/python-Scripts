word=open("file_1.txt","r")
count=0
for i in word.readlines():
	if(i.find("#")!=-1):
		count+=i.count("#")
print(count)
	
	
