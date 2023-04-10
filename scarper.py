"""

don't use for react app


"""

from requests import get
from bs4 import BeautifulSoup as Bs
from pprint import pprint



def scrappe(html_string):
    soup=Bs(html_string,'html.parser')
    return soup.find_all("div",class_="History_sinceTime__3JN2E")

def scrape_debank(address,chain):
    url=f"https://debank.com/profile/{address}/history?chain={chain}"
    bank=get(url).content
    return bank

test=scrappe(scrape_debank('0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f','metis'))
testone=scrape_debank('0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f','metis')
pprint(str(testone).find("root"))
#print(test)






