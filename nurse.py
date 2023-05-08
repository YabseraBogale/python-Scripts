import sqlite3 

con=sqlite3.Connection("nurse.db")

cur=con.cursor()

cur.execute("""

select * from nurse

""")

con.commit()

result=cur.fetchone()

print(result)