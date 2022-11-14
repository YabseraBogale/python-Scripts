"""
doesn't work
"""
def twosum(lst):
	new_lst=[]
	for i in lst:
		for j in lst:
			for k in lst:
				temp=k+j
				if temp==i and k!=j :
					s=str(k)+"+"+str(j)+"="+str(temp)
					new_lst.append(s)
	return new_lst

print(twosum([1,2,3,4,5]))
lst=[1,2,3,4,5]

