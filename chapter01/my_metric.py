#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def decorator(*args, **kw):
        start = time.time()
        print('%s执行开始执行' % fn.__name__)
        result = fn(*args, **kw)
        end = time.time()
        print('%s执行完成, 耗时: %.2f s' % (fn.__name__, end - start))
        return result
    return decorator

if __name__ == '__main__':
    # 测试
    @metric
    def fast(x, y):
        time.sleep(0.0012)
        return x + y;


    @metric
    def slow(x, y, z):
        time.sleep(0.1234)
        return x * y * z;


    f = fast(11, 22)
    s = slow(11, 22, 33)
    if f != 33:
        print('测试失败!')
    elif s != 7986:
        print('测试失败!')