from pprint import pprint
from bs4 import BeautifulSoup
from requests import get

def getContent(url,tag):
    
    return get(url).next



pprint(getContent('https://parade.com/945400/kelseypelzer/unique-baby-names/','strong'))