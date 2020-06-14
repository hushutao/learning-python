# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   Description: learn thread module
       底层线程module，需要自己实现同步原语；
       对于线程何时退出没有控制，主线程结束时所有其他线程也会强制结束；
       该模块不支持守护线程的概念；
   Author: hushutao
   Create_Date: 2020/6/14
-------------------------------------------------
"""
import thread  # python3中重命名为_thread
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, sec, lock):
    print ('start loop', nloop, 'at:', ctime())
    sleep(sec)
    print ('loop', nloop, 'done at:', ctime())
    lock.release()


def main():
    print ('starting at', ctime())
    locks = []
    nloops = range(len(loops))
    for i in nloops:
        lock = thread.allocate_lock()  # LockType
        lock.acquire()
        locks.append(lock)
    for i in nloops:
        thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    print ('all Done at:', ctime())


if __name__ == '__main__':
  main()
