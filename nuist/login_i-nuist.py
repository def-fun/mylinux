#!/usr/bin/env python3
import requests
from pprint import pprint
import time
import json

URL = 'http://a.nuist.edu.cn/index.php/index/login'
payload = 'username=20181213021&domain=NUIST&password=YWJyYWNhZGFicmEwNDI2&enablemacauth=0'


def log(info, func):
    item = {
        'func': func,
        'info': info,
        'timestamp': time.time(),
    }
    with open('login.log', 'a') as f:
        f.write(str(item))
        f.write('\n')


def login_nuist():
    h = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Origin': 'http://a.nuist.edu.cn',
        'Referer': 'http://a.nuist.edu.cn/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
    }
    r = requests.post(URL, data=payload, headers=h)
    d = json.loads(r.text)
    pprint(d)
    log(d, 'login_nuist()')


def check():
    url = 'http://a.nuist.edu.cn/index.php/index/init?_={}'.format(int(time.time() * 1000))
    h = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Referer': 'http://a.nuist.edu.cn/',
    }
    r = requests.get(url, headers=h)
    d = json.loads(r.text)
    pprint(d)
    log(d, 'check()')
    if d.get('info') != '用户已登录':
        login_nuist()


if __name__ == '__main__':
    # main()
    check()
