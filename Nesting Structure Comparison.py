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



def same_structure_as(original,other):
            
    if len(original)!=len(other):
        return False
    elif len(original)==len(other):
        i=0
        while i<len(other):
           if(type(other[i])!=type(original[i])):
                return False
           if type(other[i])==list or type(original[i])==list:
                if len(other[i])!=len(original[i]):
                    return False
               
                    
                    
           i+=1
    return True

print(same_structure_as([1,[1,1]],[2,[2,2]]))