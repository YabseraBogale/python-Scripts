def grade(lst):
        avg=sum(lst)/len(lst)
        Sun=sum(lst)
        g=""
        if avg>=90 and avg<=100:
                g="grade=A+"
        elif avg>=80 and avg<=89:
                g="grade=A"
        elif avg>=70 and avg<=79:
                g="grade=B+"
        elif avg>=60 and avg<=69:
                g="grade=B"
        elif avg>=50 and avg<=59:
                g="grade=C+"
        elif avg>=40 and avg<=49:
                g="grade=C"
        elif avg>=30 and avg<=39:
                g="grade=D+"
        elif avg>=20 and avg<=29:
                g="grade=D"
        elif avg>=0 and avg<=19:
                g="grade=F"
        print("Total:",Sun)
        print("Average:",avg)
        return g
subno=int(input("enter number of subjects:"))
lst=[]
while subno>0:
        mark=float(input("Enter number "))
        if(mark>100 or mark<0):
                print("Mark invalid")
        else:
                lst.append(mark)
                subno-=1
print(grade(lst))
