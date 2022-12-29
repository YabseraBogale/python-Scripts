from requests import get
from bs4 import BeautifulSoup
import random
import os
from time import sleep
data=get("https://type.fit/api/quotes").json()
print(dir(data))
i=0
"""
while i<10:
	quote_author=data[random.randint(0,500)]
	print(quote_author['text'])
	print("\t\t\t\t",quote_author['author'])
	sleep(3)
	os.system("clear")
	i+=1

"""
