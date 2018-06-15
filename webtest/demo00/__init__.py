# coding:utf-8
__author__ = 'sunyawei'

from flask import Blueprint
def __getattr__(self, funcname):
    if self.module is None:
        self.module = __import__(self.module_name)
        print(self.module)
    return getattr(self.module, funcname)
__author__ = 'sunyawei'
print(__name__+"初始化")

demo00 = Blueprint("demo00", __name__)
from webtest.demo00 import view

