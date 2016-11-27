import requests
import pprint
from bs4 import BeautifulSoup


def parse_content(stock_url, selector_list):
    # 'https://gupiao.baidu.com/stock/sh601857.html'
    r = requests.get(stock_url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    rs_dict = {}
    for elem_name in selector_list:
        selector = selector_list[elem_name]
        p_elem = soup.select_one(selector)
        if p_elem is not None:
            rs_dict[elem_name] = p_elem.get_text()
    return rs_dict


def main():
    url = 'https://gupiao.baidu.com/stock/sh510130.html'
    with open('config/stock_ref.props', 'r') as f:
        d = dict((x.split('=')[0:2]) for x in f.readlines())
    p = parse_content(url, d)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(p)

if __name__ == '__main__':
    print('ok')
    main()
