import random
"""

1	January	    Jan.	31	winter
2	February	Feb.	28/29
3	March	    Mar.	31	spring
4	April	    Apr.	30
5	May	        May.    31
6	June	    Jun.	30	summer
7	July	    Jul.	31
8	August	    Aug.	31
9	September	Sep.	30	autumn
10	October	    Oct.	31
11	November	Nov.	30
12	December	Dec.	31	winter


"""
def printShow(lst):
	i=0
	j=0
	while i <len(lst):
		i+=4
		print("\t",lst[j:i])
		j=i
	return f"\tNumber of Dates {len(lst)}\n"
def GenNumberofDOB(num):
	lst_of_31=["Jan.","Mar.","May.","Jul.","Aug.","Oct.","Dec."]
	lst_of_30=["Apr.","Jun.","Sep.","Nov."]
	lst_of_28=["Feb."]
	lst_made=[]
	numberofTimes=num
	while num>0:
		for i in lst_of_31:
			lst_made.append(i+" "+str(random.randint(1,31)))
		for i in lst_of_31:
			lst_made.append(i+" "+str(random.randint(1,31)))
		if num%4==0:
			lst_made.append(i+" "+str(random.randint(1,29)))
		else:
			lst_made.append(i+" "+str(random.randint(1,28)))
		num-=1
	lst_out=[]
	while numberofTimes>0:
		lst_out.append(lst_made[random.randint(0,len(lst_made)-1)])
		numberofTimes-=1
	return lst_out

def Aanlizing():
	print("\tHow many birthdays shall I generate?  (Enter \"E\" to Exit)")
	num=input("\t>")
	while num!="E":
		if num=="E":
			return "\tExiting"
		else:
			if num.isdecimal()==True:
				Date=GenNumberofDOB(int(num))
				the_same_Dob=0
				lst_of_thesame={}
				for i in Date:
					if Date.count(i)>1:
						the_same_Dob+=1
						if i not in lst_of_thesame:
							lst_of_thesame[i]=Date.count(i)
				numberofpeople=the_same_Dob
				the_same_Dob=round((the_same_Dob/len(Date))*100,2)
				print("\n\t","Geneated Dates")
				print(printShow(Date))
				print("\tBirthDays which people have the same day in the data",lst_of_thesame)
				print(f"\tThe Percentage of people having the same birthday {the_same_Dob}%")
				print("\tThe Number of people",numberofpeople)
				print("\n\tHow many birthdays shall I generate?  (Enter \"E\" to Exit)")
				num=input("\t>")
				if num=="E":
					return "\tExiting"
			else:
				print("\tEnter Decimal Digit")
				Aanlizing()
if __name__=="__main__":
	print(Aanlizing())
