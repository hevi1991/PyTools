#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html


def spider(sncode, book_list=[]):
    """ 爬取一号店数据 """
    url = "https://search.yhd.com/c0-0/k{sncode}/".format(sncode=sncode)
    # 获取html源码
    html_data = requests.get(url).text
    # xpath对象
    selector = html.fromstring(html_data)
    # 书籍列表
    item_box = selector.xpath('//div[@class="mod_search_pro"]/div[@class="itemBox"]')
    # 解析数据
    for item in item_box:
        # 标题
        a = item.xpath('*[@class="proName clearfix"]/a')[0]
        title = a.xpath('text()')
        title = "".join(title).replace("\n", "")

        # 购买链接
        link = "https:" + item.xpath('*[@class="proName clearfix"]/a/@href')[0]

        # 购买价格
        price = item.xpath('*[@class="proPrice"]/em/text()')
        price = "".join(price).replace("\n", "")

        # 商家
        is_yhd = a.xpath('span[@class="subscribe_self"]/text()')
        store = "".join(item.xpath('*[@class="storeName limit_width"]/a/text()')).replace("\n", "")
        store = "({is_yhd}){store}".format(is_yhd=is_yhd[0], store=store) if is_yhd != [] else store

        book_list.append({
            "title": title,
            "link": link,
            "price": price,
            "store": store
        })

if __name__ == '__main__':
    spider("9787115428028")
