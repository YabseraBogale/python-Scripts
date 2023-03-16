import numpy as np

def normalPush(array):
    lst=[]
    i=0
    if(len(array)==1):
        return array[0]
    while i<=len(array)-2:
        lst.append(array[i])
        i+=1
    maxnum=np.array(lst).max()
    
    return maxnum

def longest_slide_down(pyramid):
    # TODO: write some code...
    py=pyramid
    lst=[]
    sum=0
    for i in py:
        lst.append(len(i))
    for i in lst:
        sum+=normalPush(py[i-1])
    return sum


print(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))
