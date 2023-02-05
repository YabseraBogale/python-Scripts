import sqlite3



see="""
	select * from userinfo
"""

db= sqlite3.connect('UserDatabase.db')

cur=db.cursor()

#cur.execute(insert)
cur.execute(see)

row=cur.fetchall()

for i in row:
	print(i)
