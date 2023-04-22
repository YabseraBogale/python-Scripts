from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pprint import pprint
import re


def TtileList(data):
	lst=[]
	text=[]
	for i in data:
		lst.append(i)
	for i in lst:
		text.append(i.text)
	return text
def title(url):
	chrome_options = Options()
	chrome_options.add_experimental_option("detach",True)
	driver = webdriver.Chrome(options= chrome_options)
	driver.get(url)
	data=driver.find_elements(By.TAG_NAME,"title")
	lst=TtileList(data)
	driver.quit()
	return lst

if __name__=="__main__":
	#url=input("Enter Url: ")
	url="https://www.bbc.com/news/in-pictures-65346964"
	test=title(url)
	pprint(test)