def SelectionSortWithString(lst):
	new_lst=lst
	i=0
	j=0
	while i<(len(new_lst)-1):
		j=i+1
		while j<len(new_lst):
			if(new_lst[i]>new_lst[j]):
				temp=new_lst[i]
				new_lst[i]=new_lst[j]
				new_lst[j]=temp
			j+=1
		i+=1
	return new_lst
print(SelectionSortWithString(["Yabsera","Bogale","Abate","Addis"]))
