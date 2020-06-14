# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   Description: learn threading module
        支持守护线程，主线程会等待所有非守护线程完成后才退出，主线程退出时不需要等待守护线程完成；
        自身已包含同步机制；

   Author: hushutao
   Create_Date: 2020/6/14
-------------------------------------------------
"""

import threading
from time import sleep, ctime
from atexit import register

loops = [4, 2]


def loop(nloop, sec):
    print ('start loop', nloop, 'at:', ctime())
    sleep(sec)
    print ('loop', nloop, 'done at:', ctime())


class ThreadFunc(object):
    def __init__(self, func, args, func_name=''):
        self.func = func
        self.args = args
        self.func_name = func_name

    def __call__(self, *args, **kwargs):
        self.func(*self.args)


class MyThread(threading.Thread):
    def __init__(self, func, args, func_name=''):
        super(MyThread, self).__init__()  # 必须先调用其基类的构造函数
        self.func = func
        self.args = args
        self.func_name = func_name

    def run(self):
        self.func(*self.args)


# 主线程退出之前执行
@register
def _atexit():
    print ('all Done at:', ctime())


# 函数实现
def func_main():
    print ('starting at', ctime())
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        th = threading.Thread(target=loop, args=(i, loops[i]))
        # th.daemon = True
        th.start()
        threads.append(th)

    for i in nloops:
        threads[i].join()

    print ('all Done at:', ctime())


# 可调用的类实例
def called_class_main():
    print ('starting at', ctime())
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        th = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        # th.daemon = True
        th.start()
        threads.append(th)

    for i in nloops:
        threads[i].join()

    print ('all Done at:', ctime())


# 继承实现
def inherit_main():
    print ('starting at', ctime())
    nloops = range(len(loops))
    threads = []
    for i in nloops:
        th = MyThread(loop, (i, loops[i]), loop.__name__)
        # th.daemon = True
        th.start()
        threads.append(th)

    # for i in nloops:
    #     threads[i].join()

    # print ('all Done at:', ctime())


if __name__ == '__main__':
    # func_main()
    # called_class_main()
    inherit_main()
