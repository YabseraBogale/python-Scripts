"""
This function is has failed don't do it

"""
def SelectionSortWithString(lst):
	new_lst=lst
	i=0
	j=0
	while i<(len(new_lst)-1) or j<len(new_lst):
		j=i+1
		if(new_lst[i]>new_lst[j]):
			temp=new_lst[i]
			new_lst[i]=new_lst[j]
			new_lst[j]=temp
		j+=1
		i+=1
	return new_lst
lst=["Addis","abebe","sdf"]
print(SelectionSortWithString(lst))
