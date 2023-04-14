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

driver = webdriver.Chrome()
url="https://debank.com/profile/0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f/history?chain=metis"
driver.get(url)
driver.implicitly_wait(30)
data=driver.find_elements(By.CLASS_NAME,"History_tableLine__3dtlF")
# done 
# date=data[0].find_element(By.CLASS_NAME,"History_sinceTime__3JN2E").text
# done
# txt_link=data[0].find_element(By.CLASS_NAME,"History_txStatus__2PzNQ").find_element(By.TAG_NAME,"a").get_attribute("href")
# done
# function=data[0].find_element(By.CLASS_NAME,"History_interAddressExplain__2VXp7").find_element(By.CLASS_NAME,"History_ellipsis__rfBNq").text
#done
# protocol=data[0].find_element(By.CLASS_NAME,"History_greyText__KIi2L").text
# done 
# sign=data[0].find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div[2]/span/span[1]').text
#done
# a=data[0].find_element(By.CLASS_NAME,"History_tokenSymbol__2LgpT").text
# done
# amount=sign+removeStr(a)[0]
# done
# symbole=removeStr(a)[1]
# done
# amount_usd=data[0].find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div[2]/span/span[3]')
# done
# amount_usd=amount_usd.text.replace('(',"").replace(')',"").replace("$","")
# token 1 is finshed
Address=data[0].find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]').get_attribute("data-id")
print(Address)
driver.quit()
