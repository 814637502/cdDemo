# -*-coding:utf-8 -*-
__author__ = 'sunyawei'
# 自定义支持with的对象

class dbCon:
    def __init__(self,tag):
        self.tag = tag

    def __enter__(self):
        print(self.tag+"这里是__enter__")
        print("我在这可以获取一个db连接")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_tb)
        # 如果不是none说明出异常了
        if exc_tb:
            self.tag = "failed"
            print("出异常了 快来看看"+exc_tb)
        else:
            self.tag = "success"
            print("执行完成  没有异常")

# 自定义类创建完了 现在开始测试with

with dbCon("aa"):
    print("我开始执行任务了")
    # raise Exception


print("==================================用contextlib模块         contextmanager=========================================")

# 用contextlib模块

# contextlib 里面有三个对象 装饰器contextmanager 函数nested和上下文管理器closing可以对已有的生成器 函数或者对象进行包装 加入对上下文
# 管理协议的支持避免专门编写上线管理器来支持with语句

from contextlib import contextmanager

@contextmanager
def demo():
    print ("连接数据库先获取到数据库连接")
    a = 12000

    #这里的yield可把数据赋值给as 后面的参数
    yield a

    print("执行完了要释放连接")



with demo() as value:
    print("我要在这里去处理一些业务的")
    # value 的数据是yield给的
    print(value)



print("==================================用contextlib模块         closing=========================================")

# 上下文管理 closing 实现
class closing(object):
    # help doc here
    def __init__(self, thing):
        self.thing = thing
    def __enter__(self):
        return self.thing
    def __exit__(self, *exc_info):
        self.thing.close()



class ClosingDemo(object):
    def __init__(self):
        self.acquire()
    def acquire(self):
        print 'Acquire resources.'
    def free(self):
        print 'Clean up any resources acquired.'
    def close(self):
        self.free()

with closing(ClosingDemo()):
    print 'Using resources'