import re

def mapping(lst):
    i=0
    lst2=[]
    while i < len(lst):
        lst2.append(lst[i].lower())
        i+=1
    return lst2

def joining(lst):
    result=""
    i=0
    while i<len(lst):
        #print(lst[i])
        if(i==len(lst)-1):
            result+=lst[i]
            break
        result+=lst[i]+"_"
        i+=1
    return result
  
def to_underscore(string):
    # your code here
    if(type(string)!=str):
        return str(string)
    result=re.findall('[A-Z][^A-Z]*',string)
    result=mapping(result)
    return joining(result)

print(to_underscore("TestController"))
print(to_underscore("MoviesAndBooks"))
print(to_underscore("App7Test"))
print(to_underscore(1))
