
from bs4 import BeautifulSoup as sp
from requests import get
import sqlite3

con=sqlite3.connect('name.db')

pointer=con.cursor()

pointer.execute("select * from user_name")
result=pointer.fetchall()

lst=[]
for i in result:
    lst.append(i[0])
    if len(lst)==20:
        break

print(lst)