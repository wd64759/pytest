import re
import pprint


def load_stocks():
    stock_list = []
    with open('config/stock_sh.list',encoding='utf-8') as f:
        line = f.readline()
        while line:
            p = re.compile('(.*)\((\d+)\)',re.U)
            m = re.match(p, line)
            if m is not None:
                stock_list.append(m.groups()[::-1])
            line = f.readline()
    return stock_list

if __name__ == '__main__':
    pprint.pprint(load_stocks())