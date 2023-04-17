from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= chrome_options)
driver.get("https://debank.com/profile/0x0c1a3e4e1c3da4c89582dfa1afa87a1853d7f78f/history?chain=metis")
