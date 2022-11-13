def SelectionSort(lst):
	new_lst=lst
	i=0
	temp=0
	while i<len(lst)-1:
		j=i+1
		while j<len(lst):
			if(new_lst[i]>new_lst[j]):
				temp=new_lst[i]
				new_lst[i]=new_lst[j]
				new_lst[j]=temp
			j+=1
		i+=1
	return new_lst
print(SelectionSort([1,5,3,2,7,9]))

