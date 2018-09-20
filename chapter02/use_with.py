#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

def open_file():
    """ 使用With语法打开一个文件 """

    # 不使用with语法:
    f = open("./static/test2.txt", "r", encoding="utf-8")
    try:
        rest = f.read()
        print(rest)
    except BaseException as e:
        logging.exception(e)
    finally:
        f.close()

    # 使用with语法:
    with open("./static/test.txt", "r", encoding="utf-8") as f:
        rest = f.read()
        print(rest)

if __name__ == '__main__':
    open_file()