import math
def comp(array1, array2):
    # your code
    state=False
    lst=[]
    for j in array2:
        lst.append(int(math.sqrt(j)))
    i=0
    lst=sorted(lst)
    lst2=sorted(array1)
    while i<len(lst2):
        if(lst[i]==lst2[i]):
           state=True
		   i+=1
        else:
            return False
            
    return state
    
a = [121, 144, 19, 161, 19, 144, 19, 11]  
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]	
print(comp(a,b))
