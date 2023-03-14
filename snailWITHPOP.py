

"""
code failed for Higher level array works only for 3x3

"""
def normalpush(lst,Addlist):
	newlist=lst
	for i in Addlist[0]:
		newlist.append(i)
	
	return newlist

def addList(lst,Addlist):
	newList=lst
	i=0
	while i<len(Addlist[len(Addlist)-1]):
		newList.append(Addlist[len(Addlist)-1][i])
		i+=1
	return newList
	
def snailFunction(sanilArr):
	nail=sanilArr
	lst=nail[0]
	nail.pop(0)
	i=len(nail)-1
	count=0
	while i>=0:
		
		j=0
		while j<len(nail):
			num=nail[j].pop()
			lst.append(num)
			j+=1
		nail[j-1].reverse()
		lst=addList(lst,nail)
		nail.pop()
		k=len(nail)-1
		while k>=0:
			print(nail)
			num=nail[k].pop(0)
			lst.append(num)
			k-=1
		i-=1
		print(nail)

	return lst
	
snailarr=[
	[1,2,3,1,5],
	[4,5,6,4,6],
	[7,8,9,7,4],
	[7,8,9,7,2],
	[1,3,5,7,3]
]

print(snailFunction(snailarr))
