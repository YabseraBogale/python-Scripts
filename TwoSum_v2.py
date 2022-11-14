"""
doesn't work
"""
def twosum(lst):
	new_lst=[]
	for i in lst:
		for k in lst:
			for j in lst:
				temp=k+j
				if temp==i:
					if [k,j] not in new_lst or [j,k] not in new_lst:
						new_lst.append([k,j])
	return new_lst
print(twosum([1,2,3,4,5]))
