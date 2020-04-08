import requests
from bs4 import BeautifulSoup
from html.parser import HTMLParser

URL = 'https://www.amazon.com/Sony-Mirrorless-Digitial-3-0-Inch-16-50mm/dp/B00I8BICB2/ref=sr_1_1?dchild=1&keywords=sony+camera&qid=1586337304&sr=8-1'

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/80.0.3987.163 Chrome/80.0.3987.163 Safari/537.36'
}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = price[0:5]

print(converted_price)
print(title.strip())