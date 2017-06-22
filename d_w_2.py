import requests as rq
from bs4 import BeautifulSoup as bs

url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = rq.get(url)
r_html = r.text
soup = bs(r_html, 'lxml')

text = soup.find_all('p')
print(text)
