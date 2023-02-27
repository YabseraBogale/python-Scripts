"""
Snail map going on but still not solved
"""
def snail(snail_map):
    lst=snail_map
    snail_lst=[]
    j=0
    i=0
    if(len(snail_map)==1):
        return snail_map
    else:
        snail_lst.append(lst[i])
        while i<len(snail_map):
            poplst=lst.pop(j)
            print(poplst)
            i+=1
    return "Done"
    
    
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
print(snail(array))
