# coding:utf-8
from abc import abstractmethod

__author__ = 'sunyawei'
# 代理模式   A love  B  ，A1 instead of A doing something      instead of sb doing 代替某人做某事

class Woman():  # B
    def __init__(self, name):
        self.name = name
        pass


class Pursuit():
    @abstractmethod
    def send_flower(self):
        pass

    @abstractmethod
    def send_chocolate(self):
        pass

    @abstractmethod
    def send_book(self):
        pass


class A(Pursuit):
    def __init__(self, name, woman):
        self.woman = woman
        self.name = name
        pass
    # 实际上真正在干活的在这里
    def send_flower(self):
        print "%s   送了    %s99朵玫瑰"%(self.name, self.woman.name)

    def send_book(self):
        print "%s   送了    %s99本书" % (self.name, self.woman.name)

    def send_chocolate(self):
        print"%s   送了    %s99块巧克力"% (self.name, self.woman.name)


class Proxy(Pursuit):
    def __init__(self, proxyName, man_name, woman):
        self.proxyName = proxyName
        self.proxy = A(man_name, woman)
        pass
# 这个就没再干活，调用干活的方法让实际干活的人去干活
    def send_chocolate(self):
        self.proxy.send_chocolate()
        pass

    def send_book(self):
        self.proxy.send_book()

    def send_flower(self):
        self.proxy.send_book()

p = Proxy("小B", "小A", Woman("大MM"))
p.send_book()
p.send_chocolate()
p.send_flower()
# 看着是小B送给大MM礼物，其实送礼物的是小A
# 小A和大MM没有直接接触 ，而是代理小B在处理事情
