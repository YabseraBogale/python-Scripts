"""
doesn't work
"""
def twosum(lst):
	new_lst=[]
	i=0
	j=0
	k=0
	while i<len(lst):
		j=i+1
		print(i,k,j)
		while j<len(lst):
			k=j+1
			print(i,k,j)
			while k<len(lst):
				temp=lst[k]+lst[j]
				print(i,k,j,temp)
				if temp==lst[i]:
					new_lst.append(lst[k],lst[j])
				k+=1
			j+=1
		i+=1
	return new_lst
	

lst=[1,2,3,4,5]
print(twosum(lst))
