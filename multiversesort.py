from pprint import pprint
import random
import os

def sortrandom(lst):
    random_list=[]
    i=0
    while i<=len(lst):
        if i==len(lst):
            return random_list
        num=lst[random.randint(0,len(lst)-1)]
        if num not in random_list:
            random_list.append(num)
            i+=1
        else:
            num=lst[random.randint(0,len(lst)-1)]
    return random_list
names=['Harold','Dylan','Arthur','Lawrenc395600','Jordan','Jesse','Bryan','Billy','Bruce','Gabriel']
list_of_number=[0,1,2,3,4,5]

count=0
"""
for i in range(0,3628800-1):
    test_lst=sortrandom(list_of_number)
    if test_lst==list_of_number:
        print("count at",count)
        break
    else:
        count+=1



list_lst=[1,2,3]
"""
truth_of_life={'True':0,'False':0}
test_list=[]

for i in range(0,720):
    lst=sortrandom(list_of_number)
    test_list.append(lst)
    truth=lst==list_of_number
    if truth==True:
        truth_of_life['True']+=1
    truth_of_life['False']+=1




#pprint(truth_of_life)

lst_of_one=[]
lst_of_greater=[]
for i in test_list:
    if(test_list.count(i)==1):
        lst_of_one.append(i)
    else:
        lst_of_greater.append(i)

print("one =",len(lst_of_one))
print("> one",len(lst_of_greater))