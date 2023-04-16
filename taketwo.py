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
    return "".join((i for i in lst))

def Info(data):
	dateTime=data.find_element(By.CLASS_NAME,"History_sinceTime__3JN2E").text
	txt_link=data.find_element(By.TAG_NAME,"a").get_attribute("href")
	return [dateTime,txt_link]

def FunctionProtocol(data):
	function=data.find_element(By.CLASS_NAME,"History_interAddressExplain__2VXp7").text
	protocol=data.find_element(By.CLASS_NAME,"History_greyText__KIi2L").get_attribute("href")
	return [function,protocol]

def Token_1(data):
	isThere=data.find_element(By.CLASS_NAME,"History_tokenChange__b7tZ9").text
	if(len(isThere)==0):
		return [None,None]
	address=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div[2]').get_attribute("data-id")
	symbole=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div[2]').get_attribute("data-name")
	amount_usd=data.find_element(By.CLASS_NAME,"History_tokenPrice__2SUw_").text.replace("(","").replace(")","").replace("$","")
	a=data.find_element(By.CLASS_NAME,"History_tokenSymbol__2LgpT").text
	sign=data.find_element(By.CLASS_NAME,"History_tokenChangeText__2dydx").text
	amount=sign[0]+removeStr(a)
	return [address,symbole,amount_usd,amount]

def Token_2(data):
	isThere=data.find_element(By.CLASS_NAME,"History_tokenChange__b7tZ9").text
	if(len(isThere)==0):
		return [None,None]
	address=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]').get_attribute("data-id")
	symbole=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]').get_attribute("data-name")
	sign=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/span').text
	a=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/span[2]').text
	amount=sign[0]+removeStr(a)
	amount_usd=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/span[3]').text.replace("(","").replace(")","").replace("$","")
	return [address,symbole,amount,amount_usd]


def TestToken(data):
	isThere=data.find_element(By.CLASS_NAME,"History_tokenChange__b7tZ9").text
	if(len(isThere)==0):
		return [None,None]
	elements=data.find_elements(By.CLASS_NAME,"History_proposalFlag__1NcfY")
	return elements
	
def loopOfData(data):
	lst=[]
	for i in data:
		info=Info(i)
		function=FunctionProtocol(i)
		token_1=Token_1(i)
		token_2=Token_2(i)
		lst.append(token_2)
	return lst

def scrape_debank(address,chain):
	driver=webdriver.Chrome()
	url=f"https://debank.com/profile/{address}/history?chain={chain}"
	driver.get(url)
	driver.implicitly_wait(30)
	data=driver.find_elements(By.CLASS_NAME,"History_tableLine__3dtlF")
	data=loopOfData(data)	
	#data=Token_2(data[1])
	return data

if __name__=="__main__":
	test=scrape_debank("0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f","metis")
	print(test[1])
