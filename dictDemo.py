#-*-coding:utf-8 -*-
from collections import Iterator

__author__ = 'sunyawei'


a=dict() # 传入关键字
b=dict({"A":"a","B":"b","C":"c","D":"d","E":"e"})# 映射函数方式来构造字典
c=dict(zip(["A","B","C"],["a","b","c"])) # 可迭代对象方式来构造字典
d=dict([("A","a"),("B","b"),("C","c")]) # 可迭代对象方式来构造字典

class A1():
    def __init__(self,name,aa):
        self.name=name
        self.aa=aa

d_dict=list({"a","b","c","d","e"})
c_dict=list({"a","b","c","d","e"})
print(d_dict.count("a"))


class A1(object):
    pass

class B1(A1):
    def __init__(self):
        pass
print(isinstance(A1(),Iterator))
print(isinstance(B1(),A1))

print(('type(A1())==A1'),type(A1())==A1)
print(('type(B1())==A1'),type(B1())==A1)

from collections import Iterator
class A(object):
    def __iter__(self):
        pass
    def next(self):
        pass
print(isinstance(A(), Iterator))
