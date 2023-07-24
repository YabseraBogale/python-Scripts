from bs4 import BeautifulSoup as bs
from requests import get
from sqlalchemy import create_engine, MetaData,String,Integer,Column,Table

def removesemiComma(lst):
    lst2=[]
    for i in lst:
        lst2.append(i.replace(',',''))
    return lst2


url='https://www.ssa.gov/oact/babynames/decades/century.html'
data=get(url).text
soup=bs(data,'html.parser')
db=create_engine('sqlite:///names',echo=True)

meta=MetaData()

name=Table(
    'name',meta,
    Column('Id',Integer,primary_key=True),
    Column('male',String),
    Column('male_number',Integer),
    Column('female',String),
    Column('female_number',String),
)

insert = name.insert()

lst=[]
for i in soup.find_all('tr'):
    tr=str(i.find_all('td')).replace('<td>','').replace('</td>','')
    if(tr.find('[')!=-1):
        lst.append(tr)

for i in range(2,102):
    lst2=list(lst[i].replace('[','').replace(']','').split(' '))
    names_list=removesemiComma(lst2[1:])
    insert=name.insert().values(
        male=names_list[0],
        male_number=names_list[1],
        female=names_list[2],
        female_number=names_list[3]
    )
    conn=db.connect()
    result=conn.execute(insert)