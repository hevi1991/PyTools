#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html

def spider(sncode, book_list=[]):
    """ 爬取京东数据 """
    url = "https://search.jd.com/Search?keyword={sncode}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wtype=1&click=1".format(sncode = sncode)

    # 从网上取数据
    html_data = requests.get(url)
    html_data.encoding = "utf-8"

    # 转化成xpath取dom内容
    selector = html.fromstring(html_data.text)

    ul_list = selector.xpath('//*[@id="J_goodsList"]/ul/li[@class="gl-item"]/div[@class="gl-i-wrap"]')
    # 输出结果
    for li in ul_list:
        a = li.xpath('div[@class="p-img"]/a')[0]
        # 标题
        title = a.xpath('@title')

        # 购买链接
        link = "https://{0}".format(a.xpath('@href')[0])

        # 购买价格
        price = li.xpath('div[@class="p-price"]/strong/i/text()')

        # 商家
        store = li.xpath('div[@class="p-shop"]//a[@class="curr-shop"]/text()')[0] if li.xpath('div[@class="p-shop"]//a[@class="curr-shop"]/text()') != [] else ""

        book_list.append({
            "title": title[0],
            "link": link,
            "price": price[0],
            "store": store
        })

    return book_list

if __name__ == '__main__':
    spider("9787115428028")