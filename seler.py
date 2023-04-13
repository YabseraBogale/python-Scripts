from selenium import webdriver
from selenium.webdriver.common.by import By

def removeStr(str):
    lst=[]
    symbole=""
    for i in str:
        if i.isdigit() or i=="." or i==",":
            lst.append(i)
        else:
            symbole+=i

    return ["".join((i for i in lst)),symbole]
def scrape_debank(address, chain):
    
    driver = webdriver.Chrome()
    url=f'https://debank.com/profile/{address}/history?chain={chain}'
    driver.get(url)
    driver.implicitly_wait(20)
    data=driver.find_elements(By.CLASS_NAME,"History_tableLine__3dtlF")
    date=data[0].find_element(By.CLASS_NAME,"History_sinceTime__3JN2E").text

    print(date)
    driver.quit()

