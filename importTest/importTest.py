# coding:utf-8
__author__ = 'sunyawei'
import importlib
#
demo00 = "demo00"
demo = __import__(demo00)
demo.gets()

demo000 = "cd"
d = __import__(demo000)
print(d)
print(d.gets())

