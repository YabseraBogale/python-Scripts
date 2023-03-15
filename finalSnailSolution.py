def snailFunction(arr):
	snail=arr
	lst=snail[0]
	snail.pop(0)
	i=0
	while i<=len(snail)-1:
		lst.append(snail[i].pop(len(snail[i])-1))
		i+=1
	k=len(snail[i-1])-1
	while k>=0:
		lst.append(snail[i-1].pop(k))
		k-=1
	snail.pop(i-1)
	i=len(snail)-1
	while i>=0:
		lst.append(snail[i].pop(k+1))
		i-=1
	return [lst,snail]
	
def pushNumbers(lst,numlist):
	newlst=lst
	for i in numlist[0]:
		newlst.append(i)
	return newlst


def finalSnail(arr):
	if(len(arr)==1 and arr[0]==[]):
		return []
	numlist=snailFunction(arr)
	if(numlist[1]==[]):
		return numlist[0]
	else:
		if(len(arr)%2!=0):
			lst=numlist[0]
			while len(numlist[1])!=1:
				numlist=snailFunction(numlist[1])
				lst=pushNumbers(lst,numlist)
			lst.append(numlist[1][0][0])
		else:
			lst=numlist[0]
			while numlist[1]!=[]:
				numlist=snailFunction(numlist[1])
				lst=pushNumbers(lst,numlist)
			
			
	return lst
def snail(snail_map):
    if len(snail_map)==1:
        return snail_map[0]
    answer=finalSnail(snail_map)
    return answer
