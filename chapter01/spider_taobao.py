#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html
import time

def spider(sncode, book_list=[]):
    """ 抓取淘宝数据 """
    url = "https://s.taobao.com/search?data-key=sort&data-value=sale-desc&ajax=true&q={0}&imgfile=&js=1&ie=utf8&sort=sale-desc".format(sncode)
    html_data = requests.get(url)
    count = 2

    while len(html_data.content) == 0:
        if count > 10:
            print("抓取超出次数...放弃尝试")
            return
        print("第{0}次抓取淘宝数据...".format(count))
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

            book_list.append({
                "title": title,
                "link": link,
                "price": price,
                "store": store
            })
    except KeyError as e:
        print("淘宝网-没有找到结果")
    finally:
        return book_list


if __name__ == '__main__':
    spider("9787115428028")
