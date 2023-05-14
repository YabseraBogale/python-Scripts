def multiplication_table(size):
    lst=[]
    i=1
    while size>=i:
        j=1
        num=1
        lst2=[]
        while j<=size:
            
            lst2.append(num)
            num=j*i
            j+=1
        i+=1
        print(lst2)
    return lst

print(multiplication_table(3))