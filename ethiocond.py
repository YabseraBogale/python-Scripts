file_in=open("ethiocond.txt","r")
file_in2=open("ethio40_60.txt","r")
 
def Search(file_In,item1,item2):
	lst={}
	for i in file_In.readlines():
		if(i.find(item1)!=-1):
			if item1 not in lst:
				lst[item1]=1
			else:
				lst[item1]+=1
		elif(i.find(item2)!=-1):
			if item2 not in lst:
				lst[item2]=1
			else:
				lst[item2]+=1
	lst['total']=lst[item1]+lst[item2]
	if(lst[item1]>lst[item2]):
		lst['d/f']=lst[item1]-lst[item2]
		lst['d/f']=round((lst['d/f']/lst['total'])*100,2)
	else:
		lst['d/f']=lst[item2]-lst[item1]
		lst['d/f']=round((lst['d/f']/lst['total'])*100,2)
	lst[item1]=str(round((lst[item1]/lst['total'])*100,2))+"%"
	lst[item2]=str(round((lst[item2]/lst['total'])*100,2))+"%"
	return lst
result1=Search(file_in,'ሴት','ወንድ')
result2=Search(file_in2,'ሴት','ወንድ')
print(result1)
print(result2)
print("Total People who won ",result1['total']+result2['total'])

