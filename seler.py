from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url="https://debank.com/profile/0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f/history?chain=metis"
driver.get(url)

title = driver.title
print(title)

driver.implicitly_wait(0.5)

driver.quit()