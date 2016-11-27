import os
import requests
import time
from bs4 import BeautifulSoup

f = open('config/stock_ref.props','r')
d = dict((x.split('=')[0:2]) for x in f.readlines())
# print(d['stock_available_total'])

t1 = time.time()
r = requests.get('https://gupiao.baidu.com/stock/sh510130.html')
# r.close()

r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
# p_elem = soup.select_one('#app-wrap > div.stock-info > div > div.price.s-up > span:nth-of-type(2)')
# p_elem = soup.select_one("dd.s-up")
# p_elem = soup.find('dt', text='最高')
p_elem = soup.select_one('#app-wrap > div.stock-info > div > div.bets-content')
p_elem = p_elem.find('dt', text='最高')
n = p_elem.find_next_sibling('dd')
t2 = time.time()
# print(n, ' time cost:', str(t2 - t1) )


