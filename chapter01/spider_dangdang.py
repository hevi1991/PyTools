#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html

def spider(sncode, book_list=[]):
    """ 爬取当当网数据 """
    url = 'http://search.dangdang.com/?key={sncode}&act=input'.format(sncode=sncode)
    # 获取html内容
    html_data = requests.get(url)

    # xpath对象
    selector = html.fromstring(html_data.text)
    ul_list = selector.xpath('//*[@id="search_nature_rg"]/ul/li')
    for li in ul_list:
        # 标题
        title = li.xpath('a/@title')

        # 购买链接
        link = li.xpath('a/@href')

        # 购买价格
        price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
        if not price:
            price = li.xpath('div[@class="ebook_buy"]/p[@class="price e_price"]/span[@class="search_now_price"]/text()')
        price = price[0].replace('¥','')

        # 商家
        store = li.xpath('p[@class="search_shangjia"]/a[@name="itemlist-shop-name"]/text()')
        store = '当当自营' if store == [] else store[0]

        book_list.append({
            "title": title[0],
            "link": link[0],
            "price": price,
            "store": store
        })

    return book_list


if __name__ == '__main__':
    sn = '9787115428028'
    spider(sn)