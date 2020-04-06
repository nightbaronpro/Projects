import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.de/Sony-Vollformat-Digitalkamera-Megapixel-LC-Display/dp/B00Q2KEVA2/ref=sr_1_1_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=35ZIPRGCAOOGQ&dchild=1&keywords=sony+alpha+ilce-7m3&qid=1586166538&sprefix=sony+alpha+ilc%2Caps%2C492&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExVTVQU0tXTTBGTkdDJmVuY3J5cHRlZElkPUEwNzMyMDAxMk81RFozSUkzQTZSUiZlbmNyeXB0ZWRBZElkPUEwOTkzMjM2MzFGMFFLMUw4MTZVUCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.163 Chrome/80.0.3987.163 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="buyNew_noncbb").get_text()
converted_price = float(price[0:5])

print(converted_price)
print(title.strip())