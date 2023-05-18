"""

Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)
"john McClane" --> "McClane john"


"""


def name_shuffler(str_):
    #your code here
    lst=str_.split(" ")
    return lst[1]+" "+lst[0]
    
   

print(name_shuffler("john McClane"))