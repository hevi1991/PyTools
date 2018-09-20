#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from lxml import html

def parse():
    """ 将html文件中的内容, 使用xpath进行提取 """
    # 读取文件中的内容
    f = open("./static/index.html", "r", encoding="utf-8")
    s = f.read()

    selector = html.fromstring(s)
    # 解析h3标题
    h3 = selector.xpath('/html/body/h3/text()')[0]
    print(h3)

    print("---")
    # 解析ul下面的内容
    ul = selector.xpath('/html/body/ul/li')
    print(len(ul))
    for li in ul:
        print(li.xpath('text()')[0])

    print("---")
    # 解析ul指定的元素值
    #ul2 = selector.xpath('//ul/li[@class="important"]/text()')[0]
    ul2 = selector.xpath('//li[@class="important"]/text()')[0]
    print(ul2)

    print("---")
    # 解析a标签内容
    a = selector.xpath('//div[@id="container"]/a')[0]
    # 标签内的内容
    print(a.xpath('text()')[0])
    # href属性
    print(a.xpath('@href')[0])
    f.close()

    print("---")
    # 取特定位置的标签内容
    p = selector.xpath('/html/body/p[last()]/text()')
    print(p[0])

if __name__ == '__main__':
    parse()