from math import factorial

def zeros(n):
    zero=str(factorial(n))
    count=0
    i=len(zero)-1
    while 0<=i:
        if zero[i]=="0":
            count+=1
        else:
            break
        i-=1
    
    return count

print(zeros(100000))
