def BinearySearch(lst,no):
	low=0
	up=len(lst)-1
	i=round((low+up)/2)
	count=0
	while i<len(lst):
		if lst[i]==no:
			return f"found at postion {i}"
		elif lst[i]>no:
			up=i-1
			i=round((up+low)/2)
			count+=1
		else:
			low=i+1
			i=round((up+low)/2)
			count+=1
		if count>len(lst):
			return "Not in list"
print(BinearySearch([1,2,3,5,14,45],4))
