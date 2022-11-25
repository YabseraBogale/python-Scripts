def fib(num_range):
	lst=[0]
	i=0
	j=1
	while i<num_range:
		j=j+lst[i-1]
		lst.append(j)
		i+=1
		if(i==num_range):
			break
	return lst
print(fib(8))
