#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from typing import NamedTuple

import requests
from lxml import html

from my_metric import metric


class BookEntity(NamedTuple):
    """ 书本信息 """
    title: str
    price: float
    link: str
    store: str

    def __str__(self):
        return '价格: {self.price} ; 购买链接: {self.link} ; 名称: {self.title} ; 店铺: {self.store}'.format(self=self)

class MySpider(object):

    def __init__(self, sncode):
        self.sncode = sncode
        self.book_list = []

    @metric
    def dangdang(self):
        """ 爬取当当网数据 """
        url = 'http://search.dangdang.com/?key={sncode}&act=input'.format(sncode=self.sncode)
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
                price = li.xpath(
                    'div[@class="ebook_buy"]/p[@class="price e_price"]/span[@class="search_now_price"]/text()')
            price = price[0].replace('¥', '')

            # 商家
            store = li.xpath('p[@class="search_shangjia"]/a[@name="itemlist-shop-name"]/text()')
            store = '当当自营' if store == [] else store[0]

            book = BookEntity(**{
                "title": title[0],
                "link": link[0],
                "price": price,
                "store": store
            })
            self.book_list.append(book)
        return self.book_list

    @metric
    def jd(self):
        """ 爬取京东数据 """
        url = "https://search.jd.com/Search?keyword={sncode}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wtype=1&click=1".format(sncode=self.sncode)

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
            link = "https:{0}".format(a.xpath('@href')[0])

            # 购买价格
            price = li.xpath('div[@class="p-price"]/strong/i/text()')

            # 商家
            store = li.xpath('div[@class="p-shop"]//a[@class="curr-shop"]/text()')[0] if li.xpath(
                'div[@class="p-shop"]//a[@class="curr-shop"]/text()') != [] else ""

            book = BookEntity(**{
                "title": title[0],
                "link": link,
                "price": price[0],
                "store": store
            })
            self.book_list.append(book)

    @metric
    def yhd(self):
        """ 爬取一号店数据 """
        url = "https://search.yhd.com/c0-0/k{sncode}/".format(sncode=self.sncode)
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

            self.book_list.append(BookEntity(**{
                "title": title,
                "link": link,
                "price": price,
                "store": store
            }))

    @metric
    def taobao(self):
        """ 抓取淘宝数据 """
        url = "https://s.taobao.com/search?data-key=sort&data-value=sale-desc&ajax=true&q={0}&imgfile=&js=1&ie=utf8&sort=sale-desc".format(self.sncode)
        html_data = requests.get(url)
        count = 2
        while len(html_data.content) == 0:
            if count > 10:
                print("taobao抓取超出10次...放弃尝试")
                return
            html_data = requests.get(url)
            time.sleep(1)
            count += 1

        html_data = html_data.json()

        try:
            item_list = html_data["mods"]["itemlist"]["data"]["auctions"]
            for item in item_list:
                # 标题
                title = item["raw_title"]

                # 链接
                link = "https:" + item["detail_url"]

                # 价格
                price = item["view_price"]

                # 商家
                store = item["nick"]

                self.book_list.append(BookEntity(**{
                    "title": title,
                    "link": link,
                    "price": price,
                    "store": store
                }))
        except KeyError as e:
            print("淘宝网-没有找到结果")

    def spider(self):
        # 爬取各大网站的数据
        self.dangdang()
        self.jd()
        self.yhd()
        self.taobao()

        # 得到排序后的数据
        book_list = sorted(self.book_list, key=lambda item: float(item.price), reverse=False)
        for book in book_list:
            print(book)

if __name__ == '__main__':
    sncode = input("请输入ISBN:")
    client = MySpider(sncode)
    client.spider()