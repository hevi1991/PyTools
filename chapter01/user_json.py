#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json


def python_to_json():
    """ 将python对象转换成json """
    d = {
        "name": "Python书籍",
        "origin_price": 66,
        "pub_date": "2018-4-14 17:00:00",
        "store": [
            "京东",
            "淘宝"
        ],
        "author": [
            "张三",
            "李四",
            "Jhone"
        ],
        "is_valid": True,
        "is_sale": False,
        "meta": {
            "isbn": "abc-123",
            "pages": 300
        },
        "desc": None
    }
    rest = json.dumps(d, ensure_ascii=False, indent=4)
    print(rest)


def json_to_python():
    """ 将json转换为python """
    # 多行文本""" """
    d = """
    {
        "name": "Python书籍",
        "origin_price": 66,
        "pub_date": "2018-4-14 17:00:00",
        "store": [
            "京东",
            "淘宝"
        ],
        "author": [
            "张三",
            "李四",
            "Jhone"
        ],
        "is_valid": true,
        "is_sale": false,
        "meta": {
            "isbn": "abc-123",
            "pages": 300
        },
        "desc": null
    }
    """
    rest = json.loads(d)
    print(rest)

def json_to_python_from_file():
    """ 从文件读取内容, 转化为python对象 """
    f = open("./static/book.json", "r")
    s = f.read()
    f.close()
    rest = json.loads(s)
    print(rest)

if __name__ == '__main__':
    python_to_json()
    json_to_python()
    json_to_python_from_file()