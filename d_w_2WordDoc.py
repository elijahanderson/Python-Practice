import requests as rq
from bs4 import BeautifulSoup as bs
import docx

url = 'http://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = rq.get(url)
soup = bs(r.text, 'lxml')

print(str(soup))
