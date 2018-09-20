#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests


def get_book():
    """获取书本的信息"""
    url = 'http://search.dangdang.com'
    rest = requests.get(url, params={
        'key': '9787115428028',
        'act': input
    })
    print(rest.text)

    # json的方式获取数据, 通过.json()方式转化为python字典
    # requests.post()
    print(rest.status_code)
    print(rest.encoding)

if __name__ == '__main__':
    get_book()
