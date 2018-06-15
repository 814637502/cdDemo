#!/usr/bin/python
# coding:utf8


class Animal(object):
    """
    Singleton
    ：name
    """
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):#如果没有这个属性
            cls._instance = super(Animal, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, name):
            self.name = name
aa = dict(a="wangling")
cat = Animal(name="i'm a smart cat ")
cat1 = Animal(name="i'm a smart cows ")
cat.name = "no"
print(id(cat) is id(cat1))
print(id(cat), id(cat1), (id(cat1) == id(cat)))
print(cat.__dict__)
print(cat1.__dict__)

