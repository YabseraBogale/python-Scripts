#!/usr/bin/python3
import pandas as pd

print("give me a bottle of rum!")

words=open("file_2.txt")

j=0
lst=[]
lst2=[]
for i in words.readlines():
	word=i.split("@")
	pass_word=i.split(":")
	lst2.append(pass_word[1].split('\n')[0])
	lst.append(word[1].split(".")[0])

df=pd.DataFrame({"Email":lst,"pwd":lst2})
google_df=df[df["Email"]=="gmail"].reset_index().drop(["index"],axis=1)
google_df.to_csv("google.csv")
print(google_df.plot())

