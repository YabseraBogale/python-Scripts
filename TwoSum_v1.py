def twosum(lst):
	new_lst=lst
	two_sum=[]
	i=0
	j=0
	k=0
	while i<len(new_lst):
		while j<len(new_lst):
			while k<len(new_lst):
				temp=new_lst[k]+new_lst[j]
				print(temp,new_lst[i])
				if temp==new_lst[i]:
					two_sum.append([new_lst[k],new_lst[j]])
				k+=1
			j+=1
		i+=1
	return two_sum

print(twosum([1,2,3,4,5]))
					
