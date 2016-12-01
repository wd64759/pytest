import os
import requests
import re
import time
from bs4 import BeautifulSoup

f = open('config/stock_ref.props','r')
d = dict((x.split('=')[0:2]) for x in f.readlines())
# print(d['stock_available_total'])

t1 = time.time()
# r = requests.get('https://gupiao.baidu.com/stock/sh510130.html')
r = requests.get('https://gupiao.baidu.com/stock/sh601857.html')
# r.close()

r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
# p_elem = soup.select_one('#app-wrap > div.stock-info > div > div.price.s-up > span:nth-of-type(2)')
# p_elem = soup.select_one("dd.s-up")
# p_elem = soup.find('dt', text='最高')
stock_elem = {}
p_elem = soup.select_one('#app-wrap > div.stock-info > div > div.bets-content')
for p_elem in p_elem.find_all('dt'):
    v_elem = p_elem.find_next_sibling('dd')
    stock_elem[p_elem.get_text()] = v_elem.get_text()
# additional info
p_elem = soup.select_one('#app-wrap > div.stock-info > div > h1 > a.bets-name')
print('[',p_elem.get_text(),']')
for c in p_elem.get_text():
    print(c,'-',ord(c))
p = re.compile('\n[ ]+(.*)\((\d+)\)')
m = re.match(p, p_elem.get_text())
stock_name, stock_code = m.groups()
stock_elem['name'] = stock_name
stock_elem['code'] = stock_code


# p_elem = p_elem.find('dt', text='最高')
# n = p_elem.find_next_sibling('dd')
t2 = time.time()
print(stock_elem, ' time cost:', str(t2 - t1) )


