from selenium import webdriver
from selenium.webdriver.common.by import By


def removeStr(str):
    lst=[]
    for i in str:
        if i.isdigit() or i=="." or i==",":
            lst.append(i)
        else:
            break
    return "".join((i for i in lst))

def token1(data):
	address=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div[2]").get_attribute("data-id")
	symbole=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div[2]").get_attribute("data-name")
	sign=data.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[1]/div[2]/span/span[1]').text
	a=data.find_element(By.CLASS_NAME,"History_tokenSymbol__2LgpT").text
	amount=sign+removeStr(a)
	amount_usd=data.find_element(By.CLASS_NAME,"History_tokenPrice__2SUw_").text.replace("(","").replace(")","").replace("$","")
	return {"address":address,"symbole":symbole,"amount":amount,"amount_usd":amount_usd}


def token2(data):
	address=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]").get_attribute("data-id")
	symbole=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]").get_attribute("data-name")
	sign=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/span[1]").text
	a=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/span[2]").text
	amount=sign+removeStr(a)
	amount_usd=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]/span/span[3]").text.replace("(","").replace(")","").replace("$","")
	return {"address":address,"symbole":symbole,"amount":amount,"amount_usd":amount_usd}

def Gas(data):
	token=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[3]/div/div[2]/div[2]").get_attribute("data-token-chain")
	a=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[4]/div/span[2]").text
	amount=removeStr(a)
	amount_usd=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[4]/div/span[2]/span").text.replace("(","").replace(")","").replace("$","")
	return {"token":token,"amount":amount,"amount_usd":amount_usd}

def info(data):
	dateTime=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[1]/div[1]").text
	txt_link=data.find_element(By.CLASS_NAME,"History_txStatus__2PzNQ").find_element(By.TAG_NAME,"a").get_attribute("href")
	function=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]").text
	protocol=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/a").text
	address=data.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/div[2]/div[2]/div/div/div[2]/a").get_attribute("href")
	return {"datetime":dateTime,"txt_link":txt_link,"function":function,"protocol":protocol,"address":address}
	
def loopOfData(data):
	lst=[]
	count=0
	for i in data:
		Token1=token1(i)
		Token2=token2(i)
		gas=Gas(i)
		Info=info(i)
		Info["token1"]=Token1
		Info["token2"]=Token2
		Info["gas"]=gas
		lst.append(Info)
		count+=1
	return lst
	
def testLoopData(data):
	
	for i in data:
		function=i.find_element(By.CLASS_NAME,"History_ellipsis__rfBNq").is_displayed()
		if(function==True):
			function=i.find_element(By.CLASS_NAME,"History_ellipsis__rfBNq").text
			print(function)
		else:
			function=i.find_element(By.CLASS_NAME,"History_interAddressExplain__2VXp7").text
			print(function)
		
			
	return "done"
	
	
def scrape_debank(address,chain):
	driver=webdriver.Chrome()
	url=f"https://debank.com/profile/{address}/history?chain={chain}"
	driver.get(url)
	driver.implicitly_wait(30)
	data=driver.find_elements(By.CLASS_NAME,"History_tableLine__3dtlF")
	#data=loopOfData(data)
	#data=testLoopData(data)
	return data[5].find_element(By.CLASS_NAME,"History_interAddressExplain__2VXp7").text


	
	
if __name__=="__main__":
	test=scrape_debank("0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f","metis")
	print(test)


