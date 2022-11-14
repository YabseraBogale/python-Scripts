def twosum(lst):
	new_lst=[]
	for i in lst:
		for j in lst:
			for k in lst:
				temp=k+j
				if temp==i and k!=j and [j,k] not in new_lst:
					new_lst.append([k,j])
	return new_lst
print(twosum([1,2,3,4,5,8,9,10]))

	

