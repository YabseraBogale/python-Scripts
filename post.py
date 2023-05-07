"""
import requests

# Fill in your details here to be posted to the login form.
payload = {
    'username': 'username',
    'password': 'password'
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('https://www.rollacity.co.uk/admin/', data=payload)
    # print the html returned or something more intelligent to see if it's a successful login page.
    print(s.get())

"""
from bs4 import BeautifulSoup as soup
import requests
from pprint import pprint
payload = {'username': 'Dkjkljlk', 'password': 'eU7SUegRP'}
url = 'https://www.hackthissite.org/user/login'
u=requests.post(url, json=payload)
pprint(u.text)


