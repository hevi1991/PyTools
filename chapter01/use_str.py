#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def format_str():
    """ 格式化字符串 """
    name = "张三"
    print("你好, %s" % name)
    print("你好好, %(name)s" % {'age': 12, 'name': name})

    # 整型, 小数
    num = 12.135234
    print("num: %.2f" % num)
    print("code: %04d" % num)

def format_str_2():

    # 使用位置占位
    print('欢迎您, {0}, {1} --- {0}'.format('张九', '驾到'))

    # 使用名称
    print('您好, {username}, 您的编号是{num}.'.format(username="张枫", num=93))

    d = {
        'username': '李春华',
        'num': 67
    }
    print('您好, {username}, 您的编号是{num}.'.format(**d))

    point = (9, 2)
    print('坐标位置: {0[0]}:{0[1]}'.format(point))

    p = User('Peter', 27)
    print(p.show())

class User(object):
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def show(self):
        return '用户:{self.username}, 年龄:{self.age}'.format(self=self)

if __name__ == '__main__':
    # format_str()
    format_str_2()
