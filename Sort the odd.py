"""
You will be given an array of numbers. 
You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
"""

def sort_array(source_array):
    # Return a sorted array.
    lst=[]
    place=[]
    for i in source_array:
        if(i%2!=0):
            lst.append(i)
            place.append(source_array.index(i))
    lst=sorted(lst)
    print(source_array)
    lst2=source_array
    i=0
    j=0
    while i < len(lst2):
        if lst2[i]%2!=0:
            lst2[i]=lst[j]
            j+=1
        i+=1
    return lst2
    

    
print(sort_array([5, 3, 2, 8, 1, 4]))
    
