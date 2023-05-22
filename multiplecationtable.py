
from pprint import pprint
def table(num):
    lst_row=[]
    lst_ans=[]
    for i in range(1,num+1):
        for j in range(1,num+1):
            lst_row.append(i*j)
        lst_ans.append(lst_row)
        lst_row=[]
    return lst_ans

pprint(table(10))
