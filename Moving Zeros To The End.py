"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""
def move_zeros(lst):
    zero=[]
    nonzero=[]
    combined=[]
    for i in lst:
        if i==0:
            zero.append(i)
        else:
            nonzero.append(i)
    for i in nonzero:
        combined.append(i)
    for i in zero:
        combined.append(i)
    return combined

print(move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))
