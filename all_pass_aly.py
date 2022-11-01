word=open("file_1.txt","r")
def check(file_in):
	c=0
	lst_count_pass={}
	longest_password={}
	for i in word.readlines():
		k=i.split(":")[1].split("\n")[0]
		if(len(k)>10):
			longest_password[k]=len(k)
		if(k==""):
			continue
		elif(k not in lst_count_pass.keys()):
			lst_count_pass[k]=1
		else:
			lst_count_pass[k]+=1
	return len(longest_password.keys()) 
print(check(word))

