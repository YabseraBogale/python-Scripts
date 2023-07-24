from bs4 import BeautifulSoup as bs
from requests import get
from pprint import pprint

import sqlite3

url='https://www.ssa.gov/oact/babynames/decades/century.html'

data=get(url).text

soup=bs(data,'html.parser')
test=soup.find_all('tr')[3].find_all('td')

lst=[]
for i in soup.find_all('tr'):
    tr=str(i.find_all('td')).replace('<td>','').replace('</td>','')
    if(tr.find('[')!=-1):
        lst.append(tr)

def removesemiComma(lst):
    lst2=[]
    for i in lst:
        lst2.append(i.replace(',',''))
    return lst2

for i in range(2,102):
    lst2=list(lst[i].replace('[','').replace(']','').split(' '))
    print(removesemiComma(lst2[1:]))


