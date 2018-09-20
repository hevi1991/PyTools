#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from spider_dangdang import spider as dangdang
from spider_jd import spider as jd
from spider_yhd import spider as yhd
from spider_taobao import spider as taobao

def main(sncode):
    """ 图书比价工具整合 """

    book_list = []

    # 当当网图书数据
    dangdang(sncode, book_list)
    print('当当网数据爬取完成')

    # 京东网图书数据
    jd(sncode, book_list)
    print('京东网数据爬取完成')

    # 一号店网图书数据
    yhd(sncode, book_list)
    print('一号店网数据爬取完成')

    # 淘宝网图书数据
    taobao(sncode, book_list)
    print('淘宝网数据爬取完成')

    pass
    # 排序书的数据
    if book_list == []:
        print("没有找到{0}的查询结果".format(sncode))
        return
    else:
        book_list = sorted(book_list, key=lambda item : float(item["price"]), reverse=True)
        for book in book_list:
            print(book)

if __name__ == '__main__':
    # sn = input('请输入ISBN:')
    # main(sn)

    main("9787115416940")
    # "9787115470669"
    # "9787115416940"
    # "9787115428028"