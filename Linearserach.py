def Linearsearch(lst,number):
	newlst=sorted(lst)
	print("After sortion list is ",newlst)
	i=0
	while i<len(newlst):
		if newlst[i]==number:
			print(number," is at position ",i)
			return "Done"
		else:
			i+=1
	return "Not found"
	
lst=[1,3,5,-10,-2,4,2]
print(Linearsearch(lst,3))
