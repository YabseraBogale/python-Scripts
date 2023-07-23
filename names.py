from bs4 import BeautifulSoup as bs
from requests import get

import sqlite3

url='https://www.ssa.gov/oact/babynames/decades/century.html'

data=get(url).text

soup=bs(data,'html.parser')
test=soup.find_all('tr')[3].find_all('td')
print(test[1],test[3])
lst=[]
for i in soup.find_all('tr'):
    tr=str(i.find_all('td')).replace('<td>','').replace('</td>','')
    if(tr.find('[')!=-1):
        lst.append(tr)

for i in range(2,102):
    print(lst[i])



