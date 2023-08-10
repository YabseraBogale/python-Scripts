from sqlalchemy import Table, MetaData, Column, Integer, String
import sqlalchemy as db
engine=db.create_engine('sqlite:///User_Post.db',echo=True)

meta =MetaData()

student = Table(
    'Name_of_table',meta,
    Column('Can_be_Integer',Integer,primary_key=True),
    Column('can_be_string',String),
    Column('cab_be_integer',Integer,primary_key=True)
)

meta.create_all(engine)


con=engine.connect()

con.execute(student.insert(),[
    {'Can_be_Integer':1,'can_be_string':'hello','cab_be_integer':32},
    {'Can_be_Integer':52,'can_be_string':'World','cab_be_integer':25},
    {'Can_be_Integer':2,'can_be_string':'works ?','cab_be_integer':2},
])


result=con.execute(student.select())
for i in result:
    print(i)