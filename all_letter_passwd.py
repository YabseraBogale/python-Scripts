import pandas as pd
words=open("file_1.txt")
j=0
lst=[]
lst2=[]
for i in words.readlines():
	word=i.split("@")
	pass_word=i.split(":")
	lst2.append(pass_word[1].split('\n')[0])
	lst.append(word[1].split(".")[0])
	
lst_passwd_letter={}
j=0
print("length 0f passwd list",len(lst2))
for i in lst2:
	for k in i:
		if(k not in lst_passwd_letter):
			lst_passwd_letter[k]=1
		else:
			lst_passwd_letter[k]+=1
ke=lst_passwd_letter.keys()
print(len(ke))
val=lst_passwd_letter.values()
df=pd.DataFrame({"Letter":ke,"Number":val})
print("Max used number",df["Number"].max())
print("Min used number",df["Number"].min())
print("Range used number",df["Number"].max()-df["Number"].min())
print(df["Number"].mode())
print("Mean used number",round(df["Number"].mean(),2))
print("Variance used number",round(df["Number"].var(),2))
print("Standerd deviation used number",round(df["Number"].std(),2))


	
