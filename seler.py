from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()
url2="https://www.selenium.dev/documentation/webdriver/elements/finders/"
url="https://debank.com/profile/0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f/history?chain=metis"
driver.get(url)


driver.implicitly_wait(20)
data=driver.find_elements(By.CLASS_NAME,"History_tableLine__3dtlF")
date=data[0].find_element(By.CLASS_NAME,"History_sinceTime__3JN2E").text

print(date)
driver.quit()

