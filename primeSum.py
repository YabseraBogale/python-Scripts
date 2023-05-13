
"""
    this code is not optimzided enough
"""
def primeSum(limit):
    num=limit+1
    sum=0
    i=2
    while i<num:
        j=2
        yes_no=False
        while j<i:
            if i%j==0:
                yes_no=True
            j+=1
        if yes_no==False:
            sum+=i
        i+=1
        
    return sum

print(primeSum(10))