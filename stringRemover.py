def removeStr(str):
    lst=[]
    symbole=""
    for i in str:
        if i.isdigit() or i=="." or i==",":
            lst.append(i)
        else:
            symbole+=i
    if(lst[len(lst)-1].isdigit()):
        return ["".join((i for i in lst)),symbole]
    lst.remove(lst[len(lst)-1])
    return ["".join((i for i in lst)),symbole]

print(removeStr("2,168.2607 m.USDC"))

