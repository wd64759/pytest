import os
import requests
from bs4 import BeautifulSoup

f = open('config/stock_ref.props','r')
d = dict((x.split('=')[0:2]) for x in f.readlines())
print(d['stock_available_total'])

r = requests.get('https://gupiao.baidu.com/stock/sh601857.html')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
p_elem = soup.select_one('#app-wrap > div.stock-info > div > div.price.s-up > span:nth-of-type(2)')
print(p_elem)
