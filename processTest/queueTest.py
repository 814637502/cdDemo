#-*-coding:utf-8-*-
from multiprocessing import Process,Queue
import random
import time

__author__ = 'sunyawei'


# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

print("==============================================================================================================")

# def write(q):
#     for a in ('A1','A2''A3''A4'):
#         q.put(a)
#         print("add one value to queue")
#
#
#
# def read(q):
#     while 1:
#         value = q.get()
#         print(value)
#
# if __name__ =="__main__":
#     q = Queue()
#     pw = Process(target = write, args=(q,))
#     pr = Process(target = read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()
#     # 父进程创建Queue，并传给各个子进程：
#     # q = Queue()
#     # pw = Process(target=write, args=(q,))
#     # pr = Process(target=read, args=(q,))
#     # # 启动子进程pw，写入:
#     # pw.start()
#     # # 启动子进程pr，读取:
#     # pr.start()
#     # # 等待pw结束:
#     # pw.join()
#     # # pr进程里是死循环，无法等待其结束，只能强行终止:
#     # pr.terminate()
#     print 'Process end.'



