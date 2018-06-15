# coding:utf-8
import copy
import sys

__author__ = 'sunyawei'
class Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_object(Class, *args, **kwargs):
    return Class(*args, **kwargs)

point1 = Point(1, 2)
point2 = eval("{}({}, {})".format("Point", 2, 4)) # Risky
point3 = getattr(sys.modules[__name__], "Point")(3, 6)
point4 = globals()["Point"](4, 8)
point5 = make_object(Point, 5, 10)
point6 = copy.deepcopy(point5)
point6.x = 6
point6.y = 12
point7 = point1.__class__(7, 14) # could have used any of point1 to point6
'''
Point1是按照传统方式创建的，我们把Point类对象当成构造器使用，其它point对象则是动态创建出来的，其中，
在创建point2、point3和point4时，我们把类名当做参数传给相关函数。point6采用经典的原型方式创建：首先根据现有对象复制出新的对象，
然后在新对象上执行初始化或配置操作。point7是用point1的类对象创建出来的，创建时传入了新的参数。

　　由point6的创建过程可知，我们能够通过Python语言内置的copy.deepcopy()函数以原型法来创建对象。而point7则告诉大家，
这项任务在Python语言中还有更优雅的实现方式：无需先克隆对象，然后再修改新对象，而是可以直接用新参数来创建新对象，
这样做效率会高很多。
'''