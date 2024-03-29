"""

Complete the function/method (depending on the language) to return true/True when its argument is an array that has the same nesting structures and same corresponding length of nested arrays as the first array.

For example:
# should return True
same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )

# should return False 
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )

# should return True
same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )

# should return False
same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )

"""

def checker(lst1,lst2):
    lst1=str(lst1)
    lst2=str(lst2)
    if len(lst2)==len(lst1):
        return True
    return False

def same_structure_as(original,other):
    
    if  type(original)!=type(other):
        
        return False
    
    elif len(original)!=len(other):
        return False
    elif len(original)==len(other):
        i=0
        while i<len(other):
           if(type(other[i])!=type(original[i])):
                test=checker(other,original)
                print("here")
                if test==True:
                    return test
                return False
           elif type(other[i])==list or type(original[i])==list:
                if len(other[i])!=len(original[i]):
                    return False                     
           i+=1
   
    return True

print(same_structure_as([1,[1,1]],[2,[2,2]]))