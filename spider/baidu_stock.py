import requests
import re
import pprint
from bs4 import BeautifulSoup


def parse_content(stock_url):
    # 'https://gupiao.baidu.com/stock/sh601857.html'
    r = requests.get(stock_url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    stock_elem = {}
    p_elem = soup.select_one('#app-wrap > div.stock-info > div > div.bets-content')
    for p_elem in p_elem.find_all('dt'):
        v_elem = p_elem.find_next_sibling('dd')
        stock_elem[p_elem.get_text()] = v_elem.get_text()
    # additional info
    p_elem = soup.select_one('#app-wrap > div.stock-info > div > h1 > a.bets-name')
    p = re.compile('\n[ ]+(.*)\((\d+)\)')
    m = re.match(p, p_elem.get_text())
    stock_name, stock_code = m.groups()
    stock_elem.update({'name':stock_name, 'code':stock_code})
    return stock_elem

def main():
    # url = 'https://gupiao.baidu.com/stock/sh510130.html'
    for stockinfo in load_stocks():
        url = 'https://gupiao.baidu.com/stock/sh{0}.html'.format(stockinfo[0])
        stock = parse_content(url)

    with open('config/stock_ref.props', 'r') as f:
        d = dict((x.split('=')[0:2]) for x in f.readlines())
    p = parse_content(url)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(p)

if __name__ == '__main__':
    main()
